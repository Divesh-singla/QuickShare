from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from constant.path import filePath
from mysqlConnection.connection import getConnection
from query.fileMetaDataQuery import insertFileMetadata
import os
from datetime import datetime
from helper.fileSizeConverter import __getConvertedFileSize

total_row_updated = 0

def ImportDocx(request):
    # get cookie 
    
    page = (request.get_full_path())
    upload_status = [99,""]
    result = 99
    fileUrl=""
    fileName = ""
    
    csrf_token = 'bfbff'

    read = False
    # set id and downloading uploaded file
    if request.method == 'POST':
        
        read = True


        filecontainer = request.FILES['file_upload']
        # fs = FileSystemStorage(location=r"/static/upload")

        # fs = FileSystemStorage(location=filePath)
        fs = FileSystemStorage()
        # fs = FileSystemStorage(location=r"/app/static/upload")
        baseName = filecontainer.name
        

        if fs.exists(filecontainer.name)==False:
            fileName = fs.save(baseName, filecontainer)
     
            fileUrl = fs.url(fileName)
            fileSize = __getConvertedFileSize(fs.size(fileName))
            fileDate = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            # print(fileDate)
            # fileDate = str(fs.get_created_time(fileName))[:-13]

            result = 1

        else:
            fs.delete(filecontainer.name)

            fileName = fs.save(baseName, filecontainer)

            fileUrl = fs.url(fileName)
            fileSize = __getConvertedFileSize(fs.size(fileName))
            fileDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            # fileDate = (str(fs.get_created_time(fileName))[:-13])
            # print(fileUrl,"1111111111")

            result = 2

            # print("file already exist")
        # print(baseName)
        if result!=99:
            upload_status = (insertFileMetadata(fileName,fileUrl,fileSize,fileDate))



        # checking if docx file contains error or not


    response = render(request, 'fileUpload.html', {
        'title' : 'Import Docx',
        'result': upload_status[0],
        "message" : upload_status[1],
        "fileurl":fileUrl,
        "filename":fileName
    })
    return response