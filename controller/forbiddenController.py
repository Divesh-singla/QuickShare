from django.shortcuts import render

def forbiddenPage(request):
    return render (request , "forbidden.html")