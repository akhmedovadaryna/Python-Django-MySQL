__author__ = 'darina'
from django.contrib import admin
from orm.models import *

# Register your models here.

class admin_cloud_storage(admin.ModelAdmin):
    list_display = ['id_file','name_f','size','type','user_name_u','Cloud_storage_idstorage']

admin.site.register(FileForm,admin_cloud_storage)

class admin_user(admin.ModelAdmin):
    list_display = ['login','b_day','year']

admin.site.register(userForm,admin_user)

class admin_file(admin.ModelAdmin):
    list_display = ['ID','Name','Data_add','Data_change']

admin.site.register(CloudForm,admin_file)