# myapp/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register(r'startups',views.Startups
)


urlpatterns = [
] + route.urls
