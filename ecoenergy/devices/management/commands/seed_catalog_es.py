from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from devices.models import (
    Category, Product, AlertRule, ProductAlertRule, 
    Organization, Zone, Device, Measurement, 
    AlertEvent, UserProfile
)

class Command(BaseCommand):
    help = 'Seed the database with Spanish catalog data'
    
    def handle(self, *args, **options):
        self.stdout.write('Starting Spanish catalog seeding...')
        self.create_spanish_catalog()
        self.stdout.write(
            self.style.SUCCESS('✅ Spanish catalog seeded successfully!')
        )

    def create_spanish_catalog(self):
        """Create Spanish catalog data"""
        
        # Crear Categorías en Español
        categorias = [
            {
                'name': 'Sensores de Energía',
                'description': 'Dispositivos para medir consumo energético y parámetros eléctricos'
            },
            {
                'name': 'Controladores Industriales',
                'description': 'Dispositivos de control y automatización para entornos industriales'
            },
            {
                'name': 'Sistemas de Monitoreo',
                'description': 'Equipos para monitoreo en tiempo real de variables energéticas'
            },
            {
                'name': 'Medidores Inteligentes',
                'description': 'Medidores avanzados con capacidades de comunicación y análisis'
            },
            {
                'name': 'Sensores Ambientales',
                'description': 'Dispositivos para medición de condiciones ambientales'
            }
        ]
        
        for cat_data in categorias:
            categoria, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                self.stdout.write(f'✓ Categoría creada: {cat_data["name"]}')

        # Crear Organizaciones
        organizaciones = [
            {
                'name': 'Empresa Principal S.A.',
                'description': 'Sede central y administración principal del grupo'
            },
            {
                'name': 'Planta Industrial Norte',
                'description': 'Planta de producción ubicada en la zona norte'
            },
            {
                'name': 'Centro Logístico Sur',
                'description': 'Centro de distribución y logística zona sur'
            },
            {
                'name': 'Oficinas Administrativas',
                'description': 'Edificio corporativo y oficinas administrativas'
            }
        ]
        
        for org_data in organizaciones:
            organizacion, created = Organization.objects.get_or_create(
                name=org_data['name'],
                defaults={'description': org_data['description']}
            )
            if created:
                self.stdout.write(f'✓ Organización creada: {org_data["name"]}')

        # Crear Zonas
        org_principal = Organization.objects.get(name='Empresa Principal S.A.')
        org_planta = Organization.objects.get(name='Planta Industrial Norte')
        org_logistica = Organization.objects.get(name='Centro Logístico Sur')
        org_oficinas = Organization.objects.get(name='Oficinas Administrativas')
        
        zonas = [
            {'name': 'Sala de Control Principal', 'organization': org_principal, 'description': 'Centro de control operacional'},
            {'name': 'Línea de Producción A', 'organization': org_planta, 'description': 'Línea de producción principal'},
            {'name': 'Línea de Producción B', 'organization': org_planta, 'description': 'Línea de producción secundaria'},
            {'name': 'Área de Almacenamiento', 'organization': org_logistica, 'description': 'Zona de almacenamiento de productos'},
            {'name': 'Dock de Carga', 'organization': org_logistica, 'description': 'Área de carga y descarga'},
            {'name': 'Oficinas Piso 1', 'organization': org_oficinas, 'description': 'Área administrativa primer piso'},
            {'name': 'Sala de Servidores', 'organization': org_oficinas, 'description': 'Centro de procesamiento de datos'},
        ]
        
        for zona_data in zonas:
            zona, created = Zone.objects.get_or_create(
                name=zona_data['name'],
                organization=zona_data['organization'],
                defaults={'description': zona_data['description']}
            )
            if created:
                self.stdout.write(f'✓ Zona creada: {zona_data["name"]}')

        # Crear Productos
        cat_sensores = Category.objects.get(name='Sensores de Energía')
        cat_controladores = Category.objects.get(name='Controladores Industriales')
        cat_monitoreo = Category.objects.get(name='Sistemas de Monitoreo')
        cat_medidores = Category.objects.get(name='Medidores Inteligentes')
        cat_ambiental = Category.objects.get(name='Sensores Ambientales')
        
        productos = [
            {
                'name': 'Sensor de Energía Trifásico',
                'sku': 'SEN-3F-ES-001',
                'description': 'Sensor avanzado para medición trifásica con comunicación Modbus',
                'category': cat_sensores
            },
            {
                'name': 'Controlador PLC Industrial',
                'sku': 'CTRL-PLC-ES-001',
                'description': 'Controlador programable para automatización industrial',
                'category': cat_controladores
            },
            {
                'name': 'Sistema Monitoreo Energético',
                'sku': 'MON-ENERGY-ES-001',
                'description': 'Sistema completo para monitoreo de consumo energético',
                'category': cat_monitoreo
            },
            {
                'name': 'Medidor Inteligente Monofásico',
                'sku': 'MED-1F-SMART-ES-001',
                'description': 'Medidor inteligente para aplicaciones monofásicas',
                'category': cat_medidores
            },
            {
                'name': 'Sensor de Temperatura y Humedad',
                'sku': 'SEN-TEMP-HUM-ES-001',
                'description': 'Sensor para medición ambiental de temperatura y humedad',
                'category': cat_ambiental
            },
            {
                'name': 'Analizador de Calidad Energética',
                'sku': 'ANA-CALIDAD-ES-001',
                'description': 'Equipo para análisis de calidad de energía y armónicos',
                'category': cat_sensores
            }
        ]
        
        for prod_data in productos:
            producto, created = Product.objects.get_or_create(
                sku=prod_data['sku'],
                defaults={
                    'name': prod_data['name'],
                    'description': prod_data['description'],
                    'category': prod_data['category']
                }
            )
            if created:
                self.stdout.write(f'✓ Producto creado: {prod_data["name"]}')

        # Crear Reglas de Alerta
        reglas_alerta = [
            {
                'name': 'Consumo Crítico de Energía',
                'condition': 'valor > umbral',
                'severity': 'high',
                'status': True
            },
            {
                'name': 'Consumo Elevado de Energía',
                'condition': 'valor > umbral',
                'severity': 'medium',
                'status': True
            },
            {
                'name': 'Variación de Voltaje',
                'condition': 'abs(valor - referencia) > umbral',
                'severity': 'high',
                'status': True
            },
            {
                'name': 'Temperatura Elevada',
                'condition': 'valor > umbral',
                'severity': 'medium',
                'status': True
            },
            {
                'name': 'Factor de Potencia Bajo',
                'condition': 'valor < umbral',
                'severity': 'low',
                'status': True
            }
        ]
        
        for regla_data in reglas_alerta:
            regla, created = AlertRule.objects.get_or_create(
                name=regla_data['name'],
                defaults={
                    'condition': regla_data['condition'],
                    'severity': regla_data['severity'],
                    'status': regla_data['status']
                }
            )
            if created:
                self.stdout.write(f'✓ Regla de alerta creada: {regla_data["name"]}')

        # Crear Dispositivos
        zona_control = Zone.objects.get(name='Sala de Control Principal')
        zona_linea_a = Zone.objects.get(name='Línea de Producción A')
        zona_almacen = Zone.objects.get(name='Área de Almacenamiento')
        zona_oficinas = Zone.objects.get(name='Oficinas Piso 1')
        
        sensor_3f = Product.objects.get(sku='SEN-3F-ES-001')
        controlador_plc = Product.objects.get(sku='CTRL-PLC-ES-001')
        medidor_1f = Product.objects.get(sku='MED-1F-SMART-ES-001')
        sensor_temp = Product.objects.get(sku='SEN-TEMP-HUM-ES-001')
        analizador = Product.objects.get(sku='ANA-CALIDAD-ES-001')
        
        dispositivos = [
            {'name': 'Sensor Trifásico Línea A', 'serial_number': 'ES-SN-3F-LA-001', 'zone': zona_linea_a, 'product': sensor_3f},
            {'name': 'PLC Control Principal', 'serial_number': 'ES-SN-PLC-CP-001', 'zone': zona_control, 'product': controlador_plc},
            {'name': 'Medidor Oficinas P1', 'serial_number': 'ES-SN-MED-OF1-001', 'zone': zona_oficinas, 'product': medidor_1f},
            {'name': 'Sensor Ambiental Almacén', 'serial_number': 'ES-SN-TEMP-ALM-001', 'zone': zona_almacen, 'product': sensor_temp},
            {'name': 'Analizador Calidad Línea A', 'serial_number': 'ES-SN-ANA-LA-001', 'zone': zona_linea_a, 'product': analizador},
        ]
        
        for disp_data in dispositivos:
            dispositivo, created = Device.objects.get_or_create(
                serial_number=disp_data['serial_number'],
                defaults={
                    'name': disp_data['name'],
                    'zone': disp_data['zone'],
                    'product': disp_data['product']
                }
            )
            if created:
                self.stdout.write(f'✓ Dispositivo creado: {disp_data["name"]}')

        # Crear Usuarios de Ejemplo
        usuarios = [
            {
                'username': 'admin.es', 
                'email': 'administrador@empresa.es', 
                'password': 'Admin123!',
                'org': org_principal, 
                'role': 'admin',
                'first_name': 'Carlos',
                'last_name': 'Administrador'
            },
            {
                'username': 'operador.es', 
                'email': 'operador@empresa.es', 
                'password': 'Oper123!',
                'org': org_planta, 
                'role': 'operator',
                'first_name': 'Ana',
                'last_name': 'Operadora'
            },
            {
                'username': 'visor.es', 
                'email': 'visor@empresa.es', 
                'password': 'View123!',
                'org': org_oficinas, 
                'role': 'viewer',
                'first_name': 'Luis',
                'last_name': 'Visualizador'
            },
        ]
        
        for user_data in usuarios:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                    'is_staff': True,
                    'is_active': True
                }
            )
            if created:
                user.set_password(user_data['password'])
                user.save()
                
                UserProfile.objects.get_or_create(
                    user=user,
                    defaults={
                        'organization': user_data['org'],
                        'role': user_data['role']
                    }
                )
                self.stdout.write(f'✓ Usuario creado: {user_data["username"]}')

        # Resumen Final
        self.stdout.write('\n📊 Resumen del Catálogo Español:')
        self.stdout.write(f'   Categorías: {Category.objects.count()}')
        self.stdout.write(f'   Organizaciones: {Organization.objects.count()}')
        self.stdout.write(f'   Zonas: {Zone.objects.count()}')
        self.stdout.write(f'   Productos: {Product.objects.count()}')
        self.stdout.write(f'   Reglas de Alerta: {AlertRule.objects.count()}')
        self.stdout.write(f'   Dispositivos: {Device.objects.count()}')
        self.stdout.write(f'   Usuarios: {User.objects.count()}')