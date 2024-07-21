import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from helper.tableDetails import __getSchoolTableDetails
def __getSortedData(field , data , sortingType):

    if sortingType == "ASC" or sortingType == 'asc':

        for firstIterator in range(len(data)):
            for secondIterator in range (0,len(data)-firstIterator-1):

                if data[secondIterator][f'{field}'] >= data[secondIterator+1][f'{field}']:
                        data[secondIterator] , data[secondIterator+1] = data[secondIterator+1] , data[secondIterator]
                        
        return data

    elif sortingType == "DESC" or sortingType == 'desc':

        for firstIterator in range(len(data)):
            for secondIterator in range (0,len(data)-firstIterator-1):

                if data[secondIterator][f'{field}'] <= data[secondIterator+1][f'{field}']:
                    data[secondIterator] , data[secondIterator+1] = data[secondIterator+1] , data[secondIterator]

        return data
