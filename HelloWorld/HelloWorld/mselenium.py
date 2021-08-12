from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from HelloWorld.HelloWorld import mysqlutil
from HelloWorld.HelloWorld import movieinfo

import tkinter
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
import time

# 设置selenium使用chrome的无头模式
chrome_options = Options()
movieList = []  # 电影元组，其中append的每一个元素为一个Movie对象

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

    # browser.back()
    # browser.execute_script("alert('浏览器将在3秒后自动关闭')")
    # time.sleep(3)
    # browser.quit()

    # root=tkinter.Tk()


# 对照页面布局，爬取页面数据
def get_movies_info_in_current_page():
    # a = browser.find_element_by_class_name("m-t-t")
    movie = browser.find_elements_by_class_name("recommend-movie")
    for m in movie:
        order = m.find_element_by_class_name("m-t-n").text  # 排名
        name = m.find_element_by_class_name("m-t-t") .text  # 电影名
        r_m_info = m.find_element_by_class_name("r-m-info")
        score = r_m_info.find_element_by_class_name("score").text  # 评分
        info_detail = r_m_info.find_elements_by_class_name("info-detail")
        dire_info_l = info_detail[1].find_element_by_class_name("info-l")  # 第二个info-detail为导演信息
        dire = dire_info_l.find_element_by_class_name("info-value").text  # 导演名
        pub_info_m = info_detail[2].find_element_by_class_name("info-m")  # 第三个info-detail
        pub_time = pub_info_m.find_element_by_class_name("info-value").text  # 上映时间
        info_t = info_detail[2].find_element_by_class_name("info-t")  # 第三个info-detail
        movie_time = info_t.find_element_by_class_name("info-value").text  # 电影时长

        movie_obj = movieinfo.Movie(order, name, score, dire, pub_time, movie_time)
        movieList.append(movie_obj)


def douban():
    browser.get('https://www.km.com/piandan/1912.html?page=1')
    # 等待加载，最多等待20秒
    browser.implicitly_wait(20)
    browser.maximize_window()  # 窗口最大化

    # for i in range(1):
    while True:
        pages = browser.find_element_by_class_name("v_page")
        try:
            browser.implicitly_wait(10)
            get_movies_info_in_current_page()  # 获取当前网页中的电影信息
            next_page = pages.find_element_by_xpath("//*[text()='下一页']")
            next_page.click()
        except BaseException as e:
            # raise e # 如果raise异常，程序会直接停止并打印异常信息
            print("异常，未找到“下一页”，已是最后一页")
            break



def get_something_from_selenium():
    # return su_content
    all_in_one_string = ""
    for i in movieList:
        all_in_one_string = all_in_one_string + "\t" + i.movie_name

    return all_in_one_string


douban()  # 查找第三方网站豆瓣top250
# baidu()
browser.execute_script("alert('浏览器将在3秒后自动关闭')")
time.sleep(3)
browser.quit()
for i in movieList:
    # print(i.movie_name+i.movie_order+i.movie_score+i.movie_direct+i.movie_public_time+i.movie_time)
    mysqlutil.insert_movie(name=i.movie_name, order=i.movie_order, score=i.movie_score,
                           direct=i.movie_direct, public_time=i.movie_public_time, time=i.movie_time)

# print("------------------------------------")
# print(get_something_from_selenium())
