from django.contrib import admin
from .models import Category, Product, AlertRule, ProductAlertRule, Organization, AlertEvent, Zone, Device, Measurement, UserProfile

# ─────────────────────────────────────────────────────────
# Reglas generales del sitio
# ─────────────────────────────────────────────────────────
admin.site.site_header = "EcoEnergy — Admin"
admin.site.site_title = "EcoEnergy Admin"
admin.site.index_title = "Panel de administración"

# ─────────────────────────────────────────────────────────
# MAESTROS (globales)
# ─────────────────────────────────────────────────────────

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at")
    search_fields = ("name", "description")
    list_filter = ("created_at",)
    ordering = ("name",)
    list_per_page = 50

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "category", "created_at", "updated_at")
    search_fields = ("name", "sku", "description", "category__name")
    list_filter = ("category", "created_at")
    ordering = ("name",)
    list_select_related = ("category",)
    list_per_page = 50

@admin.register(AlertRule)
class AlertRuleAdmin(admin.ModelAdmin):
    list_display = ("name", "severity", "condition", "status", "created_at")
    search_fields = ("name", "condition")
    list_filter = ("status", "severity", "created_at")
    ordering = ("name",)
    list_per_page = 50

@admin.register(ProductAlertRule)
class ProductAlertRuleAdmin(admin.ModelAdmin):
    list_display = ("product", "alert_rule", "threshold", "status", "created_at")
    search_fields = ("product__name", "alert_rule__name")
    list_filter = ("status", "alert_rule__severity", "created_at")
    ordering = ("product__name",)
    list_select_related = ("product", "alert_rule")
    list_per_page = 50

# ─────────────────────────────────────────────────────────
# POR ORGANIZACIÓN
# ─────────────────────────────────────────────────────────

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at")
    search_fields = ("name", "description")
    list_filter = ("created_at",)
    ordering = ("name",)
    list_per_page = 50

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "description", "created_at")
    search_fields = ("name", "description", "organization__name")
    list_filter = ("organization", "created_at")
    ordering = ("organization__name", "name")
    list_select_related = ("organization",)
    list_per_page = 50

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "serial_number", "zone", "product", "is_active", "created_at")
    search_fields = ("name", "serial_number", "zone__name", "product__name")
    list_filter = ("is_active", "zone__organization", "product__category", "created_at")
    ordering = ("zone__organization__name", "name")
    list_select_related = ("zone", "product", "zone__organization")
    list_per_page = 50

# ─────────────────────────────────────────────────────────
# SERIES (datos operacionales)
# ─────────────────────────────────────────────────────────

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("device", "value", "unit", "recorded_at")
    search_fields = ("device__name", "device__serial_number")
    list_filter = ("unit", "recorded_at", "device__zone__organization")
    ordering = ("-recorded_at",)
    list_select_related = ("device", "device__zone", "device__zone__organization")
    list_per_page = 50
    date_hierarchy = "recorded_at"

@admin.register(AlertEvent)
class AlertEventAdmin(admin.ModelAdmin):
    list_display = ("device", "product_alert_rule", "measured_value", "status", "triggered_at", "resolved_at")
    search_fields = ("device__name", "device__serial_number", "product_alert_rule__alert_rule__name")
    list_filter = ("status", "triggered_at", "device__zone__organization")
    ordering = ("-triggered_at",)
    list_select_related = ("device", "product_alert_rule", "device__zone__organization")
    list_per_page = 50
    date_hierarchy = "triggered_at"

# ─────────────────────────────────────────────────────────
# PERFILES DE USUARIO
# ─────────────────────────────────────────────────────────

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "organization", "role", "created_at")
    search_fields = ("user__username", "user__email", "organization__name")
    list_filter = ("role", "organization", "created_at")
    ordering = ("organization__name", "user__username")
    list_select_related = ("user", "organization")
    list_per_page = 50