import re

import execjs
import requests
import random
from pyquery import PyQuery as pq

headers = {
    'Cookie': 'SUID = 206068DF3220910A000000005F053E84;SUV = 1594179207597201;pgv_pvi = 4780042240;IPLOC = CN5204;ld = iZllllllll2K2DpVlllllVDTZYUlllllNb8jklllll9lllllRZlll5 @ @ @ @ @ @ @ @ @ @;LSTMV = 585 % 2C699;LCLKINT = 7735;ABTEST = 0 | 1597803892 | v1;SNUID = 16C8B9700603A837B06A582B06554D09;weixinIndexVisited = 1;JSESSIONID = aaa_uXjYEnbie7TzHIYox;ppinf = 5 | 1597811436 | 1599021036 | dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTYlQjElQTMlRTYlOUYlOTJ8Y3J0OjEwOjE1OTc4MTE0MzZ8cmVmbmljazoxODolRTYlQjElQTMlRTYlOUYlOTJ8dXNlcmlkOjQ0Om85dDJsdUJ6bWlvVG1uRFVfVXBoVUZTQnBnT3dAd2VpeGluLnNvaHUuY29tfA;pprdig = SCOzTAesmtmyKUph3UdLRsOe7D8TQWI8YY4OIkC6Yc5WRz954EpQcm8AqZRl4xgPzrPKgQyA4yp4pwLkIa6N995UUq1lR16u__Ilw78QTUu1szsKA2HC01TiB9GgwRKFK - z6SqvajzQAbla9vqWM5VheUG9zJrXM2tdTSm - cx38;sgid = 09 - 49490915 - AV88quwW9cZ3ialmW7ibuwFWM;ppmdig = 1597811437000000ce123449c8e6c148e9b384d08cd9c1c9;Hm_lvt_407473d433e871de861cf818aa1405a1 = 1597803901, 1597803993;Hm_lpvt_407473d433e871de861cf818aa1405a1 = 1597811497',
    'Host': 'weixin.sogou.com',
    'Upgrade - Insecure - Requests': '1',
    # 'Referer': 'https: // weixin.sogou.com / weixin?query = % E9 % A3 % 8E % E6 % 99 % AF & _sug_type_ = & s_from = input & _sug_ = n & type = 2 & page = {} & ie = utf8'.format(str(random.randint(1,7))),
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

# 这个r是从href属性中随便找的一个
r = '/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgSxTyVa2uGOsvp7LE4sJUgal8mhyEzluWfVqXa8Fplpd98Xr6r4DIa19rLf2kyvPJShW34jCyHMHbgq1L5Oje75oMAgHskOsnwzsuM3Xlyj0LfrQHwiqieeTN4wkZa7Hjmr5qQkHDLdgNDmT_VxdtMR1ABKfA-u0XWduIlALL0O-h4-BHO_5wA8QG2FD0oJYUROLMmszmrDU7vpPfaP_x_QgtPujwwRB2Pw..&amp;type=2&amp;query=%E9%A3%8E%E6%99%AF&amp;token=8D36432016C8B9700603A837B06A582B06554D095F3DF4A1'


def url_decode(r):
    url = 'https://weixin.sogou.com' + r
    b = random.randint(0, 99)
    a = url.index('url=')
    a = url[a + 30 + b:a + 31 + b:]
    url += '&k=' + str(b) + '&h=' + a
    return url


url = url_decode(r)

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
headers2 = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': 'pgv_pvi=517558272; RK=XH6F3EPTyy; qq_openid=25104E3BE00D8DB5E3F9DDA758E40369; qq_access_token=FA663CFA5045A3365F4FDECCDE23AC02; qq_client_id=101487368; pac_uid=3_25104E3BE00D8DB5E3F9DDA758E40369; xw_main_login=qq; pgv_pvid=3500539124; ptcz=4ceeca9dd90676743af9261424f2e19952137c9cb9f0d0f3acce734fd1a2a6fc; wxtokenkey=777; rewardsn=; Hm_lvt_407473d433e871de861cf818aa1405a1=1597844281,1597844383,1597844430,1597895054; Hm_lpvt_407473d433e871de861cf818aa1405a1=1597897214if-modified-since:Thu, 20 Aug 2020 12:14:04 +0800',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'
}
resp = requests.get(ctx.call("res"), headers=headers2)
resp.encoding = resp.apparent_encoding
print(resp.text)
html=pq(resp.text)
titlt=html('#activity-name')
txt=html('#js_content > section > section > section')
print(titlt.text())
print(txt.text())