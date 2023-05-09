# myapp/urls.py

from django.urls import path

from . import views 



urlpatterns = [
path('login/',views.login_page,name='login-page'),
path('signup/',views.signup_page,name='signup-page'),
path('select-role/',views.select_role,name='select-role'),
path('get-role/',views.get_role,name='get-role'),
path('submit-user/',views.submit_user,name='submit-user'),
path('validate_user/',views.validate_user,name='login-user')





]
