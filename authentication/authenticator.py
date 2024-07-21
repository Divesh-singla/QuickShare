from cgitb import reset
import sys
from django.shortcuts import render
from mysqlConnection.connection import getConnection
from django.http import HttpResponseRedirect
from constant.settings import tokenName
from django.urls import resolve
sql = getConnection()

def getOpsTokenFromCookie(getResponse):
    
    # time.sleep(1)
    def middleWare(request):
        userIdResult = ""
        tokenResult = ""
        moduleIdResult = ""
        userID = ""
        
        try:
            cookieToken = request.COOKIES[tokenName]
            
            moduleName = resolve(request.path_info).url_name  
            moduleIdQuery = f"SELECT moduleId FROM modules WHERE module_name = '{moduleName}'"
            sql.execute(moduleIdQuery)
            moduleIdResult = sql.fetchone()[0]
            # print(moduleIdResult)
            

            userIdTokenQuery = f"SELECT userId , token , role FROM user WHERE token = '{cookieToken}' "
            sql.execute(userIdTokenQuery)
            userIdResult = sql.fetchone()[0]
            tokenResult = sql.fetchone()[1]
            # userID = sql.fetchone()[2]

        except:
            cookieToken = None         

        # print(moduleIdResult,"1111111111111110000000000000")
        # print(userID)
        if moduleIdResult:
            cookieToken = request.COOKIES[tokenName]
            userIDQuery = f"SELECT userId FROM user WHERE token = '{cookieToken}' "
            sql.execute(userIDQuery)
            userID = sql.fetchone()[0]
            # print(userID,"111111111111")

            checkQuery = f"SELECT moduleId FROM newModuleaccess WHERE opsUserId = '{userID}' AND moduleId = '{moduleIdResult}'"
            sql.execute(checkQuery)
            checkResult = sql.fetchone()
            # print(checkResult,"eres")
            if checkResult == None :
                return HttpResponseRedirect('/forbidden')
                # return response



        if userIdResult:
            return getResponse(request)

            
        if tokenResult != cookieToken :
            response = HttpResponseRedirect('/admin/opsLogin')
            response.delete_cookie(tokenName)
            return response



        return HttpResponseRedirect('/admin/opsLogin')
        
    return middleWare




def getClientTokenFromCookie(getResponse):
    
    # time.sleep(1)
    def middleWare(request):
        userIdResult = ""
        tokenResult = ""
        moduleIdResult = ""
        userID = ""
        
        try:
            cookieToken = request.COOKIES[tokenName]
            
            moduleName = resolve(request.path_info).url_name  
            moduleIdQuery = f"SELECT moduleId FROM modules WHERE module_name = '{moduleName}'"
            sql.execute(moduleIdQuery)
            moduleIdResult = sql.fetchone()[0]
            

            userIdTokenQuery = f"SELECT clientUserId , token , clientRole FROM clientuser WHERE token = '{cookieToken}' "
            sql.execute(userIdTokenQuery)
            userIdResult = sql.fetchone()[0]
            tokenResult = sql.fetchone()[1]
            # userID = sql.fetchone()[2]

        except:
            cookieToken = None         


        if moduleIdResult:
            cookieToken = request.COOKIES[tokenName]
            userIDQuery = f"SELECT clientUserId FROM clientuser WHERE token = '{cookieToken}' "
            sql.execute(userIDQuery)
            userID = sql.fetchone()[0]
            

            checkQuery = f"SELECT moduleId FROM newModuleaccess WHERE clientUserId = '{userID}' AND moduleId = '{moduleIdResult}'"
            sql.execute(checkQuery)
            checkResult = sql.fetchone()
            # print(checkResult,"eres")
            if checkResult == None :
                return HttpResponseRedirect('/forbidden')
                # return response



        if userIdResult:
            return getResponse(request)

        
        if tokenResult != cookieToken :
            response = HttpResponseRedirect('/client/Login')
            response.delete_cookie(tokenName)
            return response



        return HttpResponseRedirect('/client/Login')
        
    return middleWare


    # token = request.COOKIES['Token']
    # # token = HttpResponse

    # tokenQuery = f"SELECT userId from user WHERE token = '{token}' "
    # sql.execute(tokenQuery)
    # tokenResult = sql.fetchone()
    # if tokenResult:
    #     return tokenResult[0]
    # return request

# print("11111111111111",getTokenFromCookie)
