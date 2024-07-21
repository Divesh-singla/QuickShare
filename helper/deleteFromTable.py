import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from mysqlConnection.connection import getConnection
sql = getConnection()

def __deleteData(deletingList, tableName , idColumnName):
    deletedRowCount = 0
    deletingList = deletingList.split(",")
    for listIterator in deletingList:
        deleteQuery = f"DELETE FROM {tableName} WHERE {idColumnName} = '{listIterator}'"
        # print(deleteQuery)
        sql.execute(deleteQuery)
        result = sql.rowcount
        deletedRowCount += result
    # if len(deletedRowCount) == len(deletingList):
    return deletedRowCount


