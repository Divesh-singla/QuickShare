import sys
from django.shortcuts import render,redirect
from query.userQuery import validateClientUser
from helper.validation import __emailValidator
from helper.encryption import __encryptorMD5
from helper.tokenHelper import __getTokenFromDb
from django.http import HttpResponseRedirect
from constant.settings import tokenName
from helper.logout import __logOut

def clientLoginPage(request):
    csrf_token = 'bfbff'
    loginStatus = [0,""]
    token = ["",""]

    if request.method == "POST":
        email = (request.POST['email'])
        password = __encryptorMD5((request.POST ["password"]))
        
        
        if __emailValidator(email) :
            loginStatus = validateClientUser(email , password)
            token = __getTokenFromDb(email ,  'clientuser' , 'token' , 'email')
        
            
        else:
            loginStatus = [0 , "Invalid Email"]
        
        
    response =  render(request, "clientLoginPage.html", {
        "login_message" : loginStatus[1],
        "login_status" : loginStatus[0]
    })

    if loginStatus[0]:
    
        response.set_cookie(tokenName,f'{token[1]}')


    return response
