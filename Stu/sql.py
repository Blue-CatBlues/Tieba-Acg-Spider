import sqlite3
db_path = r'D:\\迅雷下载\\chapter4\\chapter4\\test.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("SELECT SQLITE_VERSION();")
print(cur.fetchone())
tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print("Tables in the database:", tables)

cur.execute("INSERT INTO book VALUES (1,'红楼梦',22.00);")
cur.execute("INSERT INTO book VALUES (2,'活着',23.00);")
cur.execute("INSERT INTO book VALUES (3,'三国演义',34.00);")
cur.execute("INSERT INTO book VALUES (4,'水浒传',28.00);")

more_books=((5,'百年孤独',23.00),(6,"西游记",35.00),(7,"中国通史",36.00))
cur.executemany("INSERT INTO book VALUES (?,?,?)",more_books)
cur.execute("SELECT * FROM book").fetchone()

conn.commit()
conn.close()