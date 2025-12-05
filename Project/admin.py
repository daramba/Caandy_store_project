from django.contrib import admin
from .models import Manufacturer, Brand, SweetType, Flavor, Sweet, Purchase

# Регистрация всех моделей
admin.site.register(Manufacturer)
admin.site.register(Brand)
admin.site.register(SweetType)
admin.site.register(Flavor)

# Кастомизация отображения сладостей
class SweetAdmin(admin.ModelAdmin):
    list_display = ('sweet_id', 'brand', 'type', 'flavor', 'price', 'weight')
    list_filter = ('brand', 'type', 'flavor')
    search_fields = ('composition', 'brand__brand_name')

admin.site.register(Sweet, SweetAdmin)

# Кастомизация отображения покупок
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchase_id', 'sweet', 'quantity', 'amount', 'purchase_date')
    list_filter = ('purchase_date',)

admin.site.register(Purchase, PurchaseAdmin)