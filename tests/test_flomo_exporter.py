from bs4 import BeautifulSoup
import html2text
import mistune


def test_success_export_flomo_html_to_json():
    source = """
<html>
<body>
<div class="memo">
    <p>A</p>
    <ul> <li><p>B</p></li> </ul>
</div>
</body>
</html>
"""
    want = [
        {
            'time': '2024-10-22 13:13:53',
            'content': """A
- B""",
            'files': [],
        }
    ]
    get = flomo2json(source)
    assert want == get


def flomo2json(source):
    bs = BeautifulSoup(source, 'html.parser')
    result = []

    for memo in bs.find_all('div', class_='memo'):
        h = html2text.HTML2Text()
        markdown = h.handle(str(memo))
        item = {'time': '', 'content': markdown, 'files': []}
        result.append(item)

    return result
