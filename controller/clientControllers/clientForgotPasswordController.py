import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from query.forgotQuery import updatePassword , forgotOtpGeneration ,otpValidation
from query.userQuery import getUsername
from helper.optGenerator import __getOTP
from helper.encryption import __encryptorMD5
from helper.userID import __getUserID

from django.shortcuts import render
def getForgotPassword(request):

    csrf_token = 'bfbff' 
    emailStatus = ["",""]
    otpStatus = ["",""]
    updatePasswordStatus = ["",""]
    otp = ""
    email = ""
    if request.method == 'POST':
        email = request.POST['email']
        try:
            otp = request.POST['otp']
            password = __encryptorMD5(request.POST["newPassword"])
        except:
            print("except--------------",email)
        
        try:
            emailStatus = __getUserID(email)
            userName = getUsername(emailStatus[1])
            
            # print(emailStatus,"11111111111111111",userName)
            

            tableUpdateStatus = forgotOtpGeneration(emailStatus , __getOTP())

            # print(tableUpdateStatus,"22222222222222222")
            

            if tableUpdateStatus > 0:
                otpStatus = otpValidation(emailStatus[1] , otp)
                print("-------------otp" , otpStatus)
                if otpStatus[0] == True:
                    updatePasswordStatus = updatePassword(emailStatus[1],password)
                    print("--------updatepassresult",updatePasswordStatus)
                
        except:
            print("except block")


    return render (request , 'forgotPassword.html',{
        "email_status" :emailStatus,
        'emailAddress' : email,
        "otp" : otp,
        "otp_status":otpStatus,
        "pass_status":updatePasswordStatus
    })