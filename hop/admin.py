from django.contrib import admin
from .models import Hop, Aroma

class HopAdmin(admin.ModelAdmin):
    list_display = ('name', 'usage', 'oil_amount', 'alpha_acid')
    filter_horizontal = ('aroma',)

admin.site.register(Hop, HopAdmin)
admin.site.register(Aroma)
