def __getUniqueList(data):
    uniqueList = []

    for dataIterator in data:
        duplicateStatus = False
        for uniqueIterator in uniqueList:
            
            if uniqueIterator == dataIterator:
                duplicateStatus = True
        if duplicateStatus == False:
            uniqueList.append(dataIterator)
    return uniqueList

# print(__getUniqueList([1,1,1,14,2,1,5,3]))