from django.shortcuts import render
from .models import UserList

def cms_data(request):
    instance =  UserList.objects.all()

    return render(request,'index.html', {'instance':instance})


