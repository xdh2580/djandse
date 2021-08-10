from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import tkinter
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
import time

# 设置selenium使用chrome的无头模式
chrome_options = Options()

# chrome_options.add_argument('headless')  # 设置option,隐藏浏览器界面
# 在启动浏览器时加入配置
browser = webdriver.Chrome(
    r'C:\Users\XDH\PycharmProjects\seleniumfirst\venv\Scripts\chromedriver.exe',
    options=chrome_options)  # 获取chrome浏览器的驱动，并启动Chrome浏览器


def baidu():
    # 打开百度
    browser.get('https://www.baidu.com/')
    # 等待加载，最多等待20秒
    browser.implicitly_wait(20)
    browser.maximize_window()  # 窗口最大化

    su = browser.find_element_by_id("su")
    kw = browser.find_element_by_id("kw")
    su_content = su.get_attribute("value")
    print(su_content)

    browser.maximize_window()
    browser.set_script_timeout(5)
    kw.send_keys("selenium")
    su.click()
    # browser.refresh()
    # browser.execute_script("alert('hello')")
    browser.back()
    browser.execute_script("alert('浏览器将在3秒后自动关闭')")
    time.sleep(3)
    browser.quit()

    # root=tkinter.Tk()


def douban():
    browser.get('https://www.km.com/piandan/1912.html?page=1')
    # 等待加载，最多等待20秒
    browser.implicitly_wait(20)
    browser.maximize_window()  # 窗口最大化
    a = browser.find_element_by_class_name("m-t-t")
    b = browser.find_elements_by_class_name("m-t-t")
    print(a.text)
    for i in b:
        print(i.text)



def get_something_fome_selenium():
    # return su_content
    return "something"


douban()
browser.execute_script("alert('浏览器将在3秒后自动关闭')")
time.sleep(3)
browser.quit()