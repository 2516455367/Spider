# match匹配
# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.span())
# 匹配目标
# import re
#
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld', content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())
# 通用匹配
# import re
#
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*Demo$', content)
# print(result)
# print(result.group())
# print(result.span())
# 贪婪与非贪婪
# import re
#
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*(\d+).*Demo$', content)
# print(result)
# print(result.group(1))
# import re

# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result)
# print(result.group(1))
# import re
#
# content = 'http://weibo.com/comment/kEraCN'
# result1=re.match('')
# result1 = re.match('http.*?comment/(.*?)', content)
# result2 = re.match('http.*?comment/(.*)', content)
# print('result1', result1.group(1))
# print('result2', result2.group(1))
# 修饰符
# import re
#
# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
# result = re.match('^He.*?(\d+).*?Demo$', content,re.S)
# print(result.group(1))
# 表 3-3　修饰符
#
# 修饰符	描　　述
# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使。匹配包括换行在内的所有字符
# re.U	根据 Unicode 字符集解析字符。这个标志影响 \w、\W、\b 和 \B
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解
# 转义匹配
# import re
#
# content = '(百度) www.baidu.com'
# result = re.match('^\(百度\)(.*?m$)', content)
# print(result.group(1))


# 3. search
# import re
#
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result)
#
html = '''<div id="songs-list">
<h2 class="title"> 经典老歌 </h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2"> 一路上有你 </li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐"> 沧海一声笑 </a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦"> 往事随风 </a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond"> 光辉岁月 </a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳"> 记事本 </a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君"> 但愿人长久 </a>
</li>
</ul>
</div>'''
# import re
# result=re.search('<li.*?view="6".*?singer="(.*?)">(.*?)<.*?>',html,re.S)
# print(result.group(1),result.group(2))

# 4. findall
import re
results=re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)<.*?</li>',html,re.S)
for i in results:
    print(i)


# 5. sub
# import re
#
# content = '54aK54yr5oiR54ix5L2g'
# content = re.sub('\d{2}ix\d{1}', '', content)
# print(content)


# # 6. compile
# import re
#
# content1 = '2016-12-15 12:00'
# content2 = '2016-12-17 12:55'
# content3 = '2016-12-22 13:21'
# pattern=re.compile('\d{2}:\d{2}')
# result1=re.sub(pattern," ",content1)
# result2 = re.sub(pattern, '', content2)
# result3 = re.sub(pattern, '', content3)
# print(result1, result2, result3)
#
#






















