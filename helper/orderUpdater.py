import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from mysqlConnection.connection import getConnection
sql = getConnection()
import json
from types import SimpleNamespace

def __updateOrder(dataList, tableName , orderFieldName , userIdFieldName):

    data = json.loads(dataList, object_hook=lambda d: SimpleNamespace(**d))
    count = 0
    for dataIterator in data:
        orderUpdateQuery = f"UPDATE {tableName} SET {orderFieldName} = '{dataIterator.value}' WHERE {userIdFieldName} = '{dataIterator.id}' "
        sql.execute(orderUpdateQuery)
        orderUpdateResult = sql.rowcount
        count += orderUpdateResult

    if count > 0:
        return [True , "Order Updated"]

    else:
        return [False , "Order Not Updated"]