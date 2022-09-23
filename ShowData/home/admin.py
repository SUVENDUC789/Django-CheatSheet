from django.contrib import admin

from home.models import Biliniars as B

class ServiceAdmin(admin.ModelAdmin):
    list_display=('brank','bname','bnetworth','bage','bsource','bcountry')


admin.site.register(B,ServiceAdmin)
