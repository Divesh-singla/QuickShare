import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from mysqlConnection.connection import getConnection
from helper.tableDetails import __getUserDetails

sql = getConnection()

def getChangedPassword(currentPassword , newPassword , userID):
    
    cuurentPasswordDb = (__getUserDetails(userID).get('password'))

    if cuurentPasswordDb != None:

        if cuurentPasswordDb == currentPassword:

            if currentPassword != newPassword:
                updatePassQuery = f"UPDATE user SET password = '{newPassword}' WHERE userId = '{userID}'"
                sql.execute(updatePassQuery)
                updatePassResult = sql.rowcount

                if updatePassResult > 0 :
                    return [True,"Password changed successfully"]
            
            elif currentPassword == newPassword:
                return [False , "current password & new password can't be same!"]

        elif cuurentPasswordDb != currentPassword:
            return [False,"Current password not matched!"]

    if cuurentPasswordDb  == None:
        updatePassQuery = f"UPDATE user SET password = '{newPassword}' WHERE userId = '{userID}'"
        sql.execute(updatePassQuery)
        updatePassResult = sql.rowcount
        if updatePassResult >0:
            return [True,"Password changed successfully"]

# print(getChangedPassword('25d55ad283aa400af464c76d713c07ad','12234','1'))