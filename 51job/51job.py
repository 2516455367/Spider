import os
import random
import time
import pandas as pd
from pyquery import PyQuery as pq
import requests
from urllib.parse import urlencode
e=0
z=0
kewords=[]
workName = []
companyName = []
workAreaType = []
workMoney = []
workJieSao = {}
workLeiBie = {}
start = time.time()
################################################################
from bs4 import BeautifulSoup
################################################################
profession = str(input("请输入职位关键词/列如python或者Java等"))
pages=int(input("请输入爬取页数："))
filename=str(input('请输入文件名'))
################################################################
print("============正在获取代理IP...===========")
################################################################
def ipDAi():
    import parsel

    for page in range(1, 8):
        # print("============正在爬取第{}数据===========".format(page))
        proxies_list = []
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
    return proxies_list
print("============恭喜您代理IP获取成功...===========")
################################################################
IP = ipDAi()
################################################################
def get_one_pages(workyear, cotype, degreefrom, jobterm, companysize,release_date,monthly_pay):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}
    data = {
        'lang': 'c',
        'postchannel': '0000',
        'workyear': workyear,
        'cotype': cotype,
        'degreefrom': degreefrom,
        'jobterm': jobterm,
        'companysize':  companysize,
        'ord_field': '0',
        'dibiaoid': '0',
    }
    for page in range(1,pages+1):
        url = 'https://search.51job.com/list/000000,000000,0000,00,{},{},{},2,{}.html?'.format(release_date,monthly_pay,profession,str(page)) + urlencode(
            data)
        yield url

################################################################
def inputname():
    print('工作年限: A=在校生/应届生  B=1-3年   C=3-5年   D=5-10年    E=10年以上   F=无需经验  G=所有')
    workyear = str(input("请输入选项"))
    if workyear == 'A':
        workyear = '01'
    elif workyear == 'B':
        workyear = '02'
    elif workyear == 'C':
        workyear = '03'
    elif workyear == 'D':
        workyear = '04'
    elif workyear == 'E':
        workyear = '05'
    elif workyear == 'F':
        workyear = '06'
    else:
        workyear = '99'
    kewords.append(workyear)
    print('公司性质:   A=国企    B=外资(欧美)    C=外资(非欧美)   D=上市公司    E=合资   F=民营公司  G=外企代表处   H=政府机关   I=事业单位    J=非营利组织    K=创业公司 L=所有 ')
    cottype = str(input("请输入选项"))
    if cottype == 'A':
        cottype = '04'
    elif cottype == 'B':
        cottype = '01'
    elif cottype == 'C':
        cottype = '02'
    elif cottype == 'D':
        cottype = '10'
    elif cottype == 'E':
        cottype = '03'
    elif cottype == 'F':
        cottype = '05'
    elif cottype == 'G':
        cottype = '06'
    elif cottype == 'H':
        cottype = '07'
    elif cottype == 'I':
        cottype = '08'
    elif cottype == 'J':
        cottype = '09'
    elif cottype == 'K':
        cottype = '11'
    else:
        cottype = '99'
    kewords.append(cottype)
    print('学历要求： A=初中及以下  B=高中/中技/中专   C=大专  D=本科   E=硕士   F=博士   G=无学历要求 H=所有')
    degreefrom=str(input('"请输入选项"'))
    if degreefrom=="A":
        degreefrom='01'
    elif degreefrom=='B':
        degreefrom='02'
    elif degreefrom == 'C':
        degreefrom = '03'
    elif degreefrom == 'D':
        degreefrom = '04'
    elif degreefrom == 'E':
        degreefrom = '05'
    elif degreefrom == 'F':
        degreefrom = '06'
    elif degreefrom=='G':
        degreefrom='07'
    else:
        degreefrom='99'
    kewords.append(degreefrom)
    print('工作类型： A=全职 B=兼职 C=实习 D=全职 E=实习兼职 F=所有 ')
    jobterm=str(input('请输入选项'))
    if jobterm=='A':
        jobterm='01'
    elif jobterm=='B':
        jobterm='02'
    elif jobterm=='C':
        jobterm='03'
    elif jobterm=='D':
        jobterm='04'
    elif jobterm=='E':
        jobterm='05'
    else:
        jobterm='99'
    kewords.append(jobterm)
    print('公司规模：A=少于50人   B=50-150人  C=150-500人  D=500-1000人  E=1000-5000人  F=5000-10000人  G=10000人以上 H=所有 ')
    companysize=str(input('请输入选项'))
    if companysize=='A':
        companysize='01'
    elif companysize=='B':
        companysize='02'
    elif companysize == 'C':
        companysize = '03'
    elif companysize=='D':
        companysize='04'
    elif companysize=='E':
        companysize='05'
    elif companysize=='F':
        companysize='06'
    elif companysize=='G':
        companysize='07'
    else:
        companysize='99'
    kewords.append(companysize)
    print('发布日期：A=24小时内   B=近三天   C=近一周  D=近一月  D=其他  F=所有 ')
    release_date=str(input("请输入选项"))
    if release_date=='A':
        release_date='0'
    elif release_date=="B":
        release_date="1"
    elif release_date == "B":
        release_date = "2"
    elif release_date == "B":
        release_date = "3"
    elif release_date == "B":
        release_date = "4"
    else:
        release_date='9'
    kewords.append(release_date)
    print("月薪范围： A=2千以下   B=2-3千  C=3-4.5千   D=4.5-6千   D=6-8千  F=0.8-1万   G=1-1.5万   H=1.5-2万   I=2-3万  J=3-4万  K=4-5万  L=5万以上  M=所有 ")
    monthly_pay=str(input("请输入选项"))
    if monthly_pay=="A":
        monthly_pay='01'
    elif monthly_pay=="B":
        monthly_pay='02'
    elif monthly_pay=="C":
        monthly_pay='03'
    elif monthly_pay=="D":
        monthly_pay='04'
    elif monthly_pay=="E":
        monthly_pay='05'
    elif monthly_pay=="F":
        monthly_pay='06'
    elif monthly_pay=="G":
        monthly_pay='07'
    elif monthly_pay == "F":
        monthly_pay = '08'
    elif monthly_pay == "I":
        monthly_pay = '09'
    elif monthly_pay == "J":
        monthly_pay = '10'
    elif monthly_pay == "K":
        monthly_pay = '11'
    elif monthly_pay == "L":
        monthly_pay = '12'
    else:
        monthly_pay = '99'
    kewords.append(monthly_pay)
################################################################
def pares_html(url):
    global e, z
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}
    response = requests.get(url, headers=headers, proxies=IP[random.randint(0, (len(IP) - 1))])
    response.encoding = "gbk"
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            ################################################################
            ul = soup.select('.dw_table .el .t1 span a')
            for el in ul:
                html = pq(url=el['href'], headers=headers, proxies=IP[random.randint(0, (len(IP) - 1))], encoding="gbk")
                # 爬取职业名称
                for txt0 in html('.tCompanyPage .tCompany_center.clearfix .tHeader.tHjob h1').items():
                    workName.append(txt0.text())
                # 爬取公司名称
                for txt1 in html(
                        '.tCompanyPage .tCompany_center.clearfix .tHeader.tHjob .cname a:first-child').items():
                    companyName.append(txt1.text())
                # 爬取工作地点
                for txt2 in html('.tCompanyPage .tCompany_center.clearfix .tHeader.tHjob .msg.ltype').items():
                    workAreaType.append(txt2.text())
                # 爬取薪资额度
                for txt3 in html('.tCompanyPage .tCompany_center.clearfix .tHeader.tHjob strong').items():
                    workMoney.append(txt3.text())
                # 爬取职业需求
                for txt4 in html('.tBorderTop_box .bmsg.job_msg.inbox').items():
                    m = txt4.text()
                    workJieSao[e] = ''.join(list(map(lambda x: x.strip('\n'), m)))
                    e = e + 1
                # 爬取职业类别
                for txt5 in html('.bmsg.job_msg.inbox .mt10').items():
                    n = txt5.text()
                    workLeiBie[z] = ''.join(list(map(lambda y: y.strip('\n'), n)))
                    z = z + 1
        else:
            return None
    except requests.HTTPError:
        print("网页出错")
################################################################
def write_datas():
    print("###########正在讲数据写入本地...###########")
    lst1 = list(workJieSao.values())
    lst2 = list(workLeiBie.values())
    df = pd.DataFrame(
        {'职位名': workName, '公司名': companyName, '工作基本需求': workAreaType, '薪资': workMoney, '职业需求': lst1, '职业类别': lst2})
    print(df)

    df.to_excel("{}/{}.xlsx".format(os.getcwd(),filename),encoding='utf-8',index=False)
    print("###########数据写入完成...###########")
    end = time.time()
    print('###########您总共花费{}s##########'.format(end - start))
################################################################
def main():
    inputname()
    print("###########查询中...###########")
    urls=get_one_pages(kewords[0],kewords[1],kewords[2],kewords[3],kewords[4],kewords[5],kewords[6])
    print("###########爬取中...###########")
    for url in urls:
        pares_html(url)
    write_datas()
    print("###########数据获取完毕...###########")
if __name__ == '__main__':
    main()
    print("###########程序结束...###########")
