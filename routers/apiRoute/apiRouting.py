from django.urls import path
from controller.schoolApiController import getSchoolApi
from controller.schoolApiController import getSchoolDataBySchoolApi
from controller.schoolApiController import getSaveSchoolData
from controller.schoolApiController import getUpdateSchoolData
from django.views.decorators.csrf import csrf_exempt

configureApiRoutes = [{
    'path': 'schoolApi',
    'controller': csrf_exempt(getSchoolApi),
    'name': 'SchoolApi',
    'csrf': False,
    'pageType': 'public'
},
{
    'path': 'schoolDataBySchool',
    'controller': csrf_exempt(getSchoolDataBySchoolApi),
    'name': 'schoolDataByUserId',
    'csrf': False,
    'pageType': 'public'
},
{
    'path': 'saveSchoolData',
    'controller': csrf_exempt(getSaveSchoolData),
    'name': 'saveSchoolData',
    'csrf': False,
    'pageType': 'public'
},
{
    'path': 'updateSchoolData',
    'controller': csrf_exempt(getUpdateSchoolData),
    'name': 'updateSchoolData',
    'csrf': False,
    'pageType': 'public'
},
]

def createRoute(obj):
    if obj['pageType'] == "public":
        return path(obj.get("path") , obj['controller'] , name=obj['name'])



apiUrlPatterns = []

for urlIteator in configureApiRoutes:
    apiUrlPatterns.append(createRoute(urlIteator))


# apiUrlPatterns = [
#     path("schoolApi" , csrf_exempt(getSchoolApi) , name="SchoolApi"),
#     path("schoolDataBySchool" ,csrf_exempt(getSchoolDataBySchoolApi) , name="byUserId" ),
#     path("saveSchoolData" , csrf_exempt(getSaveSchoolData) , name="saveSchoolData"),
#     path("updateSchoolData" , csrf_exempt(getUpdateSchoolData) , name="updateSchoolData"),
# ]
