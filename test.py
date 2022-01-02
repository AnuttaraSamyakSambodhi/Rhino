import sqlite3

ver = sqlite3.version
print(ver)

sqver = sqlite3.sqlite_version
print(sqver)

con = sqlite3.connect("d:/DATAbase/kospi.db")
type(con)

cursor = con.cursor()

cursor.execute("CREATE TABLE kakao(Date text, Open int,High int, Low int, Closing int,Volumn int")