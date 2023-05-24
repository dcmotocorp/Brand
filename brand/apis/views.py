from django.shortcuts import render
from .models import Startups
from .serializers import StartupSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
# Create your views here.

# =============== START UPS =========================



# @api_view(("GET",))
# def get_all_startups(request):
#     instants = Startups.objects.all()
#     serializers = StartupSerializer(instants,many=True)
#     return Response(serializers.data,status=status.HTTP_200_OK)


class Startups(ModelViewSet):
    queryset = Startups.objects.all()
    serializer_class = StartupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


 

def get_per_startupFeed(request):
    pass

def get_startup_detail(request):
    pass 


#    update section 

def update_startup_basic_info(request):
    pass

def update_startup_feed(request):
    pass

#     delete section 
 
def delete_startup_feed(request):
    pass

def delete_startup(request):
    pass 



# =============== START UPS =========================

# =============== INVESTOR  =========================

def get_all_investors(request):
    pass 

def get_per_investorsfeed(request):
    pass
# =============== INVESTOR  =========================

# =============== AUDIENCE  =========================
def get_all_audience(request):
    pass 
# =============== AUDIENCE  =========================


