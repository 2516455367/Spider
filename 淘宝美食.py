from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)  # 等待时间


# KEYWORD='iPad'
def search():
    browser.get('https://www.taobao.com')
    input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
    )  # 等待#q加载完成
    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button'))
    )  # 点击按钮
    input.send_keys('美食')
    submit.click()  # 执行点击


def main():
    search()


if __name__ == '__main__':
    main()








