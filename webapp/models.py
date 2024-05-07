from django.contrib.auth.models import AbstractUser
from django.db import models
#from coneccion import Coneccion
import psycopg2

class Coneccion:
    #def __init__():
    host = "localhost"
    dbname = "principal"
    user = "azulito"
    password = "1234"
    port = "5432"
    #conn = psycopg2.connect(host="localhost",dbname="principal",
        #    user="azulito",password="1234",port="5432")
    def do(self,query):
        conn = psycopg2.connect(host=self.host,dbname=self.dbname,
            user=self.user,password=self.password,port = self.port)
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
"""
class Animes(models.Model):
    id_anime = models.AutoField(primary_key=True)
    nombre_anime = models.CharField(max_length=100)
    descripcion_anime = models.CharField(max_length=500, default='no.jpg')
    imagen_anime = models.CharField(max_length=50, default='no.jpg')
    portada_anime = models.CharField(max_length=50, default='no.jpg')

    def __str__(self):
        return self.nombre_anime
"""
sql = Coneccion()
class Animes():
    tabla = "Animes"
    def __init__(self,id = 0,nom = "",des = "",img = "",portada = ""):
        #sql = Coneccion()
        self.tabla = "Animes"
        self.id_anime = id
        self.nombre_anime = nom
        self.descripcion_anime = des
        self.imagen_anime = img
        self.portada_anime = portada
        sql.do(f"""
        CREATE TABLE IF NOT EXISTS {self.tabla}(
            id_anime SERIAL PRIMARY KEY,
            nombre_anime varchar,
            descripcion_anime varchar,
            imagen_anime varchar,
            portada_anime varchar
        );
        """)
    def save(self):
        sql.do(f"""
            INSERT INTO {self.tabla}(nombre_anime,descripcion_anime,
            imagen_anime,portada_anime) VALUES
            ('{self.nombre_anime}','{self.descripcion_anime}',
            '{self.imagen_anime}','{self.portada_anime}');
        """)

    def all(self):
        #sql = Coneccion()
        al = []
        res = sql.do(f"""SELECT * FROM {self.tabla};""")
        for row in res:
            print(row)
            #print(row[0],row[1])
            An = Animes(row[0],row[1],row[2],row[3],row[4])
            #print(An)
            al.append(An)
        return al
    def all():
        tabla = "Animes"
        #sql = Coneccion()
        al = []
        res = sql.do(f"""SELECT * FROM {tabla};""")
        for row in res:
            print(row)
            An = Animes(row[0],row[1],row[2],row[3],row[4])

            al.append(An)
        return al
    def find_by_name(nombre):
        tabla = "Animes"
        #sql = Coneccion()
        res = sql.do(f"""SELECT * FROM {tabla} where nombre_anime = '{nombre}';""")
        row = res[0]
        An = Animes(row[0],row[1],row[2],row[3],row[4])
        return An
    
    def __str__(self):
        return self.nombre_anime

"""
class Episodios(models.Model):
    id_episodio = models.AutoField(primary_key=True)
    nombre_episodio = models.CharField(max_length=100)
    temporada = models.IntegerField(default=0)
    ruta_imagen_episodio = models.CharField(max_length=50, default='no.jpg')
    ruta_episodio = models.CharField(max_length=50, default='no.jpg')
    #episodio_anime = models.ForeignKey(Animes, on_delete=models.CASCADE, null=True, blank=True)
    episodio_anime = ""

    def __str__(self):
        return self.nombre_episodio
"""
class Episodios():
    tabla = "Episodios"
    def __init__(self,anime = ""):
        try:
            res = sql.do(f"select id_anime from Animes where nombre_anime = '{anime}'")
            episodio_anime_id = res[0]
        except:
            episodio_anime_id = 0
        #sql = Coneccion()
        self.id_episodio = 0
        self.nombre_episodio = ""
        self.temporada = 1
        self.ruta_imagen_episodio = ""
        self.ruta_episodio = ""
        inicial()
    def __init__(self,id,name,temp,anime_id,rut_img,rut_ep):
        self.id_episodio = id
        self.nombre_episodio = name
        self.temporada = temp
        self.episodio_anime_id = anime_id
        self.ruta_imagen_episodio = rut_img
        self.ruta_episodio = rut_ep
        inicial()
    def inicial(self):
        sql.do(f"""
        CREATE TABLE IF NOT EXISTS {self.tabla}(
            id_episodio SERIAL PRIMARY KEY,
            nombre_episodio varchar,
            temporada int,
            episodio_anime_id int
            ruta_imagen_episodio varchar,
            ruta_episodio varchar,
        );
        """)
    def save(self):
        sql.do(f"""
            INSERT INTO {self.tabla}(nombre_episodio,temporada,episodio_anime_id,
            ruta_imagen_episodio,ruta_episodio) VALUES
            ('{self.nombre_episodio}',{self.temporada},{episodio_anime_id},
            '{self.ruta_imagen_episodio}','{self.ruta_episodio}');
        """)

    def all(self):
        #sql = Coneccion()
        al = []
        res = sql.do(f"""SELECT * FROM {self.tabla} where 
            episodio_anime_id = {self.episodio_anime_id};""")
        for row in res:
            print(row)
            #print(row[0],row[1])
            #An = Animes(row[0],row[1],row[2],row[3],row[4])
            An = Episodios(row[0],row[1],row[2],row[3],row[4],row[5])
            #print(An)
            al.append(An)
        return al
    def all(anime_id):
        tabla = "Episodios"
        al = []
        res = sql.do(f"""SELECT * FROM {tabla} where 
            episodio_anime_id = {anime_id};""")
        for row in res:
            print(row)
            #print(row[0],row[1])
            #An = Animes(row[0],row[1],row[2],row[3],row[4])
            An = Episodios(row[0],row[1],row[2],row[3],row[4],row[5])
            #print(An)
            al.append(An)
        return al
    def one(ep_id):
        tabla = "Episodios"
        al = []
        res = sql.do(f"""SELECT * FROM {tabla} where 
            id_episodio = {ep_id};""")
        row = res[0]
        An = Episodios(row[0],row[1],row[2],row[3],row[4],row[5])
        return An
    
    def __str__(self):
        return self.nombre_anime

class Usuario(AbstractUser):
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    #episodio = models.ForeignKey(Episodios, on_delete=models.CASCADE, null=True, blank=True)
    episodio = ""
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username
"""
class Usuario:
    tabla = "Usuarios"
    def __init__(self):

        sql.do(f""#"
        CREATE TABLE IF NOT EXISTS {self.tabla}(
            id_anime SERIAL PRIMARY KEY,
            nombre_anime varchar,
            descripcion_anime varchar,
            imagen_anime varchar,
            portada_anime varchar
        );
        ""#")
    def save(self):
        sql.do(f""#"
            INSERT INTO {self.tabla}(nombre_anime,descripcion_anime,
            imagen_anime,portada_anime) VALUES
            ('{self.nombre_anime}','{self.descripcion_anime}',
            '{self.imagen_anime}','{self.portada_anime}');
        ""#")
        """
