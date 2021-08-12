"""该类用于存储movie信息，手动映射数据库中对应表的数据"""
import pymysql


class Movie:
    movie_order = ""
    movie_name = ""
    movie_score = ""
    movie_direct = ""
    movie_public_time = ""
    movie_time = ""

    def __init__(self, movie_order, movies_name, movie_score, movie_direct, movie_public_time, movie_time):
        self.movie_order = movie_order
        self.movie_name = movies_name
        self.movie_score = movie_score
        self.movie_direct = movie_direct
        self.movie_public_time = movie_public_time
        self.movie_time = movie_time

    # def insert_self_into_db(self):
    #     db = pymysql.connect(
    #         host='localhost',
    #         user='root',
    #         password='123456',
    #         db='mydb1',
    #         charset='utf8',
    #         # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    #     )
    #     try:
    #         cursor = db.cursor()
    #         sql = """insert into table1(name) values('%s') """ % self.movie_name
    #         print("sql:" + sql)
    #         cursor.execute(sql)
    #         db.commit()
    #         print("插入成功")
    #     except Exception:
    #         print("插入异常，已跳过")
    #     finally:
    #         db.close()