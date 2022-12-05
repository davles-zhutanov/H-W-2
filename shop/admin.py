from django.contrib import admin

from .models import Item
from .models import Purchase

admin.site.register(Item)
admin.site.register(Purchase)