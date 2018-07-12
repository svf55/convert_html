#!/usr/bin/env python
"""
Convert html file to json.
"""


import argparse
import json
from bs4 import BeautifulSoup


def convert_json(f):
    with open(f, 'rb') as file:
        soup = BeautifulSoup(file, 'html.parser')

    texts = soup.find_all()
    content = []
    for t in texts:
        if t.name == 'img':
            data_item = {
                'type': 'img',
                'href': t['src'],
                'size': {
                    'width': t['width'],
                    'height': t['height']
                }
            }
        elif t.name == 'a':
            data_item = {
                'type': 'link',
                'value': t.get_text(),
                'link': t['href'],
            }
        else:
            data_item = {
                'type': 'text',
                'value': t.get_text()
            }
        content.append(data_item)

    return json.dumps({
        'content': content
    }, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='input file')
    parser.add_argument('file', help='HTML file')
    args = parser.parse_args()
    print(convert_json(args.file))

