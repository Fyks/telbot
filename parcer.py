import random
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as BS


def get_page(domain):
    return urlopen(Request(domain, headers={
        'User-Agent': 'Mozilla/5.0'
    })).read()


def parse_page(domain):
    return BS(get_page(domain), 'lxml')


def getting_link(domain):
    a_list = []
    a = parse_page(domain)
    for links in a.find_all('a', class_='preview'):
        a_list.append(links.get('href'))
    return rand_link(a_list)


def rand_link(links):
    return links[random.randint(0, len(links) - 1)]


def getting_pic(domain):
    pic = parse_page(getting_link(domain)).find_all('img', id='wallpaper')
    for i in pic:
        return i.get('src')


def final_link(domain):
    return 'https:' + getting_pic(domain)
