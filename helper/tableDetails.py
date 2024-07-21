import sys

from matplotlib.style import use
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from mysqlConnection.connection import getConnection
sql = getConnection()

def __getUserDetails(userId="" , lowerLimit = "" , dataDistribution = ""):
    if userId :
        accountDetailQuery = f"SELECT * FROM user WHERE userId = '{userId}'"
        sql.execute(accountDetailQuery)
        accountDetailResult = sql.fetchone()
        accountDetailDict = {
            'userId' : accountDetailResult[0],
            'first_name' : accountDetailResult[1],
            'last_name' : accountDetailResult[2],
            'email' : accountDetailResult[3],
            'user_name' : accountDetailResult[4],
            'password' : accountDetailResult[5],
            'token' : accountDetailResult[6],
            'otp':accountDetailResult[7],
            'date_time':accountDetailResult[8],
            'role' : accountDetailResult[9],
            'status' : accountDetailResult[10]
        }
        return accountDetailDict
        

    elif all([userId == "" , lowerLimit == "" , dataDistribution == ""]):
        accountDetailQuery = f"SELECT * FROM user"
        sql.execute(accountDetailQuery)
        accountDetailResult = sql.fetchall()
        # print(tableDetailResult)
        accountDetailsList = []
        for detailIterator in accountDetailResult:
            detailDict = {
            'userId' : detailIterator[0],
            'first_name' : detailIterator[1],
            'last_name' : detailIterator[2],
            'email' : detailIterator[3],
            'user_name' : detailIterator[4],
            'password' : detailIterator[5],
            'token' : detailIterator[6],
            'otp':detailIterator[7],
            "date_time":detailIterator[8],
            "role" : detailIterator[9],
            'status' : detailIterator[10]
            }
            accountDetailsList.append(detailDict)
        return accountDetailsList

    elif all([userId == "" , lowerLimit != "" , dataDistribution != "" ]):
        accountDetailQuery = f"SELECT * FROM user LIMIT {lowerLimit} , {dataDistribution}"
        sql.execute(accountDetailQuery)
        accountDetailResult = sql.fetchall()
        # print(tableDetailResult)
        accountDetailsList = []
        for detailIterator in accountDetailResult:
            detailDict = {
            'userId' : detailIterator[0],
            'first_name' : detailIterator[1],
            'last_name' : detailIterator[2],
            'email' : detailIterator[3],
            'user_name' : detailIterator[4],
            'password' : detailIterator[5],
            'token' : detailIterator[6],
            'otp':detailIterator[7],
            "date_time":detailIterator[8],
            "role" : detailIterator[9],
            'status' : detailIterator[10]
            }
            accountDetailsList.append(detailDict)
        return accountDetailsList


def __getSchoolTableDetails(schoolId = "" , pageSlug = "" , lowerLimit = "" , dataDistribution = ""):
    if schoolId:
        tableDetailQuery = f"SELECT * FROM schooldetails WHERE school_id = '{schoolId}'"
        sql.execute(tableDetailQuery)
        tableDetailResult = sql.fetchone()
        tableDetailDict = {
            "school_id" : tableDetailResult[0],
            "school_name" : tableDetailResult[1],
            "school_affiliation" : tableDetailResult[2],
            "state" : tableDetailResult[3],
            "district" : tableDetailResult[4],
            "postal_address" : tableDetailResult[5],
            "city" : tableDetailResult[6],
            "tehsil" : tableDetailResult[7],
            "pincode" : tableDetailResult[8],
            "mobile_no" : tableDetailResult[9],
            "fax_no" : tableDetailResult[10],
            "email" : tableDetailResult[11],
            "running_class" : tableDetailResult[12],
            "noc_no" : tableDetailResult[13],
            'licence_no' : tableDetailResult[14],
            'affiliation_no' : tableDetailResult[15],
            "date_time" : tableDetailResult[16],
            "status" : tableDetailResult[17],
            "order" : tableDetailResult[18],
            "page_slug" : tableDetailResult[19],
        }
        return tableDetailDict

    elif pageSlug:
        tableDetailQuery = f"SELECT * FROM schooldetails WHERE page_slug = '{pageSlug}'"
        sql.execute(tableDetailQuery)
        tableDetailResult = sql.fetchone()
        tableDetailDict = {
            "school_id" : tableDetailResult[0],
            "school_name" : tableDetailResult[1],
            "school_affiliation" : tableDetailResult[2],
            "state" : tableDetailResult[3],
            "district" : tableDetailResult[4],
            "postal_address" : tableDetailResult[5],
            "city" : tableDetailResult[6],
            "tehsil" : tableDetailResult[7],
            "pincode" : tableDetailResult[8],
            "mobile_no" : tableDetailResult[9],
            "fax_no" : tableDetailResult[10],
            "email" : tableDetailResult[11],
            "running_class" : tableDetailResult[12],
            "noc_no" : tableDetailResult[13],
            'licence_no' : tableDetailResult[14],
            'affiliation_no' : tableDetailResult[15],
            "date_time" : tableDetailResult[16],
            "status" : tableDetailResult[17],
            "order" : tableDetailResult[18],
            "page_slug" : tableDetailResult[19],
        }
        return tableDetailDict

   
    elif all([schoolId == "", pageSlug == "" ,lowerLimit == "" , dataDistribution == "" ]):

        tableDetailQuery = f"SELECT * FROM schooldetails"
        sql.execute(tableDetailQuery)
        tableDetailResult = sql.fetchall()
        completeDetailsList = []
        for detailIterator in tableDetailResult:
            tableDetailDict = {
            "school_id" : detailIterator[0],
            "school_name" : detailIterator[1],
            "school_affiliation" : detailIterator[2],
            "state" : detailIterator[3],
            "district" : detailIterator[4],
            "postal_address" : detailIterator[5],
            "city" : detailIterator[6],
            "tehsil" : detailIterator[7],
            "pincode" : detailIterator[8],
            "mobile_no" : detailIterator[9],
            "fax_no" : detailIterator[10],
            "email" : detailIterator[11],
            "running_class" : detailIterator[12],
            "noc_no" : detailIterator[13],
            'licence_no' : detailIterator[14],
            'affiliation_no' : detailIterator[15],
            "date_time" : detailIterator[16],
            "status" : detailIterator[17],
            "order" : detailIterator[18],
            "page_slug" : detailIterator[19],

            }
            completeDetailsList.append(tableDetailDict)
        return  completeDetailsList

    elif all([schoolId == "" , pageSlug == "" , lowerLimit != "" , dataDistribution != "" ]):
        tableDetailQuery = f"SELECT * FROM schooldetails LIMIT {lowerLimit} , {dataDistribution}"
        print(tableDetailQuery)
        sql.execute(tableDetailQuery)
        tableDetailResult = sql.fetchall()
        completeDetailsList = []
        for detailIterator in tableDetailResult:
            tableDetailDict = {
            "school_id" : detailIterator[0],
            "school_name" : detailIterator[1],
            "school_affiliation" : detailIterator[2],
            "state" : detailIterator[3],
            "district" : detailIterator[4],
            "postal_address" : detailIterator[5],
            "city" : detailIterator[6],
            "tehsil" : detailIterator[7],
            "pincode" : detailIterator[8],
            "mobile_no" : detailIterator[9],
            "fax_no" : detailIterator[10],
            "email" : detailIterator[11],
            "running_class" : detailIterator[12],
            "noc_no" : detailIterator[13],
            'licence_no' : detailIterator[14],
            'affiliation_no' : detailIterator[15],
            "date_time" : detailIterator[16],
            "status" : detailIterator[17],
            "order" : detailIterator[18],
            "page_slug" : detailIterator[19],

            }
            completeDetailsList.append(tableDetailDict)
        return  completeDetailsList


def __getState():
    stateFetchQuery = f"SELECT state_id , state_title FROM state"
    sql.execute(stateFetchQuery)
    stateFetchResult = sql.fetchall()
    # print(stateFetchResult)
    stateList = []
    for details in stateFetchResult:
        stateDict = {
            'state_id' : str(details[0]),
            'state_name' : details[1]
        }
        stateList.append(stateDict)
    return stateList

def __getDistrict(stateId = ""):
    if stateId == "":
        districtQuery = f"SELECT districtid , district_title FROM district"
        sql.execute(districtQuery)
        districtResult = sql.fetchall()
        districtList = []
        for districtIterator in districtResult:
            districtDict = {
                'district_id': str(districtIterator[0]),
                'district_name' : districtIterator[1]
            }
            districtList.append(districtDict)
        return districtList

    else:
        districtQuery = f"SELECT districtid , district_title FROM district WHERE state_id = '{stateId}' "
        sql.execute(districtQuery)
        districtResult = sql.fetchall()
        districtList = []
        for districtIterator in districtResult:
            districtDict = {
                'district_id': str(districtIterator[0]),
                'district_name' : districtIterator[1]
            }
            districtList.append(districtDict)
        return districtList

def __getCity(districtId = ""):
    if districtId =="" : 
        cityQuery = f"SELECT city_id , city_name FROM city"
        sql.execute(cityQuery)
        cityResult = sql.fetchall()
        cityList = []
        for cityIterator in cityResult:
            cityDict = {
                'city_id' : str(cityIterator[0]),
                "city_name" : cityIterator[1]
            }
            cityList.append(cityDict)
        return cityList

    else:
        cityQuery = f"SELECT city_id , city_name FROM city WHERE = '{districtId}'"
        sql.execute(cityQuery)
        cityResult = sql.fetchall()
        cityList = []
        for cityIterator in cityResult:
            cityDict = {
                'city_id' : str(cityIterator[0]),
                "city_name" : cityIterator[1]
            }
            cityList.append(cityDict)
        return cityList

def __getTehsil(TehsilId = ""):
    if TehsilId =="" : 
        tehsilQuery = f"SELECT tehsil_id , tehsil_name FROM tehsil"
        sql.execute(tehsilQuery)
        tehsilResult = sql.fetchall()
        tehsilList = []
        for tehsilIterator in tehsilResult:
            tehsilDict = {
                'tehsil_id' : str(tehsilIterator[0]),
                "tehsil_name" : tehsilIterator[1]
            }
            tehsilList.append(tehsilDict)
        return tehsilList

    else:
        tehsilQuery = f"SELECT tehsil_id , tehsil_name FROM tehsil WHERE = '{TehsilId}'"
        sql.execute(tehsilQuery)
        tehsilResult = sql.fetchall()
        tehsilList = []
        for tehsilIterator in tehsilResult:
            tehsilDict = {
                'tehsil_id' : str(tehsilIterator[0]),
                "tehsil_name" : tehsilIterator[1]
            }
            tehsilList.append(tehsilDict)
        return tehsilList


def __getClasses():
    classQuery = f"SELECT * FROM classes"
    sql.execute(classQuery)
    classresult = sql.fetchall()
    classList = []
    for classIterator in classresult:
        classDict = {
            'class_id' : str(classIterator[0]),
            "class_name" : classIterator[1],
            "date_time":classIterator[2]
        }
        classList.append(classDict)
    return classList

def __getRoleTableDetails(roleId = "" , lowerLimit = "" , dataDistribution = ""):
    if roleId :
        accountDetailQuery = f"SELECT * FROM role WHERE roleId = '{roleId}'"
        sql.execute(accountDetailQuery)
        accountDetailResult = sql.fetchone()
        accountDetailDict = {
            "roleId" : accountDetailResult[0],
            "role_name" : accountDetailResult[1],
            "date_time" : accountDetailResult[2]
        }
        return accountDetailDict

    elif all([roleId == "" , lowerLimit == "" , dataDistribution == ""]):
        accountDetailQuery = f"SELECT * FROM role"
        sql.execute(accountDetailQuery)
        accountDetailResult = sql.fetchall()
        accountDetailsList = []
        for detailIterator in accountDetailResult:
            detailDict = {
                'roleId' : detailIterator[0],
                "role_name" : detailIterator[1],
                "date_time" : detailIterator[2]
            }
            accountDetailsList.append(detailDict)
        return accountDetailsList

    elif all([roleId == "" , lowerLimit != "" , dataDistribution != "" ]):
        accountDetailQuery = f"SELECT * FROM role LIMIT {lowerLimit} , {dataDistribution}"
        sql.execute(accountDetailQuery)
        accountDetailResult = sql.fetchall()
        accountDetailsList = []
        for detailIterator in accountDetailResult:
            detailDict = {
                'roleId' : detailIterator[0],
                "role_name" : detailIterator[1],
                "date_time" : detailIterator[2]
            }
            accountDetailsList.append(detailDict)
        return accountDetailsList


def __getModuleAccessTableDetails(id=""):
    if id =="" : 
        moduleAccessQuery = f"SELECT * FROM moduleaccess"
        sql.execute(moduleAccessQuery)
        moduleAccessResult = sql.fetchall()
        moduleAccessList = []
        for moduleAccessIterator in moduleAccessResult:
            moduleAccessDict = {
                'id' : str(moduleAccessIterator[0]),
                "moduleId" : moduleAccessIterator[1],
                "roleId" : moduleAccessIterator[2],
                "view" : moduleAccessIterator[3],
                "edit" : moduleAccessIterator[4]
            }
            moduleAccessList.append(moduleAccessDict)
        return moduleAccessList

    else:

        moduleAccessQuery = f"SELECT * FROM moduleaccess WHERE id = '{id}'"
        sql.execute(moduleAccessQuery)
        moduleAccessResult = sql.fetchone()
        moduleAccessList = []

        moduleAccessDict = {
                'id' : str(moduleAccessResult[0]),
                "moduleId" : moduleAccessResult[1],
                "roleId" : moduleAccessResult[2],
                "view" : moduleAccessResult[3],
                "edit" : moduleAccessResult[4]
            }
        moduleAccessList.append(moduleAccessDict)
        return moduleAccessList


def __getModuleTableDetails(moduleId = ""):
    if moduleId:
        moduleQuery = f"SELECT * FROM modules WHERE moduleId = '{moduleId}'"
        sql.execute(moduleQuery)
        moduleResult = sql.fetchone()
        moduleResultList = []
        moduleResultDict = {
            "moduleId" : moduleResult[0],
            "module_name": moduleResult[1],
            "date_time" : moduleResult[2]
        }
        moduleResultList.append(moduleResultDict)
        return moduleResultList

    else:
        moduleQuery = f"SELECT * FROM modules"
        sql.execute(moduleQuery)
        moduleResult = sql.fetchall()
        moduleResultList = []
        for moduleIterator in moduleResult:
            moduleResultDict = {
                'moduleId' : moduleIterator[0],
                "module_name" : moduleIterator[1],
                "date_time" : moduleIterator[2]
            }
            moduleResultList.append(moduleResultDict)
        return moduleResultList

def __getModuleEditView(roleId = ""):
    moduleQuery = f"SELECT * FROM modules"
    sql.execute(moduleQuery)
    moduleResult = sql.fetchall()
    
    
    moduleResultList = []
    for moduleIterator in moduleResult:
        viewQuery = f"SELECT view FROM moduleaccess WHERE roleId = '{roleId}' AND moduleId = '{moduleIterator[0]}'"
        sql.execute(viewQuery)
        viewResult = sql.fetchone()
        if viewResult  == None:
            viewResult = ["",""]

        editQuery = f"SELECT edit FROM moduleaccess WHERE roleId = '{roleId}' AND moduleId = '{moduleIterator[0]}'"
        sql.execute(editQuery)
        editResult = sql.fetchone()
        if editResult  == None:
            editResult = ["",""]

        moduleResultDict = {
            'moduleId' : moduleIterator[0],
            "module_name" : moduleIterator[1],
            "date_time" : moduleIterator[2],
            "view" : viewResult[0],
            "edit" : editResult[0]
        }
        moduleResultList.append(moduleResultDict)
    return moduleResultList

def __getCustomerTableDeatil(customerId = "" , pageSlug = "" , lowerLimit = "" , dataDistribution = "") :
    if customerId :
        accountDetailQuery = f"SELECT * FROM customerdetails WHERE customerId = '{customerId}'"
        sql.execute(accountDetailQuery)
        accountDetailResult = sql.fetchone()
        accountDetailDict = {
            "customerId" : accountDetailResult[0],
            "customerName" : accountDetailResult[1],
            "customerUserName" : accountDetailResult[2],
            "customerEmail" : accountDetailResult[3],
            "customerMobile" : accountDetailResult[4],
            "customerPassword" : accountDetailResult[5],
            "customerToken" : accountDetailResult[6],
            "customerStatus" : accountDetailResult[7],
            "date_time":accountDetailResult[8],
            "page_slug": accountDetailResult[9],
        }
        return accountDetailDict
    
    elif pageSlug:
        accountDetailQuery = f"SELECT * FROM customerdetails WHERE page_slug = '{pageSlug}'"
        sql.execute(accountDetailQuery)
        accountDetailResult = sql.fetchone()
        accountDetailDict = {
            "customerId" : accountDetailResult[0],
            "customerName" : accountDetailResult[1],
            "customerUserName" : accountDetailResult[2],
            "customerEmail" : accountDetailResult[3],
            "customerMobile" : accountDetailResult[4],
            "customerPassword" : accountDetailResult[5],
            "customerToken" : accountDetailResult[6],
            "customerStatus" : accountDetailResult[7],
            "date_time":accountDetailResult[8],
            "page_slug": accountDetailResult[9],

        }
        return accountDetailDict

    elif all([customerId == "" , pageSlug == "" , lowerLimit == "" , dataDistribution == ""]):
        accountDetailQuery = f"SELECT * FROM customerdetails"
        sql.execute(accountDetailQuery)
        accountDetailResult = sql.fetchall()
        accountDetailsList = []
        for detailIterator in accountDetailResult:
            detailDict = {
            "customerId" : detailIterator[0],
            "customerName" : detailIterator[1],
            "customerUserName" : detailIterator[2],
            "customerEmail" : detailIterator[3],
            "customerMobile" : detailIterator[4],
            "customerPassword" : detailIterator[5],
            "customerToken" : detailIterator[6],
            "customerStatus" : detailIterator[7],
            "date_time":detailIterator[8],
            "page_slug": detailIterator[9],

        }
            accountDetailsList.append(detailDict)
        return accountDetailsList

    elif all([customerId == "" , pageSlug == "" , lowerLimit != "" , dataDistribution != "" ]):
        accountDetailQuery = f"SELECT * FROM customerdetails LIMIT {lowerLimit} , {dataDistribution}"
        sql.execute(accountDetailQuery)
        accountDetailResult = sql.fetchall()
        accountDetailsList = []
        for detailIterator in accountDetailResult:
            detailDict = {
            "customerId" : detailIterator[0],
            "customerName" : detailIterator[1],
            "customerUserName" : detailIterator[2],
            "customerEmail" : detailIterator[3],
            "customerMobile" : detailIterator[4],
            "customerPassword" : detailIterator[5],
            "customerToken" : detailIterator[6],
            "customerStatus" : detailIterator[7],
            "date_time":detailIterator[8],
            "page_slug": detailIterator[9],

        }
            accountDetailsList.append(detailDict)
        return accountDetailsList

# def __customerTableDetails()
# print(__getCustomerTableDeatil("","divesh-singla"))