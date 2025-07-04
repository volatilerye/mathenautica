import re
from pathlib import Path
from typing import Final

BASE_HTML_DIR: Final[Path] = Path("../html")
DEPLOY_HTML_HTTPS: Final[str] = "https://volatilerye.github.io/mathenautica/"

def replace_ogp(html: Path) -> None:
    with html.open(encoding="utf-8") as f:
        replaced = f.read()
        matched = re.search(r'<title>(.*) \- (.*)</title>', replaced)
        print(html)
        if not matched:
            return  # No match found, skip this file
        print(matched.group(1), matched.group(2))

        replaced = re.sub(
            r'<meta content="" property="og:title"/>',
            f'<meta content="MATHENAUTICA" property="og:title"/>',
            replaced
        )
        replaced = re.sub(
            r'<meta content="" property="og:site_name"/>',
            f'<meta content="{matched.group(2)}" property="og:site_name"/>',
            replaced
        )
        replaced = re.sub(
            r'<meta content="" property="og:url"/>',
            f'<meta content="{DEPLOY_HTML_HTTPS}{html.relative_to(BASE_HTML_DIR)}" property="og:url"/>',
            replaced
        )        

    with html.open("w", encoding="utf-8") as f:
        f.write(replaced)


if __name__ == "__main__":
    for html in BASE_HTML_DIR.glob("**/*.html"):
        replace_ogp(html)
