from django.contrib import admin
from Record.models import Profile



@admin.register(Profile)
class authorAdmin(admin.ModelAdmin):
    list_display = ("id","prouser")
    list_display_links= ("id","prouser")

# Register your models here.
