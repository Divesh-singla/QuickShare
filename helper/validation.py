import re

import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from mysqlConnection.connection import getConnection
sql = getConnection()
def __emailValidator(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex , email):
        return True
    else:
        return False
    
# import json
# from types import SimpleNamespace

# data = '[{"name": "John Smith", "id" : "hometown"}, {"name": "New York", "id": 123}]'

# # Parse JSON into an object with attributes corresponding to dict keys.
# x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))


def __validateFields(tableName , dataField , type=""):
    if type == None:
        query = f"SELECT * FROM {tableName}"
        sql.execute(query)
        result = sql.fetchall()

        duplicate  = False
        duplicatItems = []

        
        for rowIterator in result :
            for entityIterator in rowIterator:
                for dataIterator in dataField: 
                    if dataIterator  == entityIterator:

                        duplicate = True
                        duplicatItems.append(f"{entityIterator} Already Exists !")
        if duplicate :
            return [False , duplicatItems]
            
        else:
            return [True ,"All Available"]
    elif type == "edit":
        return [True , ""]

def __validationDb(validationColumnName ,tableName , validationData, idColumnName="" , userId = "", type=""):
    if type == "edit":
        query = f"SELECT {idColumnName} , {validationColumnName}  FROM {tableName}"
        # print(query)
        sql.execute(query)
        queryResult = sql.fetchall()
        for x in queryResult:
            if str(x[0]) != userId:
                if x[1] == validationData:
                    return [False , f'{validationData} already exists!']
                else:
                    return [True , f'{validationData}']
            # else:
            #     return [True , f'{validationData}']

    else:
        query = f"SELECT {validationColumnName} FROM {tableName} "
        sql.execute(query)
        queryResult = sql.fetchall()
        status = False
        if queryResult:
            for x in queryResult:
                print(x[0],"inside validatior__________")
                if x[0] == validationData:
                    status = True
            if status == True:   
                return [False , f'{validationData} already exists!']
            else:
                return [True , f'{validationData}']
        else:
            return [True , f'{validationData}']
            