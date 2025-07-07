import re
from typing import Final

EXCLUDE_INVERT_E: Final[set[str]] = {
    r'(\s*)<meta content="MATHENAUTICA" property="og:site_name"/>',
    r'(\s*)<title>(.+) - MATHENAUTICA</title>'
}

def replace_custom_menu_title(html_text: str) -> str:
    return html_text.replace(
        '<h1 class="menu-title">',
        '<h1 class="custom-menu-title">',
    )

def invert_e(html_text: str) -> str:
    replaced = html_text
    matched = re.finditer(r"(.*)(MATHENAUTICA)(.*)", replaced)
    for match in list(matched)[::-1]:
        for exclude in EXCLUDE_INVERT_E:
            if re.match(exclude, match.group(0)):
                break
        else:
            replaced = replaced[:match.start(2)] + "MATH<div class='invert-e'>E</div>NAUTICA" + replaced[match.end(2):]

    return replaced
