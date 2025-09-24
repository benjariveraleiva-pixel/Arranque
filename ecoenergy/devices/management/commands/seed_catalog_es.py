# devices/management/commands/seed_catalog_es.py
from django.core.management.base import BaseCommand
from devices.models import Category, Product, AlertRule, ProductAlertRule, Organization, Zone, Device

class Command(BaseCommand):
    help = "Carga datos iniciales en español para EcoEnergy"

    def handle(self, *args, **kwargs):
        self.stdout.write("Cargando datos iniciales...")
        
        # Crear categorías
        cat_iluminacion, _ = Category.objects.get_or_create(
            name="Iluminación",
            defaults={'description': 'Productos de iluminación eficiente'}
        )
        
        cat_climatizacion, _ = Category.objects.get_or_create(
            name="Climatización",
            defaults={'description': 'Sistemas de climatización eficiente'}
        )
        
        # Crear productos (los 3 requeridos)
        producto1, _ = Product.objects.get_or_create(
            sku="LED-40W",
            defaults={
                'name': "Panel LED 40W",
                'description': "Panel LED de alta eficiencia 40W",
                'category': cat_iluminacion
            }
        )
        
        producto2, _ = Product.objects.get_or_create(
            sku="TERM-3000",
            defaults={
                'name': "Termostato Inteligente 3000",
                'description': "Termostato programable para climatización",
                'category': cat_climatizacion
            }
        )
        
        producto3, _ = Product.objects.get_or_create(
            sku="SENS-TEMP",
            defaults={
                'name': "Sensor de Temperatura",
                'description': "Sensor para medición de temperatura ambiental",
                'category': cat_climatizacion
            }
        )
        
        # Crear reglas de alerta (las 2 requeridas)
        alerta_alto, _ = AlertRule.objects.get_or_create(
            name="Consumo Alto",
            defaults={
                'description': "Alerta por consumo excesivo de energía",
                'condition_type': 'GT',
                'threshold_value': 100.0
            }
        )
        
        alerta_bajo, _ = AlertRule.objects.get_or_create(
            name="Consumo Bajo Inusual",
            defaults={
                'description': "Alerta por consumo inusualmente bajo",
                'condition_type': 'LT',
                'threshold_value': 5.0
            }
        )
        
        # Relacionar productos con reglas de alerta
        ProductAlertRule.objects.get_or_create(
            product=producto1,
            alert_rule=alerta_alto
        )
        
        ProductAlertRule.objects.get_or_create(
            product=producto2,
            alert_rule=alerta_alto
        )
        
        ProductAlertRule.objects.get_or_create(
            product=producto3,
            alert_rule=alerta_bajo
        )
        
        # Crear organización (1 requerida)
        org, _ = Organization.objects.get_or_create(
            name="EcoEnergy Central",
            defaults={'description': 'Sede principal de EcoEnergy'}
        )
        
        # Crear zonas (2 requeridas)
        zona1, _ = Zone.objects.get_or_create(
            name="Oficinas",
            organization=org,
            defaults={'description': 'Área de oficinas administrativas'}
        )
        
        zona2, _ = Zone.objects.get_or_create(
            name="Taller",
            organization=org,
            defaults={'description': 'Área de taller y producción'}
        )
        
        # Crear dispositivos (3 requeridos)
        Device.objects.get_or_create(
            serial_number="DEV-001",
            defaults={
                'name': "Sensor Oficina 1",
                'zone': zona1,
                'product': producto1
            }
        )
        
        Device.objects.get_or_create(
            serial_number="DEV-002",
            defaults={
                'name': "Termostato Principal",
                'zone': zona1,
                'product': producto2
            }
        )
        
        Device.objects.get_or_create(
            serial_number="DEV-003",
            defaults={
                'name': "Sensor Taller",
                'zone': zona2,
                'product': producto3
            }
        )
        
        self.stdout.write(
            self.style.SUCCESS("✅ Datos iniciales cargados exitosamente!")
        )