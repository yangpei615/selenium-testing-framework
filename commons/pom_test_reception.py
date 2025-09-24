# 使用pom模式封装
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from shangma_test.commons.utils import imgcode


#  定义一个公共父类
class BasePage:
    # 一旦对象被创建，获取实例属性驱动
    def __init__(self, driver):
        self.driver = driver

    # 定义一个类方法完成显示等待
    # 由于类方法中，不能使用实例属性，那么将类方法改成实例方式
    def wait(self, func):
        return WebDriverWait(self.driver, 5).until(func)

    # 重写定位元素的方法，结合显示等待
    def find_element(self, by, value, need_wait=False):
        def f(driver):
            if driver.find_element(by, value).text:
                msg = driver.find_element(by, value).text
                # 元素需要获取文本需要就可以传递实参为True来返回文本内容
                if need_wait:
                    # #当获取元素的文本，该元素存在但是没有出现文本，那么将空文本替换直到有文本才返回
                    return msg.replace(" ","")
                else:
                    return True
            else:
                return True
            # 一旦调用重写的find_element方法，那么先触发显示等待

        self.wait(f)
        # 触发完显示等待之后，使用原生find_element定位元素操作
        return self.driver.find_element(by, value)



# 登录页面类，继承父类
class ReceptionLoginPage(BasePage):
    # 将页面的元素定义为类属性
    # 登录按钮
    btn_login = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/a')
    # 账户
    ipt_username = (By.XPATH, '//*[@id="login-email-address"]')
    # 密码
    ipt_password = (By.XPATH, '//*[@id="login-password"]')
    # 验证码图片
    code_msg = (By.XPATH, '//*[@id="Jverify_img"]')
    # 验证码文本框
    ipt_code = (By.XPATH, '//*[@id="Jverify"]')
    # 登录按钮
    bth_login_submit = (By.XPATH, '//*[@id="ajax-login-submit"]')
    # 登录提示框
    log_msg = (By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]')
    # 登录后点击确定按钮
    bth_login_ok = (By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]')

    # 马上投标按钮
    btn_pay = (By.XPATH, '/html/body/div[7]/div[2]/div[1]/div[1]/ul/li[1]/span[6]/a/span')
    # 投资金额
    ipt_money = (By.XPATH, '//*[@id="J_BIDMONEY"]')
    # 立即投标
    bth_ipay= (By.XPATH, '//*[@id="tz_link"]')
    # 支付密码
    ipt_pay_passwd = (By.XPATH, '//*[@id="J_bid_password"]')
    # 确定按钮
    btn_pay_submit = (By.XPATH, '//*[@id="J_bindpassword_btn"]')
    # 支付结果
    pay_msg = (By.XPATH, '//*[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[2]')
    # 支付提示框
    txt_deal_msg = (By.XPATH, '//*[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[3]/input[1]')


    # 定义用例脚本执行登录步骤
    def login(self, username, password):
        # 点击登录按钮
        self.find_element(*self.btn_login).click()
        # 输入账户
        self.find_element(*self.ipt_username).send_keys(username)
        # 输入密码username
        self.find_element(*self.ipt_password).send_keys(password)
        # 获取验证码图片
        self.find_element(*self.code_msg).screenshot('data/verify.png')
        # 识别验证码
        code = imgcode('data/verify.png')
        # 输入验证码
        self.find_element(*self.ipt_code).send_keys(code)
        # 点击登录按钮
        self.find_element(*self.bth_login_submit).click()
        # 获取登录后内容
        msg = self.find_element(*self.log_msg).text
        #  登录后点击确定按钮
        self.find_element(*self.bth_login_ok).click()
        return  msg

    # 定义用例脚本执行投标 步骤
    def pay(self, money, paypasswd, assert_msg):
        # 点击马上投标按钮
        # self.find_element(*self.btn_pay).click()
        # 输入投资金额
        self.find_element(*self.ipt_money).send_keys(money)
        # 点击立即投标
        self.find_element(*self.bth_ipay).click()
        # 输入支付密码
        self.find_element(*self.ipt_pay_passwd).send_keys(paypasswd)
        # 点击确定按钮
        self.find_element(*self.btn_pay_submit).click()
        # 获取支付结果
        pay_msg = self.find_element(*self.pay_msg, need_wait=True).text
        # 关闭支付结果提示框
        self.find_element(*self.txt_deal_msg).click()
        return pay_msg