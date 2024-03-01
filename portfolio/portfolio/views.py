from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    return render(request,"about.html")
def dummy(request):
    n1=0
    try:
        n=int(request.POST['val1'])
        n1=n
    except:
        pass
    return render(request,"dummy.html",{'nums':n1})
def homepage(request):
    return render(request,"index.html")
