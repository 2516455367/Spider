# 获取目标网页
import os
import random
from multiprocessing import Pool
start_url = 'https://www.vmgirls.com/wp-admin/admin-ajax.php'
import requests
import parsel
import re
proxies_list = []
for page in range(1, 8):
    # print("============正在爬取第{}数据===========".format(page))

    base_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(str(page))
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}
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
        # print("保存成功", proxies_dict)
        proxies_list.append(proxies_dict)


def get_one_page(url,page):
    data = {
        'append': 'list - home',
        'paged': page,
        'action': 'ajax_load_posts',
        'query': '',
        'page': 'home'
    }
    headers = {
        'accept': 'text / html, * / *; q = 0.01',
        'accept - encoding': 'gzip, deflate, br',
        'accept - language': 'zh - CN, zh;q = 0.9',
        'content - length': '64',
        'content - type': 'application / x - www - form - urlencoded;charset = UTF - 8',
        'origin': 'https:// www.vmgirls.com',
        'referer': 'https: // www.vmgirls.com /',
        'cookie': '_ga = GA1.2.1170434813.1593873236;__gads = ID = 18cfd885c920dac7: T = 1593873236:S = ALNI_MZI5PxxkpdserNg1NH7WOWAhxmT4w;Hm_lvt_a5eba7a40c339f057e1c5b5ac4ab4cc9 = 1593873237, 1594093300, 1594788951;_gid = GA1.2.85305203.1594788951;Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c = 1593873243, 1594788956;_GPSLSC =;Hm_lpvt_a5eba7a40c339f057e1c5b5ac4ab4cc9 = 1594804717;Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c = 1594804723',
        'sec - fetch - dest': 'empty',
        'sec - fetch - mode': 'cors',
        'sec - fetch - site': 'same - origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36',
        'x - requested -with': 'XMLHttpRequest'
    }
    response = requests.post(url=url, data=data, headers=headers,
                             proxies=proxies_list[random.randint(0, len(proxies_list) - 1)])
    if response.status_code == 200:
        return response.text
    return False


url_list = []


def parse_html(html):
    partten = re.compile('<a.*?content" href="(.*?)" title=.*?style.*?</a>', re.S)
    results = re.findall(partten, html)
    for result in results:
        url_list.append(result)
    return url_list


def praser_imahes_url(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        # print(response.status_code)
        if response.status_code == 200:
            html_image=parsel.Selector(response.text)
            title=html_image.xpath('//div[@class="nc-light-gallery"]/p[1]/text()').extract()
            images=html_image.xpath('//div[@class="nc-light-gallery"]/p[2]/a/@href').extract()
            save_images(title[len(title)-1],images)

        else:
            print("请求失败")
    except:
        return None

def save_images(name,result):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'
    }
    i=1
    print("#########正在下载{}影集#########".format(name))
    path='{}/images/{}'.format(os.getcwd(),name)
    if not os.path.exists(path):
        os.makedirs(path)
    for img in result:
        re = requests.get(img, headers=headers)
        with open('{}/{}.jpeg'.format(path, i), "wb") as f:
            print("#########正在下载第{}张图片#########".format(i))
            f.write(re.content)
            i=i+1


def main(key_page):
    html = get_one_page(start_url,key_page)
    parse_html(html)
    for url in url_list:
        praser_imahes_url(url)


if __name__ == '__main__':
    key=int(input("请输入需要爬取的页数"))
    pool=Pool()
    pool.map(main,[i for i in range(1,key+1)])
    print("恭喜爬取完成")
