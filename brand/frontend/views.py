from django.shortcuts import render

# Create your views here.


def login_page(request):
    return render(request,'login.html')

def signup_page(request):
    return render(request,'signup.html')

def select_role(request):
    return render(request,'role.html')
