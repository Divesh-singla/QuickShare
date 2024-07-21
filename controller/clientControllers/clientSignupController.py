import sys
sys.path.insert(0,r'S:\ACIL\project\attendanceCRM')
from django.shortcuts import render
from query.ClientQuery import addClientQuery
from helper.encryption import __encryptorMD5
from helper.tableDetails import __getUserDetails
from helper.validation import __validationDb
from helper.removeDuplicate import __getUniqueList
from helper.tokenHelper import __generateToken


def clientSignUp(request,access=""):

    firstName = ""
    lastName = ""
    email = ""
    password = ""
    userName = ""

    result = ["", ""]
    urlType = request.GET.get("type")
    userId = request.GET.get("userId")

    if urlType == "edit" :
        firstName = __getUserDetails(userId).get("first_name")
        lastName = __getUserDetails(userId).get("last_name")
        userName = __getUserDetails(userId).get("user_name")
        email = __getUserDetails(userId).get("email")


    if request.method == 'POST':
        firstName = request.POST['first-name']
        lastName = request.POST['last-name']
        email = request.POST['email']
        userName = request.POST['username']

        if urlType == "edit":
            password = None
        else:
            password =  __encryptorMD5(request.POST['new-password']) 
        # result = addUserQuery(firstName , lastName , email , userName , password )
            token = __generateToken(password)
        validateResult1= __validationDb("email" ,'clientuser' , email, 'clientUserId' , userId, urlType) 
        validateResult2 =  __validationDb("user_name" ,'clientuser' , userName, 'clientUserId' , userId, urlType)

        print(validateResult1,validateResult2,"1111111111111")
        # print(s)
        if validateResult1[0]  and  validateResult2[0]:
            result = addClientQuery(firstName , lastName , email , userName , password ,token , urlType , userId)
        elif validateResult1[0] == False:
            result = [False , validateResult1[1]]
        elif validateResult2[0] == False:
            result = [False , validateResult2[1]]



    return render(request , "clientSignupPage.html" ,{
       'first_name': firstName ,
       'last_name': lastName ,
       'email_address': email ,
       'password': password, 
       'user_name': userName ,
       'status' : result,
       "urlType":urlType,
    })
