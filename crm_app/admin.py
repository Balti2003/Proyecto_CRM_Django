from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "website")

@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "company", "assigned_to")
    
@admin.register(models.Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ("client", "user", "date", "type", "notes")