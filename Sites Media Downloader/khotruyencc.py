import requests
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs

def onechapter(web, output_dir):
    makedirs(output_dir, exist_ok=True)
    res = requests.get(web)
    html_content = res.text
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    image_links = [img['data-src'] for img in img_tags]
    for i, link in enumerate(image_links):
        image_save_path = join(output_dir, f'image_{i}.jpg')
        res = requests.get(link)
        with open(image_save_path, 'wb') as f:
            f.write(res.content)

def multichapters(link, dir, latest_chapter, *special_chapters):
    listchaps = []
    for c in range(1,latest_chapter+1):
        chapterlink = f'{link}chapter-{c}'
        listchaps.append(chapterlink)
        for x in special_chapters:
            c = c + x
            specialchapterlink = f'{link}chapter-{c}'
            c = c - x
            listchaps.append(specialchapterlink)
    for x in listchaps:
        onechapter(x, dir)
            