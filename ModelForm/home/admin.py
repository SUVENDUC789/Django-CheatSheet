from django.contrib import admin

# Register your models here.

from home.models import User

class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email')

admin.site.register(User,UserAdmin)