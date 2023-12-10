import pymysql

from decouple import config

def conexion2023():
    conex=pymysql.connect(
                        host=config('BD_HOST'),
                        user=config('BD_USER'),
                        password=config('BD_PASSWORD'),
                        database=config('BD_DB'),
                        port=3306
                        )
    return conex