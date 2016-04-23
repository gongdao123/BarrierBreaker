from django.contrib import admin

# Register your models here.
from Proxys.models import HttpProxy

class HttpProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'nick_name', 'modified_datetime']
    fields = ['nick_name', 'hash_id', 'lan_ip']
    search_fields = ['nick_name', 'hash_id', 'lan_ip']

admin.site.register(HttpProxy, HttpProxyAdmin)
