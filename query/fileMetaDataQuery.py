import sys
from mysqlConnection.connection import getConnection
from constant.message import FAILURE, SUCCESS, ALREADYEXIST,get_message

sql = getConnection()


def insertFileMetadata(fileName, filePath, fileSize, fileDate):

    upload_status = [99,""]
    
    checkFileQuery = f'SELECT * FROM fileinfo WHERE fileName = "{fileName}"'
    sql.execute(checkFileQuery)
    checkFileQueryResult = sql.fetchone()

    if checkFileQueryResult==None:
        InsertFileQuery = f"INSERT INTO fileinfo (fileName,fileLink,size,date) VALUES ('{fileName}','{filePath}','{fileSize}','{fileDate}')"
        sql.execute(InsertFileQuery)
        InsertFileQueryResult = sql.rowcount
        
        if InsertFileQueryResult>0:
            upload_status = [1,""]
        else:
            upload_status = [99,""]

    else:
        updateFileQuery = f"UPDATE fileinfo SET fileLink='{filePath}' ,size='{fileSize}',date='{fileDate}' WHERE fileName='{fileName}'"
        sql.execute(updateFileQuery)
        updateFileQueryResult = sql.rowcount

        if updateFileQueryResult>0:
            
            upload_status = [2,""]
        else:
            upload_status = [99,""]

    if upload_status[0] == 1:
        result = [1,get_message(SUCCESS)]
    elif upload_status[0] == 2:
        result = [2,get_message(ALREADYEXIST)]
        
    elif upload_status[0] == 99:
        result = [99,get_message (FAILURE)]   

    return(result)


def getAllFileDetails():

    getFileQuery="SELECT * FROM fileinfo"
    sql.execute(getFileQuery)
    getFileQueryResult=sql.fetchall()
    return getFileQueryResult

def getFilesByFileID(fileId):
    if type(fileId)==tuple:
        fileIdOnlyList = []

        for x in fileId:
            fileIdOnlyList.append(str(x[0]))

        finalIds = '","'.join(fileIdOnlyList)

        getFilesQuery = f'SELECT * FROM fileinfo WHERE file_id IN ("{finalIds}") and status="ON"'
        sql.execute(getFilesQuery)
        getFilesQueryResult=sql.fetchall()
        return getFilesQueryResult
    else:
        return ""





