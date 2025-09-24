from shangma_test.commons.pom_test_reception import ReceptionLoginPage
from selenium.webdriver.chrome.service import  Service
from selenium import webdriver



# 新建一个驱动
driver = webdriver.Chrome(service=Service(r'D:\softrun\tools\chromedriver-win64\chromedriver.exe'))
# 被测系统地址
url = 'http://47.107.116.139/fangwei/'
# 访问被测页面
driver.get(url)
# 将页面最大化
driver.maximize_window()


# 实例化一个对象
page = ReceptionLoginPage(driver)

# 登录用例执行
# 用例执行完成后获取实际结果
msg = page.login("Padmin",'jolie4567')
# 断言实际结果
assert msg == "成功登录"


# 投标 用例执行
# 用例执行完成后获取实际结果
msg = page.pay('1000', '123456')
# 断言实际结果
assert msg == "支付密码错误"

#  关闭页面
driver.quit()




