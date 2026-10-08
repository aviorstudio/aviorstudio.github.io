"""Validate the existing public redirect and optionally stage its static artifact."""
from html.parser import HTMLParser
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import urlsplit

class Redirect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonical = []
        self.refresh = []
        self.in_script = False
        self.scripts = []
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical.append(values.get("href"))
        if tag == "meta" and values.get("http-equiv", "").lower() == "refresh":
            self.refresh.append(values.get("content", ""))
        if tag == "script":
            self.in_script = True
    def handle_endtag(self, tag):
        if tag == "script":
            self.in_script = False
    def handle_data(self, data):
        if self.in_script:
            self.scripts.append(data)

root = Path(__file__).resolve().parents[1]
parser = Redirect()
parser.feed((root / "index.html").read_text())
target = "https://www.avior.studio/"
assert urlsplit(target).scheme == "https"
assert parser.canonical in ([target], [target.rstrip("/")]), "canonical redirect target changed"
assert len(parser.refresh) == 1 and re.fullmatch(r"0;\s*url=" + re.escape(target), parser.refresh[0]), "refresh must immediately use the canonical destination"
assert len(parser.scripts) == 1 and re.fullmatch(r"\s*location\.replace\([\"']" + re.escape(target) + r"[\"']\);?\s*", parser.scripts[0]), "script redirect must use the canonical destination"
assert sys.argv[1:] in ([], ["--build"]), "usage: check.py [--build]"
if sys.argv[1:]:
    output = root / ".artifacts/dist"
    output.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / "index.html", output / "index.html")
print("Canonical, refresh and script redirect targets agree")
