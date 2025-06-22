from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def projects(request):
    return render(request,'Projects.html')