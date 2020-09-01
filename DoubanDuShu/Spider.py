import re
from pprint import pprint
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json
from config import *
import pymongo
from requests.exceptions import ConnectionError

cilent = pymongo.MongoClient(MONGO_URL)
db = cilent[MONGO_DB]


def get_header_html_tags():
    headers = {
        'Cookie': 'bid=-fxf7eTuH2I; ap_v=0,6.0; __utma=30149280.2115844837.1597976256.1597976256.1597976256.1; __utmc=30149280; __utmz=30149280.1597976256.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=bd52c241319af1e9-227e8d7e16c30059:T=1597976257:RT=1597976257:S=ALNI_Mat5h95EEc79RbFtawXfOrBhw-d0A; _pk_ref.100001.a7dd=%5B%22%22%2C%22%22%2C1597982974%2C%22https%3A%2F%2Fbook.douban.com%2Ftag%2F%25E7%25A7%2591%25E5%25B9%25BB%22%5D; _pk_ses.100001.a7dd=*; _ga=GA1.3.2115844837.1597976256; _gid=GA1.3.1697045329.1597982975; _gat=1; _pk_id.100001.a7dd=129c1bfdd2493878.1597982974.1.1597982998.1597982974.; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1597982983,1597982996,1597983004; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1597983004',
        'Host': 'read.douban.com',
        'Referer': 'https://book.douban.com/subject/6781808/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'
    }
    data = {
        'dcs': 'book - nav',
        'dcm': 'douban'
    }
    base_url = 'https://read.douban.com/ebooks/?'
    url = base_url + urlencode(data)
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    if response.status_code == 200:
        html = BeautifulSoup(response.text, 'lxml')
        text = html.select('.bd .list.kinds-list.tab-panel li')
        for tags in text:
            for tag in tags.select('li a'):
                yield [tag['href'], tag.get_text()]
    return None


def get_index_html(keyword, page):
    headers = {
        'Content - Type': 'application / json',
        'Cookie': 'bid = -fxf7eTuH2I;__utma = 30149280.2115844837.1597976256.1597976256.1597976256.1;__utmc = 30149280;__utmz = 30149280.1597976256.1.1.utmcsr = (direct) | utmccn = (direct) | utmcmd = (none);__gads = ID = bd52c241319af1e9 - 227e8d7e16c30059: T = 1597976257:RT = 1597976257:S = ALNI_Mat5h95EEc79RbFtawXfOrBhw - d0A;_ga = GA1.3.2115844837.1597976256;_gid = GA1.3.1697045329.1597982975;_pk_ref.100001.a7dd = % 5B % 22 % 22 % 2C % 22 % 22 % 2C1597988601 % 2C % 22https % 3A % 2F % 2Fbook.douban.com % 2Ftag % 2F % 25E7 % 25A7 % 2591 % 25E5 % 25B9 % 25BB % 22 % 5D;_pk_ses.100001.a7dd = *;Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c = 1597983004, 1597983015, 1597988715, 1597988729;_gat = 1;Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c = 1597989029;_pk_id.100001.a7dd = 129c1bfdd2493878.1597982974.3.1597989042.1597985484.',
        'Host': 'read.douban.com',
        'Origin': 'https: // read.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }
    jdata = {"sort": "rating", "page": page, "kind": keyword,
             "query": "\n    query getFilterWorksList($works_ids: [ID!]) {\n      worksList(worksIds: $works_ids) {\n        \n    \n    title\n    cover\n    url\n    isBundle\n    coverLabel\n  \n    \n    url\n    title\n  \n    \n    author {\n      name\n      url\n    }\n    origAuthor {\n      name\n      url\n    }\n    translator {\n      name\n      url\n    }\n  \n    \n    abstract\n    editorHighlight\n  \n    \n    isOrigin\n    kinds {\n      \n    name @skip(if: true)\n    shortName @include(if: true)\n    id\n  \n    }\n    ... on WorksBase @include(if: true) {\n      wordCount\n      wordCountUnit\n    }\n    ... on WorksBase @include(if: true) {\n      \n    isEssay\n    \n    ... on EssayWorks {\n      favorCount\n    }\n  \n    \n    isNew\n    \n    averageRating\n    ratingCount\n    url\n  \n  \n  \n    }\n    ... on WorksBase @include(if: false) {\n      isColumn\n      isEssay\n      onSaleTime\n      ... on ColumnWorks {\n        updateTime\n      }\n    }\n    ... on WorksBase @include(if: true) {\n      isColumn\n      ... on ColumnWorks {\n        isFinished\n      }\n    }\n    ... on EssayWorks {\n      essayActivityData {\n        \n    title\n    uri\n    tag {\n      name\n      color\n      background\n      icon2x\n      icon3x\n      iconSize {\n        height\n      }\n      iconPosition {\n        x y\n      }\n    }\n  \n      }\n    }\n    highlightTags {\n      name\n    }\n  \n    isInLibrary\n    ... on WorksBase @include(if: false) {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on EbookWorks {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on WorksBase @include(if: true) {\n      ... on EbookWorks {\n        id\n        isPurchased\n        isInWishlist\n      }\n    }\n  \n        id\n        isOrigin\n      }\n    }\n  ",
             "variables": {}}
    base_url = 'https://read.douban.com/j/kind/'
    try:
        response = requests.post(base_url, json=jdata, headers=headers, allow_redirects=True)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        else:
            print("请求失败", response.status_code)
    except ConnectionError:
        print("连接请求失败")
        return None


def get_book_url(html):
    url = 'https://read.douban.com'
    data = json.loads(html)
    # pprint(data)
    for i in range(20):
        yield {
            'title': data['list'][i]['title'],
            'cover': data['list'][i]['cover'],
            'author': data['list'][i]['origAuthor'],
            'url_daata': url + data['list'][i]['url'],
            'ratingCount': data['list'][i]['ratingCount'],
        }
        # print(data['list'][i]['cover'])
        # print(data['list'][i]['title'])
        # print(data['list'][i]['origAuthor'])
        # print(url+data['list'][i]['url'])


def save_mongodb(save_result):
    if db[MONGO_TABLE].insert_one(save_result):
        return True
    return False


tags_list = []


def main():
    print('################ tags编号 ################')
    html1 = get_header_html_tags()
    for i in html1:
        content = re.sub('/kind/', ' ', i[0])
        tags_list.append(content)
        print(content, i[1])
    x = input('选择性采集请输入  1\n非选择性采集请输入  0\nINPUT:')
    if x == '1':
        keyword = input("请输入tag代号,如上:   ")
        pages = input("请输入采集页数:    ")
        for page in range(1, int(pages) + 1):
            html = get_index_html(keyword, page)
            book_url = get_book_url(html)
            for url in book_url:
                print(url)
                save_mongodb(url)
    elif x == '0':
        pages = input("请输入采集页数:    ")
        for word in tags_list:
            for page in range(1, int(pages) + 1):
                html = get_index_html(word, page)
                book_url = get_book_url(html)
                for url in book_url:
                    print(url)
                    save_mongodb(url)


if __name__ == '__main__':
    print("程序开始")
    main()
    print("程序结束")
