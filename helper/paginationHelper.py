def __paginationPaging(dataLength , dataPerPage , currentUrl):

    totalPages = round((dataLength/dataPerPage)+0.5)
    pageList = []
    for pages in range (1,totalPages+1):
        pageDict = {
            'pages' : pages,
            "url" : currentUrl
        }
        pageList.append(pageDict)

    return pageList


def __getPageLimit(perPageData , pageNo , totalPages):

    if pageNo == None  or pageNo == "first" or (pageNo) == '1':
        lowerLimit = 0
        # upperLimit = perPageData
        return [lowerLimit , perPageData]

    elif pageNo == "last":

        lowerLimit = (int(totalPages)-1)*perPageData
        return [lowerLimit , perPageData]

    elif int(pageNo) > 1 :
        lowerLimit = (int(pageNo)-1)*perPageData
        # upperLimit = int(pageNo)*perPageData
        return [lowerLimit , perPageData]

    



