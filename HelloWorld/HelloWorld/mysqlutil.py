import pymysql


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
