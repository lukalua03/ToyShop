from django.contrib import admin

from .models import Category, Product, Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','price','status',)
    list_display_links=('id','title',)
    search_fields=('id','title',)
    list_editabel=('price',)
    list_filter = ('price',)


admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
