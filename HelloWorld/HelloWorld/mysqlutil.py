import pymysql
from django.utils import html

def insert_movie(name, order="", score="", direct="", public_time="", time=""):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='mydb1',
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    try:
        cursor = db.cursor()
        sql = """insert into movie(morder,mname,score,direct,public_time,time) values('%s','%s','%s','%s','%s','%s') """ % (int(order), name, score, direct, public_time, time)
        print("sql:" + sql)
        cursor.execute(sql)
        db.commit()
        print("插入成功")
    except Exception as e:
        # raise e
        db.rollback()
        print("插入异常，已跳过")
    finally:
        db.close()


def get_movies_info_from_db():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='mydb1',
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    try:
        cursor = db.cursor()
        sql = """ select * from movie order by morder """
        print("sql:" + sql)
        cursor.execute(sql)
        movies = cursor.fetchall()
        movie_info_str_for_show = ""
        for m in movies:
            movie_info_str_for_show += str(m)+"<br>"  # 记得不能直接展示，要用format_html()让浏览器能将<br>等识别为html元素
    except Exception as e:
        raise e
    finally:
        db.close()
    return html.format_html(movie_info_str_for_show)
