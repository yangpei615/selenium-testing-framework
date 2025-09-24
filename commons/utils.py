#  公共模块的函数放在这
import csv
import json
import  requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# 验证码识别函数
def imgcode(file):
    # 识别验证码
    url = "http://upload.chaojiying.net/Upload/Processing.php"
    data = {
        # 用户名
        "user":"xiaoyouzyp",
        # 密码
        "pass":"jolie4567",
        # 用户id
        "sofid": "970606",
        # 验证码类型
        "codetype": 1901
    }
    # 打开读取图片
    files = {"userfile":open(file,"rb")}
    rsp = requests.post(url,data =data, files = files)
    res = rsp.json()
    if res["err_no"] == 0:
        print("识别成功")
        code = res["pic_str"]
        print(f"验证码数字为：{code}")
        return  code
    else:
        print("识别失败")
        return False


# 保存cookie函数
def save_cookie(driver):
    # 将cookie信息保存在本地
    cookies = driver.get_cookies()
    with open("../data/cookies.json", "w")  as f:
        # json文件的数据python中不能直接进行使用，需要进行转换才能使用
        # json.dumps将python中的字典转换为json字符串对象
        f.write(json.dumps(cookies))

# 获取cookie函数
def load_cookie(driver):
    # 当页面没有cookie信息时，需要先正常登录然后再保持cookie，在下次页面进行访问时使用cookie
    # 将保持在本地的文件cookie信息读取并使用
    try:
        with open("../data/cookies.json") as f:
            cookies = json.loads(f.read())
        for cookie in  cookies:
            # 读取json文件里面所有的cookie信息
            driver.add_cookie(cookie)
        else:
            # for循环正常结束之后，所有cookie信息添加之后进行刷新
            driver.refresh()
    except:
        print("目前页面没有可以使用的cookie信息，需要正常登录获取cookie保持再使用")

# 判断是否第一次登录
def is_login(driver):
    try:
        # 显式等待某个代表“已登录”的元素出现
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="J_account"]/span'))
        )
        return True  # 找到元素，认为已登录
    except TimeoutException:
        return False  # 未找到元素，未登录


# 数据驱动获取csv文件
def get_csv_data():
    list1 = []
    # csv文件读取
    c1 = csv.reader(open(r"E:\python_learning\selenuim_learning\shangma_test\data\pay_data.csv",encoding='UTF-8'))
    for i in c1:
        list1.append(i)
    else:
        return list1
