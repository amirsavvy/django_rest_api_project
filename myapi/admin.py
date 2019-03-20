from django.contrib import admin
from myapi.models import Stock


class StockAdmin(admin.ModelAdmin):

    list_display = ['name', 'price']


admin.site.register(Stock, StockAdmin)
