from django.urls import path
from CustumPlugins.views import cms_data
urlpatterns = [
    path('',cms_data,name='cms_data'),
 
]





