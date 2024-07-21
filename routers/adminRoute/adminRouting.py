from django.contrib import admin
from django.urls import path 
from controller.opsControllers.opsLoginController import opsLoginPage
from controller.opsControllers.forgotPasswordController import getForgotPassword
from controller.opsControllers.fileUploadingController import ImportDocx
from authentication.authenticator import getOpsTokenFromCookie
from controller.forbiddenController import forbiddenPage


configureAdminRoutes = [{
    'path': 'opsLogin',
    'controller': opsLoginPage,
    'name': 'Operational login',
    'csrf': False,
    'pageType': 'public'
},{
    'path': 'forgotPassword',
    'controller': getForgotPassword,
    'name': 'ops Forgot Password',
    'csrf': False,
    'pageType': 'public'
},{
    'path': 'uploadDoc',
    'controller': ImportDocx,
    'name': 'Upload document',
    'csrf': False,
    'pageType': 'private'
},]



def createRoute(obj):
    if obj['pageType'] == "public":
        return path(obj["path"] , obj['controller'] , name=obj['name'])
        
    elif obj['pageType'] == "private":
        # userId  = getTokenFromCookie(obj['path'])
        # print(userId)
        return path(obj["path"] , getOpsTokenFromCookie(obj['controller']) , name=obj['name'])

adminUrlPatterns = []

for urlIteator in configureAdminRoutes:
    adminUrlPatterns.append(createRoute(urlIteator))
    

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('opsLogin/', opsLoginPage , name="Operational login"),
#     path("forgotPassword/", getForgotPassword, name="forgot password"),
#     path("uploadDoc/", ImportDocx, name="Upload document"),
    

# ]