import sys
from tokenize import Token
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from mysqlConnection.connection import getConnection
from constant.settings import tokenName

def __logOut(tableName , tokenColumnName , token):
    try:

        sql = getConnection()

        deleteTokenQuery = f"UPDATE {tableName} SET {tokenColumnName} = ' ' WHERE {tokenColumnName} = '{token}'"

        sql.execute(deleteTokenQuery)
        result = sql.rowcount
        # result = 1
        # print()
        if result > 0:
            return [True , "Logout Successfull !"]
        
        return [False , "error"]


    except:
        return "Error with Database !"