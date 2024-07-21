from django.contrib import admin
from django.urls import path 
from controller.clientControllers.clientLoginController import clientLoginPage
from controller.clientControllers.clientForgotPasswordController import getForgotPassword
from controller.clientControllers.ClientFileDownloaderController import clientFileDownloader
from controller.clientControllers.clientSignupController import clientSignUp
from authentication.authenticator import getClientTokenFromCookie
from controller.forbiddenController import forbiddenPage


configureClientRoutes = [{
    'path': 'Login',
    'controller': clientLoginPage,
    'name': 'client login',
    'csrf': False,
    'pageType': 'public'
},{
    'path': 'Signup',
    'controller': clientSignUp,
    'name': 'client SignUp',
    'csrf': False,
    'pageType': 'public'
},{
    'path': 'forgotPassword',
    'controller': getForgotPassword,
    'name': 'client Forgot Password',
    'csrf': False,
    'pageType': 'public'
},{
    'path': 'downloadFiles',
    'controller': clientFileDownloader,
    'name': 'client file download',
    'csrf': False,
    'pageType': 'private'
}]



def createRoute(obj):
    if obj['pageType'] == "public":
        return path(obj["path"] , obj['controller'] , name=obj['name'])
        
    elif obj['pageType'] == "private":
        # userId  = getTokenFromCookie(obj['path'])
        # print(userId)
        return path(obj["path"] , getClientTokenFromCookie(obj['controller']) , name=obj['name'])

clientUrlPatterns = []

for urlIteator in configureClientRoutes:
    clientUrlPatterns.append(createRoute(urlIteator))
