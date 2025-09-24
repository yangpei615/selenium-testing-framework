from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import traceback

try:
    # 创建驱动
    driver = webdriver.Chrome(service=Service(r'D:\softrun\tools\chromedriver-win64\chromedriver.exe'))

    # 被测系统地址
    url = 'http://47.107.116.139/fangwei/'
    driver.get(url)

    # 将页面最大化
    driver.maximize_window()

    input("按回车关闭浏览器...")
    driver.quit()

except Exception as e:
    print("发生异常：", e)
    print("\n异常详情：")
    traceback.print_exc()

