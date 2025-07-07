def replace_book_to_site(html_text: str) -> str:
    replaced = (
        html_text.replace(
            " to search in the book",
            " to search in the site",
        )
        .replace("Search this book ...", "Search this site ...")
    )

    return replaced
