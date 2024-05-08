import mysql.connector
import cx_Oracle

# Conexión a la primera base de datos MariaDB
conn_mariadb1 = mysql.connector.connect(
    host='',
    user='will',
    password='will',
    database='usuario'
)

# Conexión a la segunda base de datos MariaDB
conn_mariadb2 = mysql.connector.connect(
    host='',
    user='will',
    password='will',
    database='timestamp'
)

# Conexión a la base de datos Oracle
conn_oracle = cx_Oracle.connect(
    user='SYSTEM',
    password='oracle',
    dsn='anime'
)

# Cursores
cursor_mariadb1 = conn_mariadb1.cursor()
cursor_mariadb2 = conn_mariadb2.cursor()
cursor_oracle = conn_oracle.cursor()

def insert_values(usuario, tiempo, anime):
    try:
        # Insertar en la primera base de datos MariaDB
        query_mariadb1 = "INSERT INTO usuario (usuario) VALUES (%s)"
        cursor_mariadb1.execute(query_mariadb1, (usuario,))
        conn_mariadb1.commit()

        # Insertar en la segunda base de datos MariaDB
        query_mariadb2 = "INSERT INTO tiempo (tiempo) VALUES (%s)"
        cursor_mariadb2.execute(query_mariadb2, (tiempo,))
        conn_mariadb2.commit()

        # Insertar en la base de datos Oracle
        query_oracle = "INSERT INTO anime (anime) VALUES (:1)"
        cursor_oracle.execute(query_oracle, (anime,))
        conn_oracle.commit()

        print("Valores insertados correctamente en las tres bases de datos.")
    except Exception as e:
        print(f"Error al insertar valores: {e}")

def select():
    try:
        # Consultas a las bases de datos
        query_mariadb1 = "SELECT usuario FROM usuario"
        cursor_mariadb1.execute(query_mariadb1)
        result_mariadb1 = cursor_mariadb1.fetchall()

        query_mariadb2 = "SELECT tiempo FROM tiempo"
        cursor_mariadb2.execute(query_mariadb2)
        result_mariadb2 = cursor_mariadb2.fetchall()

        query_oracle = "SELECT anime FROM anime"
        cursor_oracle.execute(query_oracle)
        result_oracle = cursor_oracle.fetchall()

        # Combinar resultados
        combined_results = []
        for row_mariadb1, row_mariadb2, row_oracle in zip(result_mariadb1, result_mariadb2, result_oracle):
            combined_results.append([row_mariadb1[0], row_mariadb2[0], row_oracle[0]])

        return combined_results
    except Exception as e:
        print(f"Error al realizar la consulta: {e}")
        return None
