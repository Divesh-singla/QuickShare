import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from helper.removeDuplicate import __getUniqueList
from helper.tableDetails import __getSchoolTableDetails , __getTehsil
def __getDropdowns(coloumnName1 , coloumnName2 , data1 , data2):
    initialList = []
    dropdownList = []
    for data1Iterator in data1:
        initialList.append(data1Iterator.get(coloumnName1))
        initialList = __getUniqueList(initialList)

    for initialListIterator in initialList:
        for data2Iterator in data2:
            if initialListIterator == (data2Iterator.get(coloumnName2)):
                dropdownList.append(data2Iterator)
    return dropdownList


# def getStateDropdown():
#     schoolStates = []
#     stateDropdownList = []
#     for schoolIterator in __getSchoolTableDetails():
#         schoolStates.append(schoolIterator.get("state"))
#         schoolStates = __getUniqueList(schoolStates)

#     for schoolStateIterator in schoolStates:
#         for stateIterator in __getState():
#             if schoolStateIterator == (stateIterator.get('state_id')):
#                 stateDropdownList.append(stateIterator)
#     return stateDropdownList

# def getDistrictDropdown():
#     schoolDistrict = []
#     districtDropdownList = []
#     for schoolIterator in __getSchoolTableDetails():
#         schoolDistrict.append(schoolIterator.get("district"))
#         schoolDistrict = __getUniqueList(schoolDistrict)

#     for schoolDistrictIterator in schoolDistrict:
#         for districtIterator in __getDistrict():
#             if schoolDistrictIterator == (districtIterator.get('district_id')):
#                 districtDropdownList.append(districtIterator)
#     return districtDropdownList

# def getCityDropdown():
#     schoolCity = [] 
#     cityDropdownList = []
#     for schoolIterator in __getSchoolTableDetails():
#         schoolCity.append(schoolIterator.get("city"))
#         schoolCity = __getUniqueList(schoolCity)

#     for schoolCityIterator in schoolCity:
#         for cityIterator in __getCity():
#             if schoolCityIterator == (cityIterator.get('city_id')):
#                 cityDropdownList.append(cityIterator)
#     return cityDropdownList

def getTehsilDropdown():
    schoolTehsil = []
    tehsilDropdownList = []
    for schoolIterator in __getSchoolTableDetails():
        schoolTehsil.append(schoolIterator.get("tehsil"))
        schoolTehsil = __getUniqueList(schoolTehsil)

    for schoolTehsilIterator in schoolTehsil:
        for districtIterator in __getTehsil():
            if schoolTehsilIterator == (districtIterator.get('tehsil_id')):
                tehsilDropdownList.append(districtIterator)
    return tehsilDropdownList

# print(getTehsilDropdown())
# print(__getDropdowns("tehsil" , "tehsil_id" , __getSchoolTableDetails() , __getTehsil()))