from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand',)

admin.site.register(model_or_iterable=Car, admin_class= CarAdmin)
admin.site.register(model_or_iterable=Brand, admin_class= BrandAdmin)
