from selenium.webdriver  import Chrome, Firefox, Edge
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service

# 自定义函数获取对应的浏览器驱动
def  get_webdriver(name: str='Chrome'):
    # 根据调用获取浏览器的实参来返回对应的驱动
    # 将具体浏览器实参名字进行整理
    # 将所有浏览器的名字转化为小写
    # 将所有浏览器的名字中空格去除
    # 再返回驱动的驱动
    name = name.lower().replace(" ","")
    match name:
        case "chrome":
            return  webdriver.Chrome(service=Service(r'D:\softrun\tools\chromedriver-win64\chromedriver.exe'))
        case "firefox":
            return Firefox()
        case "edge":
            return Edge()
        case "_":
            raise ValueError(f"不支持的浏览器名称: {name}。请使用 chrome/firefox/edge")
