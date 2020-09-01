#基本使用
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# browser = webdriver.Ie()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()


#############################################
#
# #申明浏览器对象
# from selenium import webdriver
# # # browser=webdriver.Edge()
# # browser=webdriver.Chrome()
#############################################
# #访问页面
# browser=webdriver.Ie()
# browser.get('https://www.taobao.com/')
# print(browser.page_source)
# browser.close()
#############################################
#查找单个元素
# from selenium import webdriver
# browser=webdriver.Ie()
# browser.get("https://www.taobao.com/")
# input_first=browser.find_element_by_id('q')
# input_second=browser.find_element_by_css_selector("#q")
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first,input_second,input_third)
# browser.close()
#方法
#find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector
# from selenium import webdriver

# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element(By.ID, 'q')
# print(input_first)
# browser.close()

#################################################
#查找多个元素
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# browser=webdriver.Ie()
# browser.get("https://www.taobao.com/")
# lis=browser.find_elements_by_css_selector('.service-bd li')
# print(lis)
# browser.close()
# lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
#方法：
# find_elements_by_id
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector
####################################
#元素交互
# from selenium import webdriver
# import time
# browser=webdriver.Ie()
# browser.get('https://www.taobao.com')
# Input=browser.find_element_by_id('q')
# Input.send_keys('iphone')
# time.sleep(1)
# Input.clear()
# Input.send_keys('ipad')
# button=browser.find_element_by_class_name('btn-search')
# button.click()
#http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement
########################################################
#动作交互
# from selenium import webdriver
# # from selenium.webdriver import ActionChains
# #
# # browser = webdriver.Ie()
# # url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# # browser.get(url)
# # browser.switch_to.frame('iframeResult')
# # source = browser.find_element_by_css_selector('#draggable')
# # target = browser.find_element_by_css_selector('#droppable')
# # actions = ActionChains(browser)
# # actions.drag_and_drop(source, target)
# # actions.perform()
###########################################################
#执行javaScript
from selenium import webdriver

# browser = webdriver.Ie()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')
#########################################################
#获取节点信息
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# browser = webdriver.Ie()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))
#############################################
#获取文本值
# from selenium import webdriver
#
# browser = webdriver.Ie()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)
###########################################
#获取 ID、位置、标签名、大小
# from selenium import webdriver
#
# browser = webdriver.Ie()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)
#切换Frame
# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
#
# browser = webdriver.Ie()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)
#隐式等待
# from selenium import webdriver
#
# browser = webdriver.Ie()
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)#
# 在这里我们用 implicitly_wait() 方法实现了隐式等待。
#显示等待
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser = webdriver.Ie()
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)
#关于等待条件，其实还有很多，比如判断标题内容，判断某个节点内是否出现了某文字等。表 7-1 列出了所有的等待条件。
#
# 表 7-1　等待条件及其含义
#
# 等待条件	含义
# title_is	标题是某内容
# title_contains	标题包含某内容
# presence_of_element_located	节点加载出，传入定位元组，如 (By.ID, 'p')
# visibility_of_element_located	节点可见，传入定位元组
# visibility_of	可见，传入节点对象
# presence_of_all_elements_located	所有节点加载出
# text_to_be_present_in_element	某个节点文本包含某文字
# text_to_be_present_in_element_value	某个节点值包含某文字
# frame_to_be_available_and_switch_to_it frame	加载并切换
# invisibility_of_element_located	节点不可见
# element_to_be_clickable	节点可点击
# staleness_of	判断一个节点是否仍在 DOM，可判断页面是否已经刷新
# element_to_be_selected	节点可选择，传节点对象
# element_located_to_be_selected	节点可选择，传入定位元组
# element_selection_state_to_be	传入节点对象以及状态，相等返回 True，否则返回 False
# element_located_selection_state_to_be	传入定位元组以及状态，相等返回 True，否则返回 False
# alert_is_present	是否出现 Alert
#. 前进后退
# import time
# from selenium import webdriver
#
# browser = webdriver.Ie()
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://www.python.org/')
# browser.back()#后退一个页面
# time.sleep(1)
# browser.forward()#前进一个页面
# browser.close()
##########################################
#Cookies
# from selenium import webdriver
#
# browser = webdriver.Ie()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())
#############################################
#选项卡管理
# import time
# from selenium import webdriver
# browser = webdriver.Ie()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')
##################################################
#异常处理
# from selenium import webdriver
#
# browser = webdriver.Ie()
# browser.get('https://www.baidu.com')
# browser.find_element_by_id('hello')
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()
