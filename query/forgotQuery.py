import sys
from mysqlConnection.connection import getConnection
from helper.encryption import __encryptorMD5
from helper.userID import __getUserID
from helper.tableDetails import __getUserDetails

sql = getConnection()



#generates otp for password recovery
def forgotOtpGeneration(emailExistsStatus,otp):
    """Takes Two Parameters i.e status of email Address exists or not in db and the OTP for the recovery\nstatus should be on zeroth Index (True or false) And email Should be on first index"""
    if emailExistsStatus[0] == True:
        # otpCheckQuery = F"SELECT otp FROM user WHERE userId = {emailExistsStatus[1]}"
        # sql.execute(otpCheckQuery)
        # otpCheckResult = sql.fetchone()

        otpDb = (__getUserDetails(emailExistsStatus[1]).get('otp'))

        if otpDb == "" or otpDb == 'Null':
            otpGenerationQuery = f'UPDATE user SET otp = "{otp}" WHERE userId = {emailExistsStatus[1]}' 
            sql.execute(otpGenerationQuery)
            otpGenerationResult = sql.rowcount
            return otpGenerationResult
        
        elif otpDb != "" or otpDb != "Null":
            return 2


       

def otpValidation(userId,otp):
    # otpQueryDb = f"SELECT otp FROM user WHERE userId = '{userId}'"
    # sql.execute(otpQueryDb)
    # otpResult = sql.fetchone()

    otpDb = __getUserDetails(userId).get('otp')

    if otp != "":
        if otpDb == otp:
            return [True , "OTP Verified"]

        elif  otpDb != otp:
            return [False,"OTP Not Verified"]

    

# updates Password 
def updatePassword(userId , newPassword):
    """Takes Two Parameters i.e Email Address and New Password"""

    # otpQueryDb = f"SELECT otp FROM user WHERE userId = '{userId}'"
    # sql.execute(otpQueryDb)
    # otpResult = sql.fetchone()

    otpDb = __getUserDetails(userId).get('otp')

    # extractingPassword = f"SELECT password FROM user WHERE userId = '{userId}'"
    # sql.execute(extractingPassword)
    # oldPassResult = sql.fetchone()

    passwordDb = __getUserDetails(userId).get('password')


    if otpDb != None:
        updatePassQuery = f"UPDATE user SET password = '{newPassword}' WHERE userId = '{userId}'"
        sql.execute(updatePassQuery)
        updatePassResult = sql.rowcount

        if updatePassResult > 0:
            updateOtpQuery = f"UPDATE user SET otp = 'Null' WHERE userId = '{userId}' "
            sql.execute(updateOtpQuery)
            deleteResult = sql.rowcount
            # print('-----------deletequery',deleteResult)
            return [True,"Password Changed Successfully"]

        elif newPassword == passwordDb:
            return [False,"New Password & Old Password Can't be Same!"]
