#16.4, 16.5
import sqlite3
import csv
import sqlalchemy

con = sqlite3.connect("books.db")

cur = con.cursor()

cur.execute("CREATE TABLE books(title text, author text, year integer)")

insert_str = "insert into books values(?, ?, ?)"
with open("books2.csv", "rt",) as infile:
    books = csv.DictReader(infile)
    for book in books:
        cur.execute(insert_str, (book["title"], book["author"], book["year"]))

con.commit()

#16.6, 16.7
sql = 'select title from books order by title asc'
sql2 = 'select * from books order by year'
for row in con.execute(sql):
    print(row)

print()

for row in con.execute(sql2):
    print(row)

print()

#16.8
conn = sqlalchemy.create_engine("sqlite:///books.db")
sql3 = "select title from books order by title asc"
rows = conn.execute(sql3)
for row in rows:
    print(row)


con.execute("DROP TABLE books")