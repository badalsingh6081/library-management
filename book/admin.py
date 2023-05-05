from django.contrib import admin
from .models import book
# Register your models here.

@admin.register(book)
class bookadmin(admin.ModelAdmin):
    list_display=['id','title','author','publisher','publish_date','category']
    
   
