from django.contrib import admin
from .models import Category, Product, AlertRule, ProductAlertRule, Organization, Zone, Device, Measurement
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(AlertRule)
admin.site.register(ProductAlertRule)
admin.site.register(Organization)
admin.site.register(Zone)
admin.site.register(Device)
admin.site.register(Measurement)