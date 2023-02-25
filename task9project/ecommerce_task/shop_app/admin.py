from django.contrib import admin

# Register your models here.
from . models import Category1,Product1
class Cat1Admin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category1,Cat1Admin)

class Prod1Admin(admin.ModelAdmin):
    list_display=['name','price','stock','available','created','updated']
    list_editable=['price','stock','available']
    prepopulated_fields={'slug':('name',)}
    list_per_page=15
admin.site.register(Product1,Prod1Admin)
