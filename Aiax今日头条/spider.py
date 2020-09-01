import os
import random
import requests
# 请求异常时抛出
from requests.exceptions import RequestException
# 解析post请求的字段
from urllib.parse import urlencode
# 解析json数据
import json
# 抓取相关字段
from bs4 import BeautifulSoup
def ipDAi():
    import parsel

    for page in range(1, 8):
        print("#########正在爬取第{}页代理IP数据#########".format(page))
        proxies_list = []
        base_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(str(page))
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
        response = requests.get(url=base_url, headers=header)
        data = response.text
        html_data = parsel.Selector(data)
        parse_list = html_data.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
        for tr in parse_list:
            http_type = tr.xpath('./td[4]/text()').extract_first()
            i_num = tr.xpath('./td[1]/text()').extract_first()
            i_port = tr.xpath('./td[2]/text()').extract_first()
            proxies_dict = {}
            proxies_dict[http_type] = i_num + ":" + i_port
            print("保存成功", proxies_dict)
            proxies_list.append(proxies_dict)
    return proxies_list


IP = ipDAi()


def get_one_page(offset, keyword):
    data = {
        'aid': 24,
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'en_qc': 1,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis'}
    # 伪装浏览器
    headers = {
        'Host': 'www.toutiao.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Accept': 'application/json, text/javascript',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        'Referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        # cookie这一步非常重要   我们在请求的时候每隔一段时间他就会变 导致请求的json为空
        'Cookie': 'tt_webid=6798858588834121230; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6798858588834121230; csrftoken=e1c1bbef2bdddf1a0956eff79ee755b6; ttcid=3f03989a23704b6ba6aa4853b9441b8034; SLARDAR_WEB_ID=vn; s_v_web_id=verify_k79wbgce_rf3idn7y_ywfm_4IcX_ALlv_F0XgbpFgC3SQ; __tasessionId=l90c2qu3i1583119236978; tt_scid=eW9knXOj5CoW5cii.BsCILwbJyp-9cDwe1KtMbu8ZesZwkJN-mLAjeVaenKnnZnG73af',
        'TE': 'Trailers'
    }
    # urlcode解析data
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)
    try:
        response = requests.get(url, headers=headers, proxies=IP[random.randint(0, (len(IP) - 1))])
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        print('请求索引页出错')
        return None


def parse_html(html):  # 解析索引页
    data = json.loads(html)
    # 确定data字段存在
    if data and 'data' in data.keys():
        for item in data.get('data'):
            # 以字典的形式获取图片链接
            if item.get('article_url') == None:
                pass
            else:
                yield item.get('article_url')


# 判断图片链接是否有效
def get_XQ_page(url):
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchFrameException
        # 实例化browwser
        browweser = webdriver.Chrome()
        browweser.get(url)
        return browweser.page_source
    except TimeoutException as e:
        print(e)
        print('请求详情页超时', url)
        return None
    except NoSuchFrameException:
        return None
    except NoSuchElementException:
        return None
    finally:
        browweser.close()


# # # 解析图片连接
url_images = []


def parse_page_detail(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        items = soup.select('.imageList ul a')
        for item in items:
            url_images.append(item['href'])

    except:
        items = soup.select('article div img')
        for item in items:
            url_images.append(item['href'])


def main():
    keyword = str(input("#########请输入关键词:"))
    pages = int(input("#########请输入爬取的页数:"))
    for page in range(1, pages + 1):
        print('#########正在爬取第{}页#########'.format(page))
        offset = (page - 1) * 20
        html = get_one_page(offset, keyword)
        htmls = parse_html(html)
        for url in htmls:
            html = get_XQ_page(url)
            if html:
                parse_page_detail(html)


if __name__ == '__main__':
    print('#########爬取图片开始#########')
    main()
    i = 1
    path = 'D:/JRTT/images'
    if not os.path.exists(path):
        os.makedirs(path)
    for url in url_images:
        print("#########正在下载第{}张图片#########".format(i))
        image = requests.get(url)
        with open('{0}/{1}.jpg'.format(path,i), 'wb') as f:
            f.write(image.content)
            i = i + 1

    print('#########爬取图片结束#########')
