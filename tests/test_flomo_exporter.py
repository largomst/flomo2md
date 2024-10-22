from bs4 import BeautifulSoup
import html2text
import markdownify


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


def flomo2json(source):
    bs = BeautifulSoup(source, 'html.parser')
    result = []
    for memo in bs.find_all('div', class_='memo'):
        time = memo.find('div', class_='time').text

        content = memo.find('div', class_='content')
        markdown = markdownify.markdownify(str(content))

        imgs = memo.find_all('img')
        links = []
        for img in imgs:
            links.append(img['src'])

        item = {
            'time': time,
            'content': markdown,
            'files': links,
        }
        result.append(item)

    return result
