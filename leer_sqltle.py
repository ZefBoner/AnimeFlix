import sqlite3
con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
res = cur.execute("""
SELECT 
    name
FROM 
    sqlite_schema
WHERE 
    type ='table';
""")
for row in res.fetchall():
    print(row)
res = cur.execute(
    #"select * from webapp_episodios"
    "select * from webapp_usuario"
    #"select * from webapp_animes"
    )
for row in res.fetchall():
    print(row)
#webapp_animes
#webapp_episodios

res = cur.execute(
    #"pragma table_info(webapp_episodios)"
    "pragma table_info(webapp_usuario)"
    #"pragma table_info(webapp_animes)"
    )
#print(res.fetchall())
for row in res.fetchall():
    print(row)