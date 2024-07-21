import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from mysqlConnection.connection import getConnection
sql = getConnection()

# checks email Exists or not in DB
def __getUserID(emailAddress): 
    """Takes 1 parameter which is Email Address \nreturns True & userid for if email Exists, Return False & error message if email not exists """
    forgotQuery = f"SELECT userId FROM user WHERE Email = '{emailAddress}'"
    sql.execute(forgotQuery)
    userIdResult = sql.fetchone()

    if userIdResult != None:
        return [True,userIdResult[0]]

    else :
        return [False,'Email not exists']

