import random
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as BS


DOMAIN = 'https://alpha.wallhaven.cc/'


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


def link_modifier(source):
    key = source.replace('\\', '')
    random_page = str(random.randint(1, 5))
    link = '{0}search?q={1}&page={2}'.format(DOMAIN, key, random_page)
    return link


def picture(domain):
    return 'https:' + getting_pic(domain)
