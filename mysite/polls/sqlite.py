import sqlite3

con = sqlite3.connect("db.sqlite3")
cursor = con.cursor()

infos = cursor.execute("delete  from polls_poll where id='10' ")
con.commit()