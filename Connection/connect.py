from peewee import *

mysql = MySQLDatabase(
    "GilAisp2_Prepare",
    user="GilAisp2_Admin",
    password="000000",
    host="10.11.13.118",
    port=3306
)

if __name__ == "__main__":
    mysql.connect()