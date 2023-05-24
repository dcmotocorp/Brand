from django.shortcuts import render
import requests, json
from django.http import HttpResponse
# Create your views here.


def login_page(request):
    return render(request,'login.html')

def signup_page(request):
    # ('username','email', 'password', 'role','first_name','last_name')
    return render(request,'signup.html')

def select_role(request):
    return render(request,'role.html')

def get_role(request):
    request.session['role'] = request.POST.get('role')
    return render(request,'signup.html')
    

def submit_user(request):
    data = request.POST
    data = {}
    data['first_name'] = request.POST.get('firstname')
    data['last_name'] = request.POST.get('lastname')
    data['email'] = request.POST.get('email')
    data['password'] = request.POST.get('password')
    data['username'] = request.POST.get('username')
    data['role'] = request.session.get('role')
    url =  "http://127.0.0.1:8000/auths/register/"
    resposne = requests.post(url,data= data)
    return render(request,'login.html')

def validate_user(request):

    data = {}
    
    data['password'] = request.POST.get('password')
    data['username'] = request.POST.get('username')
    url =  "http://127.0.0.1:8000/auths/login/"
    print(data)
    resposne = requests.post(url,data= data)
    return HttpResponse(resposne)
