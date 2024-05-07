import psycopg2

class Coneccion:
    def __init__():
        host = "localhost"
        dbname = "principal"
        user = "azulito"
        password = "1234"
        port = "5432"
        #conn = psycopg2.connect(host="localhost",dbname="principal",
        #    user="azulito",password="1234",port="5432")
    def do(query):
        conn = psycopg2.connect(host=host,dbname=dbname,user=user,password=password,port = port)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        try:
            res = cur.fetchall()
        except:
            res = None

        cur.close()
        conn.close()

        return res
        