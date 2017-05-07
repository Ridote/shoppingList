from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Product)
admin.site.register(PredefinedProduct)
admin.site.register(Unit)
admin.site.register(Category)