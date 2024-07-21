import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from mysqlConnection.connection import getConnection

def validateUser (userName , passWord):

    sql = getConnection()
    selectQuery = f"SELECT * FROM user WHERE Email = '{userName}' AND Password = '{passWord}';"
    sql.execute(selectQuery)
    queryResult = sql.fetchone()
    # print(queryResult)
    if queryResult == None:
        return (queryResult,f"Invalid Email or Password")
    else:
        return (queryResult , f'Welcome {userName}')


def getUsername(userId):
    sql = getConnection()
    selectQuery = f"SELECT concat(first_name,' ',last_name) as name FROM user WHERE userId = '{userId}';"
    sql.execute(selectQuery)
    queryResult = sql.fetchone()
    if queryResult == None:
        return (None)
    else:
        return (queryResult)
    

def validateClientUser (userName , passWord):

    sql = getConnection()
    selectQuery = f"SELECT * FROM clientuser WHERE Email = '{userName}' AND Password = '{passWord}';"
    sql.execute(selectQuery)
    queryResult = sql.fetchone()
    # print(queryResult)
    if queryResult == None:
        return (queryResult,f"Invalid Email or Password")
    else:
        return (queryResult , f'Welcome {userName}')
    
def getClientUsername(userId):
    sql = getConnection()
    selectQuery = f"SELECT concat(first_name,' ',last_name) as name FROM clientuser WHERE userId = '{userId}';"
    sql.execute(selectQuery)
    queryResult = sql.fetchone()
    if queryResult == None:
        return (None)
    else:
        return (queryResult)
    

def getClientUserIDDfromToken(token):
    sql = getConnection()

    selectQuery = f"SELECT clientUserId FROM clientuser WHERE token = '{token}';"
    sql.execute(selectQuery)
    queryResult = sql.fetchone()
    if queryResult == None:
        return [None,0]
    else:
        return (queryResult)