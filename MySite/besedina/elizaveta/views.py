from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'home.html')
def name(request):
    return render(request, 'name.html')
def age(request):
    return render(request, 'age.html')
def group(request):
    return render(request, 'group.html')
def common(request):
    return render(request, 'common.html')