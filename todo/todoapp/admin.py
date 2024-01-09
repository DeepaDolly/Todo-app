from django.contrib import admin

# Register your models here.
from .models import Todo
class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Todo,ContactAdmin)