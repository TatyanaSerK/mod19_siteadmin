from django.contrib import admin
from .models import *
# Register your models here.


# admin.site.register(test)

@admin.register(test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name','city')
    list_filter = ('numb',)