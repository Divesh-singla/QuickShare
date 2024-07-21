import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from mysqlConnection.connection import getConnection
from helper.tableDetails import __getUserDetails

sql = getConnection()

# def getMyAccountDetails(firstName , lastName , userName , email , userid):
#     detailQuery = f"SELECT * FROM user WHERE userId = '{userid}'"
#     sql.execute(detailQuery)
#     detailResult = sql.fetchone()

#     detailList = []
#     detailList.append(detailResult[1])
#     detailList.append(detailResult[2])
#     detailList.append(detailResult[4])
#     detailList.append(detailResult[3])

#     if (firstName != detailList[0]):
#         firstNameUpdateQuery = f"UPDATE user SET first_name = '{firstName}' WHERE userId = '{userid}'"
#         sql.execute(firstNameUpdateQuery)
#         firstNameUpdateResult = sql.rowcount
#         if firstNameUpdateResult >0:
#             return [True , "First Name Changed"]

#     if (firstName == detailList[0]):
#         return [False , "Nothing to Update in First Name"]

#     if (lastName != detailList[1]):
#         lastNameUpdateQuery = f"UPDATE user SET last_name = '{lastName}' WHERE userId = '{userid}'"
#         sql.execute(lastNameUpdateQuery)
#         lastNameUpdateResult = sql.rowcount
#         if lastNameUpdateResult >0:
#             return [True , "Last Name Changed"]

#     if (lastName == detailList[1]):
#         return [False , "Nothing to Update in Last Name"]

#     if (userName != detailList[2]):
#         userNameUpdateQuery = f"UPDATE user SET user_name = '{userName}' WHERE userId = '{userid}'"
#         sql.execute(userNameUpdateQuery)
#         userNameUpdateResult = sql.rowcount
#         if userNameUpdateResult > 0:
#             return [True , "User Name Changed"]
    
#     elif (userName == detailList[2]):
#         return [False , "Nothing to Update in User Name"]

#     if (email != detailList[2]):
#         emailUpdateQuery = f"UPDATE user SET email = '{email}' WHERE userId = '{userid}'"
#         sql.execute(emailUpdateQuery)
#         emailUpdateResult = sql.rowcount
#         if emailUpdateResult > 0:
#             return [True , "Email Changed"]
    
#     elif (userName == detailList[2]):
#         return [False , "Nothing to Update in Email"]


def updateFirstName(firstName , userId):
    firstNameDb = __getUserDetails(userId).get('first_name')
    # print(firstNameDb)
    if (firstName != firstNameDb):
        firstNameUpdateQuery = f"UPDATE user SET first_name = '{firstName}' WHERE userId = '{userId}'"
        sql.execute(firstNameUpdateQuery)
        firstNameUpdateResult = sql.rowcount
        if firstNameUpdateResult >0:
            return [True , "First Name Changed"]

    if (firstName == firstNameDb):
        return [False , "Nothing to Update in First Name"]

def updateLastName(lastName , userId):
    lastNameDb = __getUserDetails(userId).get('last_name')

    if (lastName != lastNameDb):
        lastNameUpdateQuery = f"UPDATE user SET last_name = '{lastName}' WHERE userId = '{userId}'"
        sql.execute(lastNameUpdateQuery)
        lastNameUpdateResult = sql.rowcount
        if lastNameUpdateResult >0:
            return [True , "Last Name Changed"]

    if (lastName == lastNameDb):
        return [False , "Nothing to Update in Last Name"]

def updateUserName(userName , userId):
    userNameDb = __getUserDetails(userId).get('user_name')

    if (userName != userNameDb):
        userNameUpdateQuery = f"UPDATE user SET user_name = '{userName}' WHERE userId = '{userId}'"
        sql.execute(userNameUpdateQuery)
        userNameUpdateResult = sql.rowcount
        if userNameUpdateResult >0:
            return [True , "User Name Changed"]

    if (userName == userNameDb):
        return [False , "Nothing to Update in User Name"]

def updateEmail(email , userId , tableName , emailFieldName , userIdFieldName):
    emailDb = __getUserDetails(userId).get('email')

    if (email != emailDb):
        emailUpdateQuery = f"UPDATE {tableName} SET {emailFieldName} = '{email}' WHERE {userIdFieldName} = '{userId}'"
        sql.execute(emailUpdateQuery)
        emailUpdateResult = sql.rowcount
        if emailUpdateResult >0:
            return [True , "Email Changed"]

    if (email == emailDb):
        return [False , "Nothing to Update in Email"]
