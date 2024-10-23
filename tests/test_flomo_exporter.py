from bs4 import BeautifulSoup

from flomo_exporter.__main__ import flomo2json, memo2md


def test_success_export_flomo_html_to_json():
    source = """
<html>
<body>
<div class="memo">
    <div class="time">2024-10-22 13:13:53</div>
    <div class="content"><p>A</p><ul><li><p>B</p></li></ul></div>
    <div class="files">
        <img src="file/a.png">
    </div>
</div>
</body>
</html>
"""
    want = [
        {
            'time': '2024-10-22 13:13:53',
            'content': """A

* B
""",
            'files': ['file/a.png'],
        }
    ]
    get = flomo2json(source)
    assert want == get


def test_memo_div_has_files_to_md():
    source = """
<html>
<body>
<div class="memo">
    <div class="time">2024-10-22 13:13:53</div>
    <div class="content"><p>A</p><ul><li><p>B</p></li></ul></div>
    <div class="files">
        <img src="file/a.png">
    </div>
</div>
</body>
</html>
"""
    want = """# 2024-10-22 13:13:53

A

* B

images:
* ![](file/a.png)
"""
    bs = BeautifulSoup(source, 'html.parser')
    memo_div = bs.find('div', class_='memo')
    get = memo2md(memo_div)
    assert want == get


def test_memo_div_has_no_files_to_md():
    source = """
<html>
<body>
<div class="memo">
    <div class="time">2024-10-22 13:13:53</div>
    <div class="content"><p>A</p><ul><li><p>B</p></li></ul></div>
</div>
</body>
</html>
"""
    want = """# 2024-10-22 13:13:53

A

* B
"""
    bs = BeautifulSoup(source, 'html.parser')
    memo_div = bs.find('div', class_='memo')
    get = memo2md(memo_div)
    assert want == get
