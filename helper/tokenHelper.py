import time
import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from mysqlConnection.connection import getConnection
sql = getConnection()

def __generateToken(encyptedPassword):
    currentTimeStamp = time.time()

    return (f"{encyptedPassword}"+f"{currentTimeStamp}")


def __getTokenFromDb(email , tableName , tokenColoumnName , emailColomnName):
    tableQuery = f"SELECT {tokenColoumnName} FROM  {tableName} WHERE {emailColomnName} = '{email}'"
    sql.execute(tableQuery)
    tableResult = sql.fetchone()
    # print(tableResult,"1111111111111111")
    if tableResult:
        return [True , tableResult[0]]
    else:
        return [False , ""]
