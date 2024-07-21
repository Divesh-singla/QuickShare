import pymysql
# dataBase = pymysql.Connect(user="root",password="",host="localhost",database="schoolcrm", autocommit=True)
# sql = dataBase.cursor()
def getConnection():
    try:
        dataBase = pymysql.Connect(user="root",password="",host="localhost",database="quicksharedb", autocommit=True)
        sql = dataBase.cursor()
        return sql

    except:
        return "Connection Error With database"
