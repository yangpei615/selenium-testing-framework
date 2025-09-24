from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service
import  time
from shangma_test.commons.utils import imgcode,save_cookie,load_cookie,is_login


#创建驱动
driver = webdriver.Chrome(service=Service(r'D:\softrun\tools\chromedriver-win64\chromedriver.exe'))
# 被测系统地址
url = 'http://47.107.116.139/fangwei/'

# 访问被测页面
driver.get(url)
# 将页面最大化
driver.maximize_window()
# 获取cookie信息保持登录状态
load_cookie(driver)

if is_login(driver):
    # 前台登录页面用例
    # 点击登录按钮
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[1]/div/a').click()
    time.sleep(3)
    # 输入账户
    driver.find_element(By.XPATH,'//*[@id="login-email-address"]').send_keys("Padmin")
    # 输入密码
    driver.find_element(By.XPATH,'//*[@id="login-password"]').send_keys('jolie4567')
    # 获取验证码图片
    driver.find_element(By.XPATH,'//*[@id="Jverify_img"]').screenshot('verify.png')
    # 识别验证码
    code = imgcode('verify.png')
    # 输入验证码
    driver.find_element(By.XPATH,'//*[@id="Jverify"]').send_keys(code)
    time.sleep(1)
    # 点击登录按钮
    driver.find_element(By.XPATH,'//*[@id="ajax-login-submit"]').click()
    # 获取登录后内容
    time.sleep(2)
    msg = driver.find_element(By.XPATH,'//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]').text
    assert msg =="成功登录"
    #  登录后点击确定按钮
    driver.find_element(By.XPATH,'//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]').click()
    # 保存cookie信息
    save_cookie(driver)

else:
    time.sleep(3)
    # 点击马上投标按钮
    driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[1]/div[1]/ul/li[1]/span[6]/a/span').click()
    # 输入投资金额
    driver.find_element(By.XPATH, '//*[@id="J_BIDMONEY"]').send_keys('1000')
    # 点击立即投标
    driver.find_element(By.XPATH, '//*[@id="tz_link"]').click()
    time.sleep(3)
    # 输入支付密码
    driver.find_element(By.XPATH, '//*[@id="J_bid_password"]').send_keys('123456')
    # 点击确定按钮
    driver.find_element(By.XPATH, '//*[@id="J_bindpassword_btn"]').click()
    time.sleep(3)
    # 获取支付结果
    pay_msg = driver.find_element(By.XPATH, '//*[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[2]').text
    assert pay_msg == "支付密码错误"


