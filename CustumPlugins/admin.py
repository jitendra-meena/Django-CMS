from django.contrib import admin
from .models import Hello, UserList, AdminInformations, ContactNumber
# Register your models here.

admin.site.register(Hello)

admin.site.register(UserList)
admin.site.register(AdminInformations)
admin.site.register(ContactNumber)