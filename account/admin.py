from django.contrib import admin
from .models import *
from django.contrib.auth.models import  Group
# Register your models here.
admin.site.register(User)
admin.site.unregister(Group)
admin.site.site_header='Mongiz_administration'
admin.site.site_title='Mongiz_administration'