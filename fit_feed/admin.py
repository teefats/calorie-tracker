from django.contrib import admin
from .models import *
# Register your models here.


class foodAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    class Meta:
        models = Fooditem
    
admin.site.register(Customer)
admin.site.register(UserFooditem)
admin.site.register(Category)
admin.site.register(Fooditem,foodAdmin)