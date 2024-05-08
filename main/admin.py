from django.contrib import admin
from .models import Product,UserProfile,Tag


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","created_by","created_at","image"]
    search_fields=['name','created_by','created_at']



admin.site.register(UserProfile)
admin.site.register(Tag)