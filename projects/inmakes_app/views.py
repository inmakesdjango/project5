from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.
def static(request):
    obj = Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
# def demo(request):
#     name="india"
#     return render(request,"home.html",{'obj':name})
# def addition(request):
#     x= int(request.GET['num1'])
#     y= int(request.GET['num2'])
#     add=x + y
#     subn=x-y
#     mul=x*y
#     div=x/y
#
#     return render(request,"result.html",{'sum':add,'sub':subn,'mult':mul, 'divi':div})
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("hai im contact")