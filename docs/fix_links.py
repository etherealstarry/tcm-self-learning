#!/usr/bin/env python3
"""Fix remaining broken links in tcm-self-learning/docs/"""
import os, re

docs = "/Users/etherealstarry/WorkBuddy/2026-05-31-17-44-16/tcm-self-learning/docs"

# Build file map: basename -> list of relative paths
all_files = {}
for root, _, files in os.walk(docs):
    for f in files:
        if f.endswith('.md'):
            full = os.path.join(root, f)
            rel = os.path.relpath(full, docs).replace('\\', '/')
            all_files.setdefault(f, []).append(rel)

print(f"Indexed {len(all_files)} unique basenames")

fixed = 0
for root, _, files in os.walk(docs):
    for fname in files:
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(root, fname)
        rel_dir = os.path.relpath(root, docs).replace('\\', '/')
        if rel_dir == '.':
            rel_dir = ''

        with open(fpath, 'r', encoding='utf-8') as fp:
            content = fp.read()
        original = content

        # Find all [text](url) links
        for m in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', content):
            text, url = m.group(1), m.group(2)
            # Skip external / anchor-only links
            if re.match(r'https?://', url) or url.startswith('#') or url.startswith('mailto:'):
                continue
            # Strip anchor for target lookup
            target = url.split('#')[0].split('?')[0]
            if not target:
                continue

            # Resolve from current file's directory
            resolved = os.path.normpath(os.path.join(rel_dir, target)).replace('\\', '/')

            if resolved in all_files:
                continue  # Already correct

            # Try to find by basename
            bn = os.path.basename(target)
            candidates = all_files.get(bn, [])
            if len(candidates) == 0:
                continue  # Can't find, skip
            # Pick candidate sharing the most path components with current file
            if len(candidates) == 1:
                best = candidates[0]
            else:
                cur_parts = set(rel_dir.split('/')) if rel_dir else set()
                best = max(candidates, key=lambda c: len(set(c.split('/')[:-1]) & cur_parts))

            correct = os.path.relpath(best, rel_dir).replace('\\', '/') if rel_dir else best
            new_url = correct
            if '#' in url:
                new_url += '#' + url.split('#', 1)[1]

            old_link = f'[{text}]({url})'
            new_link = f'[{text}]({new_url})'
            if old_link in content:
                content = content.replace(old_link, new_link, 1)
                fixed += 1

        if content != original:
            with open(fpath, 'w', encoding='utf-8') as fp:
                fp.write(content)

print(f"Total links fixed: {fixed}")
