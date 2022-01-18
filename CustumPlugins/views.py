from django.shortcuts import render
from .models import UserList, ContactNumber ,AdminInformations
from django.views import View
from django.http import HttpResponse
from django.views.generic.edit import FormView, DeleteView
from .forms import UserForm

def cms_data(request):
    instance =  UserList.objects.all()
    contact =  ContactNumber.objects.all()
    admin =  AdminInformations.objects.all()

    return render(request,'index.html', {'instance':instance,'contact':contact,'admin':admin})



# class About(FormView):
#     form_class = UserForm

#     template_name = 'user.html'
#     success_url ="/thanks/"

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
         
#         # perform a action here
#         print(form.cleaned_data)
#         return super().form_valid(form)
    

class UserDeleteView(DeleteView):
    model = UserList

    success_url ='/'