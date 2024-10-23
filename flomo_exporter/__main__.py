import markdownify
from bs4 import BeautifulSoup


def flomo2json(source):
    bs = BeautifulSoup(source, 'html.parser')
    result = []
    for memo in bs.find_all('div', class_='memo'):
        item = memo2json(memo)
        result.append(item)

    return result


def memo2json(memo):
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

    return item
