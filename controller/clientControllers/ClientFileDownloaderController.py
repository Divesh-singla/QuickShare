from django.shortcuts import render
from query.fileMetaDataQuery import getAllFileDetails,getFilesByFileID
from query.userQuery import getClientUserIDDfromToken
from query.FileAccessTableQuery import getfileAccessDetails
from constant.settings import tokenName


def clientFileDownloader(request):

    entireFileList = ""
    cookieToken = request.COOKIES[tokenName]

    clientUserId = (getClientUserIDDfromToken(cookieToken))[0]
    fileIds = getfileAccessDetails(clientUserId)
    
    entireFileList = getFilesByFileID(fileIds)


    # print(fileIds)




    if request.method == "POST":


        cookieToken = request.COOKIES[tokenName]

        # entireFileList = getAllFileDetails()

    return render (request, "fileList.html",{
        "file_data" : entireFileList
    })
