import requests
import parsel
proxies_list = []
for page in range(1,8):
    print("============正在爬取第{}数据===========".format(page))

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
        print("保存成功", proxies_dict)
        proxies_list.append(proxies_dict)
print(proxies_list[0].get(0))