import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from helper.tableDetails import __getSchoolTableDetails


class __searchFunction() :
    
    def __init__(self , keyWord , data , fields):
            self.keyWord = keyWord.lower()
            self.data = data
            self.founded_elements = []
            self.splitted_search = (self.keyWord).split(" ")
            self.fields = []
            for key,value in fields.items():
                if value == True:
                    self.fields.append(key)
        
    def accurate_match(self):
            
        for fieldsIterator in self.fields:

            for keyIterator in self.data:
                searchIterator = keyIterator[fieldsIterator].lower()
                if searchIterator.find(self.keyWord) >= 0:
                    self.founded_elements.append(keyIterator)
        return (self.founded_elements)

    
    def phraseSearch(self):
        
        count = 0
        for keywordIterator in self.splitted_search:
            count += 1
            x = [] or self.data
            print(len(x))
            
            if count > 1:
                x = self.founded_elements
                self.founded_elements = []

            for dataIterator in x:
                for fieldIterator in self.fields:
                    if (dataIterator[fieldIterator].lower()).find(keywordIterator) >= 0:
                            self.founded_elements.append(dataIterator)
            x = self.founded_elements

        
        return self.founded_elements

    
    def getSearch(self):
        # if len(self.splitted_search) <= 1:
        return self.accurate_match()
        return self.phraseSearch()


def __dateSearch(fromdate, todate , data , keyword):
    seached = []
    for dataIterator in data:
        if str(dataIterator.get(keyword)) >= fromdate and str(dataIterator.get('date_time')) <= todate:
            seached.append(dataIterator)
    return seached


# print(dateSearch('2022-05-02' ,'2022-05-04',__getSchoolTableDetails()))

# dateSearch( , )