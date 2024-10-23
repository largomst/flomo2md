import argparse
import os
import uuid

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
    content = item['content'].strip().replace('\\', '')
    files = item['files']
    if files:
        images = '\nimages:\n' + ''.join([f'* ![]({x})\n' for x in files])
    else:
        images = ''

    md = create_md(time, content, images)
    return md


def create_md(time, content, images):
    return (
        f"""# {time}

{content}
"""
        + images
    )


def flomo2md(source):
    bs = BeautifulSoup(source, 'html.parser')
    result = []
    for memo in bs.find_all('div', class_='memo'):
        item = memo2md(memo)
        result.append(item)

    return result


def main():
    input, output = cli()

    with open(input, encoding='utf-8') as f:
        source = f.read()
        mds = flomo2md(source)
        for md in mds:
            title = uuid.uuid4().hex + '.md'
            md_path = os.path.join(output, title)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(md)


def cli():
    p = argparse.ArgumentParser()
    p.add_argument('input', type=str)
    p.add_argument('output', type=str)
    args = p.parse_args()
    input = args.input
    output = args.output
    return input, output


main()
