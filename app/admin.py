from django.contrib import admin

from app.models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'new_price', 'old_price','category', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class PhoneCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class PhonesAdmin(admin.ModelAdmin):
    list_display = ('name', 'new_price', 'old_price','category', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class FridgeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class FridgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'new_price', 'old_price','category', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class HomeAppliancesCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class HomeAppliancesAdmin(admin.ModelAdmin):
    list_display = ('name', 'new_price', 'old_price','category', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin )
admin.site.register(Category, CategoryAdmin)
admin.site.register(Phones, PhonesAdmin )
admin.site.register(PhoneCategory, PhoneCategoryAdmin)
admin.site.register(Fridge, FridgeAdmin )
admin.site.register(FridgeCategory, FridgeCategoryAdmin)
admin.site.register(HomeAppliances, HomeAppliancesAdmin )
admin.site.register(HomeAppliancesCategory, HomeAppliancesCategoryAdmin)