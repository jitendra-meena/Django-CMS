from django.urls import path
from CustumPlugins.views import cms_data
from . views import *
urlpatterns = [
    
    path('',cms_data,name='cms_data'),
    # path('about/',About.as_view(),name ='about'),
    path('delete/<pk>', UserDeleteView.as_view(),name='delete'),

 
]







