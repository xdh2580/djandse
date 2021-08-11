import pymysql


# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "123456", "mydb1", charset='utf8')
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT * FROM table1")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchall()
#
# print(data[0])
#
# # 关闭数据库连接
# db.close()


def insert_movie(name):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='mydb1',
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )

    cursor = db.cursor()
    sql = """insert into table1(name) values('%s') """ % name
    print("sql:" + sql)
    cursor.execute(sql)
    db.commit()
    print("插入成功")
    db.close()
