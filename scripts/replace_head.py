import re
from pathlib import Path
from typing import Final

BASE_HTML_DIR: Final[Path] = Path("../html")
DEPLOY_HTML_HTTPS: Final[str] = "https://volatilerye.github.io/mathenautica/"

def replace_ogp(html_text: str, html_path: Path) -> str:
    matched = re.search(r'<title>(.*) \- (.*)</title>', html_text)
    if not matched:
        return html_text # No match found, skip this file

    replaced = re.sub(
        r'<meta content="" property="og:title">',
        f'<meta content="{repr(matched.group(1))[1:-1]}" property="og:title">',
        html_text
    )
    replaced = re.sub(
        r'<meta content="" property="og:site_name">',
        f'<meta content="MATHENAUTICA" property="og:site_name">',
        replaced
    )
    replaced = re.sub(
        r'<meta content="" property="og:url">',
        f'<meta content="{DEPLOY_HTML_HTTPS}{html_path.relative_to(BASE_HTML_DIR)}" property="og:url">',
        replaced
    )        

    return replaced
