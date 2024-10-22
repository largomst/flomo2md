from bs4 import BeautifulSoup


def test_success_export_flomo_note_to_markdown():
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
- B
""",
            'files': [],
        }
    ]
    get = flome2json(source)
    assert want == get


def flome2json(source):
    soup = BeautifulSoup(source, 'html.parser')
    memo_div = soup.find('div', class_='memo')
    content = []
    for element in memo_div.children:
        if element.name == 'p':
            content.append(element.get_text())
        elif element.name == 'ul':
            for li in element.find_all('li'):
                content.append(f"- {li.get_text()}")
    return [
        {
            'time': '2024-10-22 13:13:53',
            'content': "\n".join(content),
            'files': [],
        }
    ]
