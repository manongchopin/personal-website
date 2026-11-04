#!/usr/bin/env python3
"""Build the mainland (CN) edition of the personal site.

The GitHub Pages edition keeps the working paper. The CN edition removes it
for ICP filing, rewrites the heritage-site link to /world/, and switches the
Umami domain filter to chopinfisher.com.

Usage: python3 build-cn.py
Output: dist-cn/  (not committed; deploy its contents to the OSS bucket root)
"""

from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dist-cn"
NEW_DOMAIN = "chopinfisher.com,www.chopinfisher.com"

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()

for name in ("index.html", "publications.html", "privacy.html", "style.css"):
    shutil.copy2(ROOT / name, OUT / name)

assets = OUT / "assets"
assets.mkdir()
for item in (ROOT / "assets").iterdir():
    if item.name in {".DS_Store", "papers"}:
        continue
    if item.is_dir():
        shutil.copytree(item, assets / item.name, ignore=shutil.ignore_patterns(".DS_Store"))
    elif item.is_file():
        shutil.copy2(item, assets / item.name)

html = (ROOT / "index.html").read_text(encoding="utf-8")
start = html.index('<h3 class="writing-subhead">工作论文 / Working Papers</h3>')
end = html.index('<h3 class="writing-subhead">小说 / Fiction</h3>')
html = html[:start] + html[end:]
html = html.replace("未刊的论文与小说。欢迎批评；引用请注明版本与日期。",
                    "未刊的小说与创作。欢迎批评。")
html = html.replace("https://manongchopin.github.io/guobao/", "/world/")
html = html.replace("<!-- ==================== 工作论文 ==================== -->",
                    "<!-- ==================== 写作 ==================== -->")
html = html.replace('data-domains="manongchopin.github.io"',
                    f'data-domains="{NEW_DOMAIN}"')
(OUT / "index.html").write_text(html, encoding="utf-8")

for name in ("publications.html", "privacy.html"):
    text = (ROOT / name).read_text(encoding="utf-8")
    text = text.replace('data-domains="manongchopin.github.io"',
                        f'data-domains="{NEW_DOMAIN}"')
    (OUT / name).write_text(text, encoding="utf-8")

leftovers = []
for p in OUT.rglob("*.html"):
    text = p.read_text(encoding="utf-8")
    for needle in ("assets/papers", "shaonian-digital-life", "manongchopin.github.io/guobao"):
        if needle in text:
            leftovers.append((str(p.relative_to(OUT)), needle))

print(f"built {OUT}")
print("excluded: papers/, assets/papers/")
print("heritage link: /world/")
print("umami domains:", NEW_DOMAIN)
print("leftovers:", leftovers if leftovers else "none")
