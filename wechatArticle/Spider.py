import random
from pyquery import PyQuery as pq
import execjs
import requests
import re
from requests.exceptions import ConnectionError
from urllib.parse import urlencode
import pymongo
from config import *

base_url = 'https://weixin.sogou.com/weixin?'
cilent = pymongo.MongoClient(MONGO_URL)
db = cilent[MONGO_DB]


def get_proxy():
    proxy_pool_url = 'http://127.0.0.1:5555/random'
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None


proxy = None
headers = {
    # 'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8',
    # 'Accept - Encoding': 'gzip, deflate, br',
    # 'Accept - Language': 'zh - CN, zh;q = 0.8',
    # 'Connection': 'keep - alive',
    'Cookie': 'SUID = 206068DF3220910A000000005F053E84;SUV = 1594179207597201;pgv_pvi = 4780042240;IPLOC = CN5204;ld = iZllllllll2K2DpVlllllVDTZYUlllllNb8jklllll9lllllRZlll5 @ @ @ @ @ @ @ @ @ @;LSTMV = 585 % 2C699;LCLKINT = 7735;ABTEST = 0 | 1597803892 | v1;SNUID = 16C8B9700603A837B06A582B06554D09;weixinIndexVisited = 1;JSESSIONID = aaa_uXjYEnbie7TzHIYox;ppinf = 5 | 1597811436 | 1599021036 | dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTYlQjElQTMlRTYlOUYlOTJ8Y3J0OjEwOjE1OTc4MTE0MzZ8cmVmbmljazoxODolRTYlQjElQTMlRTYlOUYlOTJ8dXNlcmlkOjQ0Om85dDJsdUJ6bWlvVG1uRFVfVXBoVUZTQnBnT3dAd2VpeGluLnNvaHUuY29tfA;pprdig = SCOzTAesmtmyKUph3UdLRsOe7D8TQWI8YY4OIkC6Yc5WRz954EpQcm8AqZRl4xgPzrPKgQyA4yp4pwLkIa6N995UUq1lR16u__Ilw78QTUu1szsKA2HC01TiB9GgwRKFK - z6SqvajzQAbla9vqWM5VheUG9zJrXM2tdTSm - cx38;sgid = 09 - 49490915 - AV88quwW9cZ3ialmW7ibuwFWM;ppmdig = 1597811437000000ce123449c8e6c148e9b384d08cd9c1c9;Hm_lvt_407473d433e871de861cf818aa1405a1 = 1597803901, 1597803993;Hm_lpvt_407473d433e871de861cf818aa1405a1 = 1597811497',
    'Host': 'weixin.sogou.com',
    'Upgrade - Insecure - Requests': '1',
    # 'Referer': 'https: // weixin.sogou.com / weixin?type = 2 & s_from = input & query = % E9 % A3 % 8E % E6 % 99 % AF & ie = utf8 & _sug_ = n & _sug_type_ =',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

count=0
def get_index(keyword, page):  # 初始页
    global proxy
    global count
    if count==5:
        print("失败重试过多")
        return None
    key = {
        'query': keyword,
        'type': '2',
        'page': page
    }
    url = base_url + urlencode(key)
    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            print(proxies)
            response = requests.get(url, headers=headers, allow_redirects=False, proxies=proxies)
            response.encoding = response.apparent_encoding
        else:
            response = requests.get(url, headers=headers, allow_redirects=False)
            response.encoding = response.apparent_encoding
        if response.status_code == 200:
            # print('True')
            return response.text
        if response.status_code == 302:
            print('302错误，需要代理')
            proxy = get_proxy()
            if proxy:
                print('get a new proxy', proxy)
                return get_index(keyword, page)
            else:
                print("get proxy was faild")
        # Need Proxy
    except ConnectionError:
        count=count+1
        return get_index(keyword, page)


def get_atricle_urls(html):  # 假地址
    partten = re.compile('<h3>.*?href="(.*?)" id.*?</h3>', re.S)
    results = re.findall(partten, html)
    for result in results:
        yield result


def url_decode(r):  # 解密地址
    url = 'https://weixin.sogou.com' + r
    b = random.randint(0, 99)
    a = url.index('url=')
    a = url[a + 30 + b:a + 31 + b:]
    url += '&k=' + str(b) + '&h=' + a
    return url


def get_urls_True(url):  # 真地址
    resp = requests.get(url, headers=headers)

    # print(resp.text)
    comment = re.compile('setTimeout.*?\) (.*?),100\);', re.DOTALL)
    js_code = re.findall(comment, resp.text)
    # print(js_code[0])
    js_code = js_code[0].replace('window.location.replace(url)', 'return url;')
    # print(js_code)
    # js_code={js_code}
    result = """function res() {}""".format(js_code)
    # print(result)
    ctx = execjs.compile(result)
    # print(ctx.call("res"))
    var_url = ctx.call("res")
    return var_url


def get_article_details(article):
    headers2 = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'pgv_pvi=517558272; RK=XH6F3EPTyy; qq_openid=25104E3BE00D8DB5E3F9DDA758E40369; qq_access_token=FA663CFA5045A3365F4FDECCDE23AC02; qq_client_id=101487368; pac_uid=3_25104E3BE00D8DB5E3F9DDA758E40369; xw_main_login=qq; pgv_pvid=3500539124; ptcz=4ceeca9dd90676743af9261424f2e19952137c9cb9f0d0f3acce734fd1a2a6fc; wxtokenkey=777; rewardsn=; Hm_lvt_407473d433e871de861cf818aa1405a1=1597844281,1597844383,1597844430,1597895054; Hm_lpvt_407473d433e871de861cf818aa1405a1=1597897214if-modified-since:Thu, 20 Aug 2020 12:14:04 +0800',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'
    }
    resp = requests.get(article, headers=headers2, proxies=proxy)
    resp.encoding = resp.apparent_encoding
    # print(resp.text)
    html = pq(resp.text)
    title = html('#activity-name')
    # print(titlt.text())
    txt = html('#js_content > section > section > section')
    return {
        'title': title.text(),
        'txt': txt.text()
    }


def save_mongodb(save_result):
    if db[MONGO_TABLE].insert_one(save_result):
        return True
    return False


def main():
    keyord = input("请输入文章关键词")
    pages = int(input("请输入爬取页数，最高100页。"))
    for page in range(1,pages + 1):
        html = get_index(keyord, str(page))
        print(html)
        urls = get_atricle_urls(html)
        for url in urls:
            url = url_decode(url)
            atticle_url = get_urls_True(url)
            result_svae = get_article_details(atticle_url)
            save_mongodb(result_svae)


if __name__ == '__main__':
    print("程序开始")
    main()
    print("程序结束")
