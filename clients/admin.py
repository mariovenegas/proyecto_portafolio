from django.contrib import admin
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    readonly_field = ('created','updated')

admin.site.register(Client,ClientAdmin)
