import sys
from django.shortcuts import render,redirect
from query.userQuery import validateUser
from helper.validation import __emailValidator
from helper.encryption import __encryptorMD5
from helper.tokenHelper import __getTokenFromDb
from django.http import HttpResponseRedirect
from constant.settings import tokenName
from helper.logout import __logOut

def opsLoginPage(request):
    csrf_token = 'bfbff'
    loginStatus = [0,""]
    token = ["",""]

    if request.method == "POST":
        email = (request.POST['email'])
        password = __encryptorMD5((request.POST ["password"]))
        
        
        if __emailValidator(email) :
            loginStatus = validateUser(email , password)
            token = __getTokenFromDb(email ,  'user' , 'token' , 'email')
            
        else:
            loginStatus = [0 , "Invalid Email"]
        # print(loginStatus,'11/111111111111111111\n',loginStatus[1])    
    response =  render(request, "opsLoginPage.html", {
        "login_message" : loginStatus[1],
        "login_status" : loginStatus[0]
    })

    if loginStatus[0]:

        response.set_cookie(tokenName,f'{token[1]}')
        # print((tokenName,f'{token[1]}-------------------------------'))

        # print(request.COOKIES.get(tokenName) , "getcokkeeeeeeee")
        # if request.COOKIES.get(tokenName):
            # print("token")
        # print(request.COOKIES.get(tokenName) , "getcokkeeeeeeee") 
        # return HttpResponseRedirect('/admin/schoolListing')
        # request.delete_cookie(tokenName)    

        # logOut('user' , 'Token' , request.COOKIES.get(tokenName) , response)



    return response
