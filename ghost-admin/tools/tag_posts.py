#!/usr/bin/env python3
"""Apply a tag to a set of posts by slug, via the Ghost Admin API.

    ./tag_posts.py "Tag Name" tag-slug post-slug [post-slug ...]
    ./tag_posts.py "Tag Name" tag-slug --file slugs.txt
    ...add --apply to write; without it, this is a dry run.

Built 2026-08-30 to tag the four Architecture That Persuades posts, which were
published but untagged. Kept for the remaining untagged backlog (19 of 74 posts
carry no public tag as of that date).

WRITES TO THE LIVE SITE. Reads GHOST_ADMIN_API_KEY and GHOST_API_URL from the
repo .env, which must hold a current Admin key -- that key grants full read/write,
so remove it from .env when the tagging work is done. No third-party dependencies.

Behaviour worth knowing:
  - Existing tags are preserved; the new tag is prepended, so it becomes the
    post's PRIMARY tag (Source renders the primary tag on post cards).
  - A post that already carries the tag is skipped, so re-running is safe.
  - Only the `tags` field is sent, guarded by the post's updated_at for
    collision detection. Title, content and publish date are never touched.
  - Ghost creates the tag implicitly on first use; there is no separate step.
  - The tag slug must match routes.yaml and any {{#get}} filter in the theme
    exactly. A mismatch does not 404 -- the channel renders empty and gated
    cards silently never appear.
"""
import base64, hashlib, hmac, json, os, sys, time, urllib.request, urllib.error


def load_env(path):
    env = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env

def b64(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=")

def make_token(key):
    kid, secret = key.split(":")
    header = b64(json.dumps({"alg": "HS256", "typ": "JWT", "kid": kid}).encode())
    now = int(time.time())
    payload = b64(json.dumps({"iat": now, "exp": now + 300, "aud": "/admin/"}).encode())
    signing_input = header + b"." + payload
    sig = hmac.new(bytes.fromhex(secret), signing_input, hashlib.sha256).digest()
    return (signing_input + b"." + b64(sig)).decode()

def call(url, token, method="GET", body=None):
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"Ghost {token}")
    req.add_header("Accept-Version", "v5.0")
    data = None
    if body is not None:
        data = json.dumps(body).encode()
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, data) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        detail = e.read().decode()[:500]
        raise SystemExit(f"HTTP {e.code} on {method} {url}\n{detail}")

def parse_args(argv):
    args = [a for a in argv[1:] if a != "--apply"]
    if len(args) < 3:
        raise SystemExit(__doc__)
    tag_name, tag_slug, rest = args[0], args[1], args[2:]
    if rest[0] == "--file":
        with open(rest[1]) as f:
            slugs = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    else:
        slugs = rest
    return tag_name, tag_slug, slugs

def main():
    apply_changes = "--apply" in sys.argv
    TAG_NAME, TAG_SLUG, SLUGS = parse_args(sys.argv)
    env = load_env(os.path.expanduser("~/Documents/GitHub/bwf-source/.env"))
    key = env.get("GHOST_ADMIN_API_KEY", "")
    base = env.get("GHOST_API_URL", "").rstrip("/")
    if not key or ":" not in key:
        raise SystemExit("GHOST_ADMIN_API_KEY missing or malformed in .env (want id:secret)")

    token = make_token(key)
    api = f"{base}/ghost/api/admin"

    print(f"mode: {'APPLY' if apply_changes else 'DRY RUN'}   site: {base}")
    print(f"tag:  {TAG_NAME}  ({TAG_SLUG})   posts: {len(SLUGS)}\n")
    changed = skipped = 0
    for slug in SLUGS:
        res = call(f"{api}/posts/slug/{slug}/", token)
        post = res["posts"][0]
        existing = [t["slug"] for t in post.get("tags", [])]
        title = post["title"]

        if TAG_SLUG in existing:
            print(f"  SKIP  {title}\n        already tagged")
            skipped += 1
            continue

        # Preserve any existing tags; the new tag goes first so it becomes primary.
        new_tags = [{"name": TAG_NAME, "slug": TAG_SLUG}] + [
            {"slug": t["slug"], "name": t["name"]} for t in post.get("tags", [])
        ]
        print(f"  TAG   {title}")
        print(f"        {existing or 'no tags'}  ->  {[t['slug'] for t in new_tags]}")

        if apply_changes:
            call(f"{api}/posts/{post['id']}/", token, "PUT",
                 {"posts": [{"updated_at": post["updated_at"], "tags": new_tags}]})
            print("        written")
        changed += 1

    print(f"\n{changed} to change, {skipped} already correct")
    if not apply_changes and changed:
        print("Re-run with --apply to write.")

if __name__ == "__main__":
    main()
