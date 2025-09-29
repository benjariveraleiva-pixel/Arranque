# Setup
### 1.Clonar repositorio

$`git clone https://github.com/benjariveraleiva-pixel/Arranque.git`

### 2.Cambiar a rama de desarollo

$`git switch u2-c1`

### 3.Instalar requirimientos

Para esto recomendamos crear un entorno virtual

(`python -m venv entorno_virtual`, luego accede a este con `source/entorno_virtual/Scripts/activate`)

En la raiz del repositorio utiliza `pip install -r requirements.txt`

### 4.Crear base de datos

Deberas crear tu base de datos vacia, luego debes modificar el archivo "`Arranque/ecoenergy/example.env`", editando los siguientes parametros:
| Elemento | Descripcion |
| ----------- | ----------- |
| DJANGO_SECRET_KEY | Aqui va tu secret key |
| DJANGO_DEBUG | Para activar el modo Debug (True por defecto, False para desactivarlo). | 
|DB_ENGINE| Aca el motor de base de datos, MySQL o Sqlite (MySQL por defecto).|
|DB_NAME| El nombre de tu base de datos (El que le pusiste cuando la creaste).|
|DB_HOST| El host de tu base de datos (127.0.0.1 para trabajar de forma local).|
|DB_PORT| El puerto de tu base de datos (3306 para MySQL).|
|DB_USER| El usuario con el que se conectara (Asegurate de que tenga permisos sobre la base de datos).|
DB_PASSWORD| Contrasena del usuario.|

### 5.Migrar los modelos
En la raiz del projecto utiliza `python manage.py make migrations`, luego `python manage.py migrate`. Para confirmar que funciono, revisa tu base de datos, deberian aparecer las tablas.

### 6.Acceder a panel administracion

Primero crea un superusuario con (En la raiz del proyecto) `python manage.py createsuperuser` y completa el formulario.

luego accede a `<direccion>:<puerto>/admin` (Si estas trabajando localmente probablemente luzca algo como `127.0.0.1:8000/admin`).

E ingrasa tus credenciales


### 7.Insertar datos base (semillas)

En la raiz del proyecto ejecuta `python manage.py seed_catalog_es`.

