# Source: https://ingress.fandom.com/wiki/Glyphs
# Author：KevinNiu
# Date：2020-02-16
# Igress Glyphs

import json
import requests

def donwload_img(url):
    name = url[url.rfind('/') + 1:]
    r = requests.get(url)
    with open(f'imgs/{name}', 'wb') as f:
        f.write(r.content)

def big_img_url(item):
    # https://static.wikia.nocookie.net/ingress/images/7/7f/More_Glyph.png/revision/latest/scale-to-width-down/50?cb=20210307185120
    img_url = item['img']
    img_url = img_url[:img_url.find('.png') + 4]
    item['img'] = img_url
    item['local_img'] = img_url[img_url.rfind('/') + 1:]
    return item

def main():
    print("Hello World!")
    with open('graphics.json', 'r') as f:
        data = json.load(f)
        data = [big_img_url(x) for x in data]
        # for x in data:
        #     donwload_img(x['img'])
        results = [f'<img src="{x["img"]}"/>,{x["text"]}' for x in data]
        lines = '\n'.join(results)
        with open ('result.txt', 'w') as f:
            f.write(lines)
        print(lines)


if __name__ == "__main__":
    main()
