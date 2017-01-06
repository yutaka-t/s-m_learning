<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding:utf-8 -*-

=======
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# ライブラリを取り込む
from bs4 import BeautifulSoup

# 解析したいHTML
html = """
<html><body>
    <h1>スクレイピングとは?</h1>
    <p>Webページを解析すること。</p>
    <p>任意の個所を抽出すること</p>
</body></html>
"""

# HTMLを解析する
soup = BeautifulSoup(html, 'html.parser')

# 任意の部分を抽出する
h1 = soup.html.body.h1
p1 = soup.html.body.p
>>>>>>> 278d62e934f37dabdf2fadda6b2e3aa70888f0f9
