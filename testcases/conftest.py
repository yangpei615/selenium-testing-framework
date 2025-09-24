import time
import pytest
from shangma_test.commons.driver import get_webdriver
from shangma_test.commons.pom_test_reception import ReceptionLoginPage
from shangma_test.commons.utils import  load_cookie, is_login, save_cookie
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 通过fixture处理前后置
@pytest.fixture
def driver():
    return get_webdriver()


# 定义让前台保持登录状态的fixture,作用域是整个测试会话
@pytest.fixture(scope='session')
def user_driver():
    # driver = webdriver.Chrome(service=Service(r'D:\softrun\tools\chromedriver-win64\chromedriver.exe'))
    driver = get_webdriver()
    # 获取驱动
    driver.get("http://47.107.116.139/fangwei/")
    driver.maximize_window()
    # 使用cookies信息
    load_cookie(driver)
    # 等待页面渲染
    time.sleep(2)

    # 如果第一次登录：没有cookie信息那么正常流程登录
    if not is_login(driver):
        # 创建页面类对象
        page = ReceptionLoginPage(driver)
        # 通过页面类对象调用执行方法脚本
        page.login("Padmin","jolie4567")

    yield driver

    # 第一次正常登录之后，用例执行结束之后，完成后置保持cookie信息
    save_cookie(driver)
    print("当前是否已登录？", is_login(driver))

#  定义清除缓存的夹具，可以结合第一次成功登录的夹具一起使用
@pytest.fixture
def clear_deal_page(user_driver):
    user_driver.get("http://47.107.116.139/fangwei/index.php?ctl=deal&id=20972")
    yield user_driver