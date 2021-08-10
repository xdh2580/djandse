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
browser.quit()

# root=tkinter.Tk()

def get_something_fome_selenium():
    return su_content
