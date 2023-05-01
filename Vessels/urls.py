# Load path from django.urls
from django.urls import path

# Load this applications views.py file
from . import views

# define url patterns
urlpatterns = [
    # get index view
    # example url : /airports/
    path('', views.index),
    # show airport info
    # example url /airports/MYR
    # notice the airport_code parameter in the url matches
    # the parameter in the airport_info function
    path('Vessels/', views.Vessels),
    path('/<str:vessel_name>', views.Vessel_info),
    path('Vessels/Charleston', views.charleston_vessels),
    path('Vessels/<int:vessel_id>/', views.vessel_schedule),
    path('Port/', views.port_info),
]