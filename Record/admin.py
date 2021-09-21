from django.contrib import admin
from .models import Product,Employee

@admin.register(Product)
class authorAdmin(admin.ModelAdmin):
    list_display = ("id","name","category","owner")
    list_display_links= ("id","name")

@admin.register(Employee)
class authorAdmin(admin.ModelAdmin):
    list_display = ("id","employee_name")
    list_display_links= ("id","employee_name")
