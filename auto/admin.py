from django.contrib import admin

from auto.models import *


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    max_num = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSpecificationInline]


class OrdersInline(admin.TabularInline):
    model = Order


class UsersAdmin(admin.ModelAdmin):
    inlines = [OrdersInline]


class CarModelline(admin.TabularInline):
    model = CarModel


class CarCompanyAdmin(admin.ModelAdmin):
    inlines = [CarModelline]


class CarYearAdmin(admin.ModelAdmin):
    list_display = ('product', 'model', 'car_year')


admin.site.register(CarCompany, CarCompanyAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CarYear, CarYearAdmin)
admin.site.register(SliderImage)
admin.site.register(UserWithoutAccount, UsersAdmin)
