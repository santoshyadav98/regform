from django.contrib import admin
from regandlogin.models import Reg

# Register your models here.
class regisadmin(admin.ModelAdmin):
    list_display=['firstName','lastname','email','username','password','confpassword']
admin.site.register(Reg,regisadmin)

