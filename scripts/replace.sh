#!/bin/bash

python -X utf8 ../../scripts/replace_book_to_site.py
python -X utf8 ../../scripts/replace_alert.py
python -X utf8 ../../scripts/replace_nav_chapters.py

# move book to docs
rm -rf ../../docs
mkdir ../../docs
mv ../html/* ../../docs
rm -rf ../../book