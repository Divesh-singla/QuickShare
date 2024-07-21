
import sys
sys.path.insert(0,r'S:\ACIL\project\attendanceCRM')
from mysqlConnection.connection import getConnection

sql = getConnection()

def addClientQuery(firstName , lastName , emailAddress , userName , passWord, token="" , type = ""  ,userId = ""):
    if type == "edit" and userId:
        userUpdateQuery = f"UPDATE clientuser SET first_name = '{firstName}', last_name = '{lastName}', email =  '{emailAddress}' , user_name =  '{userName}'  WHERE clientUserId = '{userId}'"
        sql.execute(userUpdateQuery)
        userUpdateResult = sql.rowcount
        if userUpdateResult>0:
            return [True , "Record Updated"]
        else:
            return [False , "Record Not Updated !"]

    else:
        userInsertQuery = f"INSERT INTO clientuser (first_name , last_name , email , user_name , password , token ) VALUES ('{firstName}' , '{lastName}' , '{emailAddress}' , '{userName}' , '{passWord}' , '{token}' )"
        sql.execute(userInsertQuery)
        userInsertResult = sql.rowcount
        if userInsertResult>0:
            return [True , "Record Saved"]
        else:
            return [False , "Record Not Saved !"]