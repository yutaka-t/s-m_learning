#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup


def sel(q):
    print(soup.select_one(q).string)


books_html = """
<ul id="bible">
    <li id="ge">Genesis</li>
    <li id="ex">Exodus</li>
    <li id="le">Leviticus</li>
    <li id="nu">Numbers</li>
    <li id="de">Deuteronomy</li>
</ul>"""

soup = BeautifulSoup(books_html, "html.parser")

# CSSセレクタで検索
# sel = lambda q : print(soup.select_one(q).string)
sel("#nu")
sel("li#nu")
sel("#bible #nu")
sel("#bible > #nu")
sel("ul#bible > li#nu")


