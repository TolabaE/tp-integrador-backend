# Panel de control tienda de ropa

*** Este proyecto fue realizado con


## Pasos a seguir para levantar el servidor en tu ordenar.

* una vez copiado la url de github, abrimos la terminal del visual y usamos el siguiente comando.

```git clone https://github.com/TolabaE/tp-integrador-backend.git```

### 1. Crear el entorno virtual

Es fundamental para aislar las librerías. En la carpeta raíz del proyecto (donde está manage.py), ejecuta:

+ Crear entorno
```
python -m venv venv
```
+ activar el entorno
```
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```
### 2. Instalar las dependencias

Como el proyecto esta realizado con Django necesitas instalar las dependecias que se encuentran en el archivo requirements.txt

```
pip install -r requirements.txt
```

### 3.Levantar el servidor
Como en el proyecto actual si esta copiada la base de datos no es necesario realizar la migracion ni crear una base de datos nueva. simplemente arrancamos.

```
python manage.py runserver
```