from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class CBV(View):
    def get(self, request):
        return HttpResponse("<h1 style='colo:red'>Welcome to Class Based Views</h1>")
    
    def post(self, request):
        return HttpResponse("Thank U")

def Contact(request):
    if request.method=='POST':
        return HttpResponse("Thank You for fun")
    else:
        return HttpResponse("<h1 style='color:red'>Welccome to function Based Views</h1>")