import sys
from mysqlConnection.connection import getConnection
from constant.message import FAILURE, SUCCESS, ALREADYEXIST,get_message

sql = getConnection()


def getfileAccessDetails(clientID):

    if clientID!=None:
     
        getFileAccessQuery = f"SELECT fileId FROM fileaccess where clientID='{clientID}'"
        sql.execute(getFileAccessQuery)
        getFileAccessQueryResult = sql.fetchall()
        return getFileAccessQueryResult
    else:
        return ["",""]
    