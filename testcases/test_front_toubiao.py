import allure

from shangma_test.commons.pom_test_reception import ReceptionLoginPage
import pytest
from shangma_test.commons.utils import get_csv_data


# 以pytest模式编写用例
# 函数用例为主

# 参数化用例
@pytest.mark.parametrize("money, paypassword, assert_msg",[
    ['1000','66666','支付密码错误'],
    ['2000', '6668866', '支付密码错误'],
    ['3000', '6668866', '支付密码错误']
]
)
@allure.step("这是第一个测试用例")
@allure.severity(allure.severity_level.CRITICAL)
def  test_toubiao_fail1(user_driver, clear_deal_page, money, paypassword, assert_msg):
    allure.attach("描述：", "我是第一个反向用例")
    # 执行投标用例流程
    # 通过页面类对象调用执行方法脚本
    page = ReceptionLoginPage(user_driver)
    msg = page.pay(money, paypassword, assert_msg)
    # 断言结果
    assert msg == assert_msg



# # 使用csv传递用例
# @pytest.mark.parametrize("money, paypassword, assert_msg",get_csv_data())
# @allure.step("这是第二个测试用例")
# @allure.severity(allure.severity_level.CRITICAL)
# def  test_toubiao_fail2(user_driver, clear_deal_page, money, paypassword, assert_msg):
#     allure.attach("描述：","我是第二个反向用例")
#     # 执行投标用例流程
#     # 通过页面类对象调用执行方法脚本
#     page = ReceptionLoginPage(user_driver)
#     msg = page.pay(money, paypassword, assert_msg)
#     # 断言结果
#     assert msg == assert_msg
