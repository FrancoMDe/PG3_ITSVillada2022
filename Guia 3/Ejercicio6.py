import pymysql

miConexion = pymysql.connect(
    host="localhost", user="jsn", passwd="pepe1234", db="Biblioteca"
)
cur = miConexion.cursor()
try:
    cur.execute("SELECT * FROM Empleado")
    print(cur.fetchall())
except pymysql.err.ProgrammingError as e:
    print("Error en el comando!!!!!")
    print(e)

miConexion.close()
