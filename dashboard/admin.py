from django.contrib import admin
from .models import powerloom, production
# Register your models here.


class PowerloomAdmin(admin.ModelAdmin):
    list_display = ('plno', 'qty_name', 'size', 'location',
                    'image', 'status', 'comment')


class ProductionAdmin(admin.ModelAdmin):
    list_display = ('doprod', 'plno', 'pcs', 'weight', 'total_prod')


admin.site.register(powerloom, PowerloomAdmin)
admin.site.register(production, ProductionAdmin)
