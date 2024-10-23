import markdownify
from bs4 import BeautifulSoup


def flomo2json(source):
    bs = BeautifulSoup(source, 'html.parser')
    result = []
    for memo in bs.find_all('div', class_='memo'):
        item = memo2json(memo)
        result.append(item)

    return result


def memo2json(memo_div):
    time = memo_div.find('div', class_='time').text

    content = memo_div.find('div', class_='content')
    markdown = markdownify.markdownify(str(content))

    imgs = memo_div.find_all('img')
    links = []
    for img in imgs:
        links.append(img['src'])

    item = {
        'time': time,
        'content': markdown,
        'files': links,
    }

    return item


def memo2md(memo_div):
    item = memo2json(memo_div)
    time = item['time']
    content = item['content']
    files = item['files']
    images = '\n'.join([f'* ![]({x})' for x in files])

    return create_md(time, content, images)


def create_md(time, content, images):
    return f"""# {time}
{content}
images:
{images}
"""
