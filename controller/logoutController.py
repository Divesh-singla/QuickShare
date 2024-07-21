import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from django.http import HttpResponseRedirect
from tokenize import Token
from constant.settings import tokenName
from helper.logout import __logOut

def logoutController(request):

    token = request.COOKIES.get(tokenName)
    
    __logOut("user" , "Token" , token )
    response = HttpResponseRedirect("/admin/login")

    return response