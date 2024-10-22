from bs4 import BeautifulSoup


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
                content.append(f'- {li.get_text()}')
    return [
        {
            'time': '2024-10-22 13:13:53',
            'content': '\n'.join(content).rstrip(),
            'files': [],
        }
    ]


def test_export_flomo_with_files_to_json():
    source = """ <div class="memo">
      <div class="time">2024-10-18 17:55:00</div>
      <div class="content">
        <p>#领域/产品/设计</p>
        <p>
          形式有时候就是本质。HTML
          的外观是人产生第一印象的地方。传达出这个网站是否是用心设计过的。
        </p>
        <ul>
          <li>漂亮的设计 https://v.flomoapp.com/mine/?memo_id=MTQwOTY1NTk4</li>
        </ul>
      </div>
      <div class="files">
        <img
          src="file/2024-10-18/1081485/1729245370.2828069_6T3Afmea.jpg"
        /><img
          src="file/2024-10-18/1081485/1729245370.282824_ccUqi8Dd.jpg"
        /><img src="file/2024-10-18/1081485/1729245370.282831_RRI2OmuW.jpg" />
      </div>
    </div>"""
    want = [
        {
            'time': '2024-10-18 17:55:00',
            'content': """#领域/产品/设计

形式有时候就是本质。HTML的外观是人产生第一印象的地方。传达出这个网站是否是用心设计过的。

漂亮的设计 https://v.flomoapp.com/mine/?memo_id=MTQwOTY1NTk4
""",
            'files': [
                'file/2024-10-18/1081485/1729245370.2828069_6T3Afmea.jpg',
                'file/2024-10-18/1081485/1729245370.282824_ccUqi8Dd.jpg',
                'file/2024-10-18/1081485/1729245370.282831_RRI2OmuW.jpg',
            ],
        }
    ]
    get = flome2json(source)
    assert want == get
