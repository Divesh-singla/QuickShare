import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from mysqlConnection.connection import getConnection
sql = getConnection()

def __updateStatus(userId  , tableName , statusFieldName , userIdFieldName):

    showStatusQuery = f"SELECT {statusFieldName} FROM {tableName} WHERE {userIdFieldName} = '{userId}'"
    sql.execute (showStatusQuery)
    status = sql.fetchone()
    if status != None:
        status = status[0]

    # print(status)
    if status == "off":
        status = "on"
    else:
        status = "off"

    
    statusUpdateQuery = f"UPDATE {tableName} SET {statusFieldName} = '{status}' WHERE {userIdFieldName} = '{userId}'"
    sql.execute(statusUpdateQuery)
    statusUpdateResult = sql.rowcount
    if statusUpdateResult > 0:
        return [True,"Order Updated"]
    else:

        return [False,"Order Not Updated"]


## bulk update
# def __updateStatus(values , tableName , statusField , userIdField):
#     count = 0
#     for x in values:
#         statusUpdateQuery = f"UPDATE {tableName} SET {statusField} = '{x['value']}' WHERE {userIdField} = '{x['id']}'"
#         # print(statusUpdateQuery)
#         sql.execute(statusUpdateQuery)
#         statusUpdateResult = sql.rowcount
#         count += int(statusUpdateResult)

#     if count > 0 :
#             return [True,"Order Updated"]
#     else:
#             return [False,"Order Not Updated"]

# print(__updateStatus([{"id":"66","value":"off"},{"id":"67","value":"off"}] , 'schooldetails' , "status" , "school_id"))

# print(__updateStatus("67" ,'schooldetails' ,  "status" , "school_id"))
