# 字符串初始化
html = """
<div id="container">
    <ul class="list">
        <li class="item-0">frst item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
</div>"""
from pyquery import PyQuery as pq

doc = pq(html)
#
# print(doc('li'))
# URL初始化
# doc1 = pq(url="http://www.baidu.com/")
# print(doc1('head'))
# # 文件初始化
# doc = pq(filename="文件名.html")
# css选择器
# print(doc('#container .list li'))
# 查找子元素
# items=doc('.list')
# print(type(items))
# lis=items.find("li")
# print(lis)
# lsl=items.children()#查找直接子元素
# print(lsl)
# 查找父元素
# items=doc('.list')
# container=items.parent()#.parents()查找所有父节点
# print(type(container))
# print(container)
# 获取兄弟元素
# li=doc('.list .item-0.active')
# print(li.siblings())
# 遍历单个元素
# 多个元素
lis=doc('li a').items()
print(type(lis))
a=[]
for i in lis:
    a.append(i.text())
    print(i)
print(a)
with open("./result.txt", "w+") as f:
    for i in range(len(a)):
       f.write(","+a[i])
# 获取属性
# a = doc('.item-0 a')
# print(a)
# print(a.attr('href'))
# print(a.attr.href)
# #获取文本
# b= doc('.item-0 a')
# print(b)
# print(b.text())
# 获取html标签
# li=doc('.item-0.active')
# print(li)
# print(li.html())
# Dom操作
# li=doc('.item-0.active')
# print(li)
# li.remove_class('active')
# print(li)
# li.add_class("active")
# print(li)
# 属性修改
# li=doc('.item-0.active')
# print(li)
# li.attr("name","link")
# print(li)
# li.css("font-size","14px")
# print(li)
# remove
# html1=""""
# <div class='wrap'>
#     Hellow World
#     <p>This is a pargarth</p>
# </div>
# """
# doc1=pq(html1)
# warp=doc1('.wrap')
# print(warp.text())
# warp.find('p').remove()
# print(warp.text())
# html2 = """
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#             <li class="item-0">frst item</li>
#             <li class="item-1"><a href="link2.html">second item</a></li>
#             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#             <li class="item-0"><a href="link5.html">fifth item</a></li>
#         </ul>
#      </div>
# </div>"""
# doc2 = pq(html2)
# l1=doc2('li:first-child')
# print(l1)
# l1=doc2('li:last-child')
# print(l1)
# l1=doc2('li:nth-child(2)')
# print(l1)
# l1=doc2('li:gt(2)')
# print(l1)
# l1=doc2('li:nth-child(2n)')
# l1=doc2('li:contains(second)')
# print(l1)