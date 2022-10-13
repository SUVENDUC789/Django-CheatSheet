from django.contrib import admin
from home.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email')
