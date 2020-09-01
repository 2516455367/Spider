import os
import tkinter as tk

from PIL import Image ,ImageTk

workyear = ['在校生/应届生', '1-3年 ', '3-5年 ', '5-10年 ', '10年以上 ', '无需经验 ', '所有']
workyearvalue=['01','02','03','04','05','06','99']
cottype = ['国企 ', '外资(欧美)', ' 外资(非欧美)', '上市公司  ', '合资', '民营公司', '外企代表处', ' 政府机关', '事业单位', '非营利组织', '创业公司 ','所有']
cottypevalue=['04','01','02','10','03','05','06','07','08','09','11','99']
degreefrom=['初中及以下', ' 高中/中技/中专',   '大专',  '本科',   '硕士',  ' 博士 ', ' 无学历要求',' 所有']
degreefromvalue=['01','02','03','04','05','06','07','99']
jobterm=['全职 ','兼职 ','实习','全职',' 实习兼职', '所有' ]
jobtermvalue=['01','02','03','04','05','99']
companysize=['少于50人',   '50-150人',  '150-500人',  '500-1000人',  '1000-5000人',  '5000-10000人',  '10000人以上',' 所有']
companysizevalue=['01','02','03','04','05','06','07','99']
release_date=['24小时内' , ' 近三天 ', ' 近一周',  '近一月',  '其他',  '所有']
release_dateValue=['0','1','2','3','4','9']
monthly_pay=['2千以下',   '2-3千',  '3-4.5千',   '4.5-6千',   '6-8千',  '0.8-1万',   '1-1.5万',   '1.5-2万',   '2-3万',  '3-4万',  '4-5万',  '5万以上',  '所有']
monthly_payValue=['01','02','03','04','05','06','07','08','09','10','11','12','99']
e,z=0,0
root = tk.Tk()
root.title("51job爬取实战")
root.geometry('1400x400')  # 设置宽度长度
cv= tk.Canvas(root, width = 600, height =500, bg ="white")
cv.pack()
a = os.path.abspath('1.jpg')
image = Image.open(a)
im = ImageTk.PhotoImage(image)
cv.create_image(270,190,image = im)

l1 = tk.Label(root, text="工作年限", font=("Arial", 10),fg='red')
l1.grid(row=1 ,column=1)
l2=tk.Label(root,text="公司性质",font=("Arial", 10),fg='red')
l2.grid(row=2 ,column=1)
l3=tk.Label(root,text="学历要求",font=("Arial", 10),fg='red')
l3.grid(row=3 ,column=1)
l4=tk.Label(root,text="工作类型",font=("Arial", 10),fg='red')
l4.grid(row=4 ,column=1)
l5=tk.Label(root,text='公司规模',font=("Arial", 10),fg='red')
l5.grid(row=5,column=1)
l6=tk.Label(root,text='发布日期',font=("Arial", 10),fg='red')
l6.grid(row=6,column=1)
l7=tk.Label(root,text='月薪范围',font=("Arial", 10),fg='red')
l7.grid(row=7,column=1)
profession_t=tk.Label(root,text='查询关键词',font=("Arial", 10),fg='red')
profession_t.grid(row=8,column=1)
profession = tk.Entry(root, text="", width=30,fg='green')
profession.grid(row=8, column=2)
pages_t=tk.Label(root,text='爬取的页数',font=("Arial", 10),fg='red')
pages_t.grid(row=9, column=1)
pages = tk.Entry(root, text="", width=30,fg='green')
pages.grid(row=9, column=2)
filename_t=tk.Label(root,text='输入文件名',font=("Arial", 10),fg='red')
filename_t.grid(row=10, column=1)
filename = tk.Entry(root, text="", width=30,fg='green')
filename.grid(row=10, column=2)
Beizu1=tk.Label(root,text='所有',font=("Arial", 40),fg='red')
Beizu1.grid(row=11,column=5)
Beizu2=tk.Label(root,text='选项',font=("Arial", 40),fg='red')
Beizu2.grid(row=11,column=6)
Beizu3=tk.Label(root,text='均为',font=("Arial", 40),fg='red')
Beizu3.grid(row=11,column=7)
Beizu4=tk.Label(root,text='单选',font=("Arial", 40),fg='red')
Beizu4.grid(row=11,column=8)
Author=tk.Label(root,text='作者：小柒哥哥\n'
                          'QQ:2516455367',font=("Arial", 10),fg='red')
Author.grid(row=12,column=2)
#单选框 工作年限
var_workyear = tk.StringVar()
var_workyear1 = tk.Radiobutton(root, text=workyear[0], variable=var_workyear, value=workyearvalue[0],fg='green')
var_workyear1.grid(row=1, column=2)
var_workyear2 = tk.Radiobutton(root, text=workyear[1], variable=var_workyear, value=workyearvalue[1],fg='green')
var_workyear2.grid(row=1, column=3)
var_workyear3 = tk.Radiobutton(root, text=workyear[2], variable=var_workyear, value=workyearvalue[2],fg='green')
var_workyear3.grid(row=1, column=4)
var_workyear4 = tk.Radiobutton(root, text=workyear[3], variable=var_workyear, value=workyearvalue[3],fg='green')
var_workyear4.grid(row=1, column=5)
var_workyear5 = tk.Radiobutton(root, text=workyear[4], variable=var_workyear, value=workyearvalue[4],fg='green')
var_workyear5.grid(row=1, column=6)
var_workyear6 = tk.Radiobutton(root, text=workyear[5], variable=var_workyear, value=workyearvalue[5],fg='green')
var_workyear6.grid(row=1, column=7)
var_workyear7 = tk.Radiobutton(root, text=workyear[6], variable=var_workyear, value=workyearvalue[6],fg='green')
var_workyear7.grid(row=1, column=8)
#单选框  公司性质
var_cottype = tk.StringVar()
var_cottype1 = tk.Radiobutton(root, text=cottype[0], variable=var_cottype, value=cottypevalue[0],fg='green')
var_cottype1.grid(row=2, column=2)
var_cottype2 = tk.Radiobutton(root, text=cottype[1], variable=var_cottype, value=cottypevalue[1],fg='green')
var_cottype2.grid(row=2, column=3)
var_cottype3 = tk.Radiobutton(root, text=cottype[2], variable=var_cottype, value=cottypevalue[2],fg='green')
var_cottype3.grid(row=2, column=4)
var_cottype4 = tk.Radiobutton(root, text=cottype[3], variable=var_cottype, value=cottypevalue[3],fg='green')
var_cottype4.grid(row=2, column=5)
var_cottype5 = tk.Radiobutton(root, text=cottype[4], variable=var_cottype, value=cottypevalue[4],fg='green')
var_cottype5.grid(row=2, column=6)
var_cottype6 = tk.Radiobutton(root, text=cottype[5], variable=var_cottype, value=cottypevalue[5],fg='green')
var_cottype6.grid(row=2, column=7)
var_cottype7 = tk.Radiobutton(root, text=cottype[6], variable=var_cottype, value=cottypevalue[6],fg='green')
var_cottype7.grid(row=2, column=8)
var_cottype8 = tk.Radiobutton(root, text=cottype[7], variable=var_cottype, value=cottypevalue[7],fg='green')
var_cottype8.grid(row=2, column=9)
var_cottype9 = tk.Radiobutton(root, text=cottype[8], variable=var_cottype, value=cottypevalue[8],fg='green')
var_cottype9.grid(row=2, column=10)
var_cottype_x = tk.Radiobutton(root, text=cottype[9], variable=var_cottype, value=cottypevalue[9],fg='green')
var_cottype_x.grid(row=2, column=11)
var_cottype_y = tk.Radiobutton(root, text=cottype[10], variable=var_cottype, value=cottypevalue[10],fg='green')
var_cottype_y.grid(row=2, column=12)
var_cottype_z = tk.Radiobutton(root, text=cottype[11], variable=var_cottype, value=cottypevalue[11],fg='green')
var_cottype_z.grid(row=2, column=13)
#单选框 学历要求
var_degreefrom = tk.StringVar()
var_degreefrom1 = tk.Radiobutton(root, text=degreefrom[0], variable=var_degreefrom, value=degreefromvalue[0],fg='green')
var_degreefrom1.grid(row=3, column=2)
var_degreefrom2 = tk.Radiobutton(root, text=degreefrom[1], variable=var_degreefrom, value=degreefromvalue[1],fg='green')
var_degreefrom2.grid(row=3, column=3)
var_degreefrom3 = tk.Radiobutton(root, text=degreefrom[2], variable=var_degreefrom, value=degreefromvalue[2],fg='green')
var_degreefrom3.grid(row=3, column=4)
var_degreefrom4 = tk.Radiobutton(root, text=degreefrom[3], variable=var_degreefrom, value=degreefromvalue[3],fg='green')
var_degreefrom4.grid(row=3, column=5)
var_degreefrom5 = tk.Radiobutton(root, text=degreefrom[4], variable=var_degreefrom, value=degreefromvalue[4],fg='green')
var_degreefrom5.grid(row=3, column=6)
var_degreefrom6 = tk.Radiobutton(root, text=degreefrom[5], variable=var_degreefrom, value=degreefromvalue[5],fg='green')
var_degreefrom6.grid(row=3, column=7)
var_degreefrom7 = tk.Radiobutton(root, text=degreefrom[6], variable=var_degreefrom, value=degreefromvalue[6],fg='green')
var_degreefrom7.grid(row=3, column=8)
var_degreefrom8 = tk.Radiobutton(root, text=degreefrom[7], variable=var_degreefrom, value=degreefromvalue[7],fg='green')
var_degreefrom8.grid(row=3, column=9)
#单选框 工作类型
var_jobterm = tk.StringVar()
var_jobterm1 = tk.Radiobutton(root, text=jobterm[0], variable=var_degreefrom, value=jobtermvalue[0],fg='green')
var_jobterm1.grid(row=4, column=2)
var_jobterm2 = tk.Radiobutton(root, text=jobterm[1], variable=var_degreefrom, value=jobtermvalue[1],fg='green')
var_jobterm2.grid(row=4, column=3)
var_jobterm3 = tk.Radiobutton(root, text=jobterm[2], variable=var_degreefrom, value=jobtermvalue[2],fg='green')
var_jobterm3.grid(row=4, column=4)
var_jobterm4 = tk.Radiobutton(root, text=jobterm[3], variable=var_degreefrom, value=jobtermvalue[3],fg='green')
var_jobterm4.grid(row=4, column=5)
var_jobterm5 = tk.Radiobutton(root, text=jobterm[4], variable=var_degreefrom, value=jobtermvalue[4],fg='green')
var_jobterm5.grid(row=4, column=6)
var_jobterm6 = tk.Radiobutton(root, text=jobterm[5], variable=var_degreefrom, value=jobtermvalue[5],fg='green')
var_jobterm6.grid(row=4, column=7)
#单选框 公司规模
var_companysize = tk.StringVar()
var_companysize1 = tk.Radiobutton(root, text=companysize[0], variable=var_companysize, value=companysizevalue[0],fg='green')
var_companysize1.grid(row=5, column=2)
var_companysize2 = tk.Radiobutton(root, text=companysize[1], variable=var_companysize, value=companysizevalue[1],fg='green')
var_companysize2.grid(row=5, column=3)
var_companysize3 = tk.Radiobutton(root, text=companysize[2], variable=var_companysize, value=companysizevalue[2],fg='green')
var_companysize3.grid(row=5, column=4)
var_companysize4 = tk.Radiobutton(root, text=companysize[3], variable=var_companysize, value=companysizevalue[3],fg='green')
var_companysize4.grid(row=5, column=5)
var_companysize5 = tk.Radiobutton(root, text=companysize[4], variable=var_companysize, value=companysizevalue[4],fg='green')
var_companysize5.grid(row=5, column=6)
var_companysize6 = tk.Radiobutton(root, text=companysize[5], variable=var_companysize, value=companysizevalue[5],fg='green')
var_companysize6.grid(row=5, column=7)
var_companysize7 = tk.Radiobutton(root, text=companysize[6], variable=var_companysize, value=companysizevalue[6],fg='green')
var_companysize7.grid(row=5, column=8)
var_companysize8 = tk.Radiobutton(root, text=companysize[7], variable=var_companysize, value=companysizevalue[7],fg='green')
var_companysize8.grid(row=5, column=9)
#单选框 发布日期
var_release_date = tk.StringVar()
var_release_date1 = tk.Radiobutton(root, text=release_date[0], variable=var_release_date, value=release_dateValue[0],fg='green')
var_release_date1.grid(row=6, column=2)
var_release_date2 = tk.Radiobutton(root, text=release_date[1], variable=var_release_date, value=release_dateValue[1],fg='green')
var_release_date2.grid(row=6, column=3)
var_release_date3 = tk.Radiobutton(root, text=release_date[2], variable=var_release_date, value=release_dateValue[2],fg='green')
var_release_date3.grid(row=6, column=4)
var_release_date4 = tk.Radiobutton(root, text=release_date[3], variable=var_release_date, value=release_dateValue[3],fg='green')
var_release_date4.grid(row=6, column=5)
var_release_date5 = tk.Radiobutton(root, text=release_date[4], variable=var_release_date, value=release_dateValue[4],fg='green')
var_release_date5.grid(row=6, column=6)
var_release_date6 = tk.Radiobutton(root, text=release_date[5], variable=var_release_date, value=release_dateValue[5],fg='green')
var_release_date6.grid(row=6, column=7)
#单选框 月薪范围
var_monthly_pay = tk.StringVar()
var_monthly_pay1 = tk.Radiobutton(root, text=monthly_pay[0], variable=var_monthly_pay, value=monthly_payValue[0],fg='green')
var_monthly_pay1.grid(row=7, column=2)
var_monthly_pay2 = tk.Radiobutton(root, text=monthly_pay[1], variable=var_monthly_pay, value=monthly_payValue[1],fg='green')
var_monthly_pay2.grid(row=7, column=3)
var_monthly_pay3 = tk.Radiobutton(root, text=monthly_pay[2], variable=var_monthly_pay, value=monthly_payValue[2],fg='green')
var_monthly_pay3.grid(row=7, column=4)
var_monthly_pay4 = tk.Radiobutton(root, text=monthly_pay[3], variable=var_monthly_pay, value=monthly_payValue[3],fg='green')
var_monthly_pay4.grid(row=7, column=5)
var_monthly_pay5 = tk.Radiobutton(root, text=monthly_pay[4], variable=var_monthly_pay, value=monthly_payValue[4],fg='green')
var_monthly_pay5.grid(row=7, column=6)
var_monthly_pay6 = tk.Radiobutton(root, text=monthly_pay[5], variable=var_monthly_pay, value=monthly_payValue[5],fg='green')
var_monthly_pay6.grid(row=7, column=7)
var_monthly_pay7 = tk.Radiobutton(root, text=monthly_pay[6], variable=var_monthly_pay, value=monthly_payValue[6],fg='green')
var_monthly_pay7.grid(row=7, column=8)
var_monthly_pay8 = tk.Radiobutton(root, text=monthly_pay[7], variable=var_monthly_pay, value=monthly_payValue[7],fg='green')
var_monthly_pay8.grid(row=7, column=9)
var_monthly_pay9 = tk.Radiobutton(root, text=monthly_pay[8], variable=var_monthly_pay, value=monthly_payValue[8],fg='green')
var_monthly_pay9.grid(row=7, column=10)
var_monthly_pay_x = tk.Radiobutton(root, text=monthly_pay[9], variable=var_monthly_pay, value=monthly_payValue[9],fg='green')
var_monthly_pay_x.grid(row=7, column=11)
var_monthly_pay_y = tk.Radiobutton(root, text=monthly_pay[10], variable=var_monthly_pay, value=monthly_payValue[10],fg='green')
var_monthly_pay_y.grid(row=7, column=12)
var_monthly_pay_z = tk.Radiobutton(root, text=monthly_pay[11], variable=var_monthly_pay, value=monthly_payValue[11],fg='green')
var_monthly_pay_z.grid(row=7, column=13)
var_monthly_pay_m = tk.Radiobutton(root, text=monthly_pay[12], variable=var_monthly_pay, value=monthly_payValue[12],fg='green')
var_monthly_pay_m.grid(row=7, column=14)
def bf():
    import os
    import random
    import time
    import pandas as pd
    from pyquery import PyQuery as pq
    import requests
    from urllib.parse import urlencode
    e = 0
    z = 0
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
    def get_one_pages(workyear, cotype, degreefrom, jobterm, companysize, release_date, monthly_pay):
        data = {
            'lang': 'c',
            'postchannel': '0000',
            'workyear': workyear,
            'cotype': cotype,
            'degreefrom': degreefrom,
            'jobterm': jobterm,
            'companysize': companysize,
            'ord_field': '0',
            'dibiaoid': '0',
        }
        for page in range(1, int(pages.get()) + 1):
            url = 'https://search.51job.com/list/000000,000000,0000,00,{},{},{},2,{}.html?'.format(release_date,monthly_pay,profession.get(), str(page)) + urlencode(data)
            yield url

    ################################################################

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
                    html = pq(url=el['href'], headers=headers, proxies=IP[random.randint(0, (len(IP) - 1))],
                              encoding="gbk")
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

        df.to_excel("{}/{}.xlsx".format(os.getcwd(), filename.get()), encoding='utf-8', index=False)
        print("###########数据写入完成...###########")
        end = time.time()
        print('###########您总共花费{}s##########'.format(end - start))

    ################################################################
    def main():
        print("###########查询中...###########")
        urls = get_one_pages(var_workyear.get(), var_cottype.get(), var_degreefrom.get(), var_jobterm.get(), var_companysize.get(), var_release_date.get(), var_monthly_pay.get())
        print("###########爬取中...###########")
        for url in urls:
            pares_html(url)
        write_datas()
        print("###########数据获取完毕...###########")

    if __name__ == '__main__':
        main()
        print("###########程序结束...###########")
# 执行按钮
b1 = tk.Button(root, text="一键爬取", font=("Arial", 10), width=25, command=bf,fg='blue')
b1.grid(row=11, column=2)
root.mainloop()
