# Panel de control tienda de ropa

Este proyecto fue realizado con Django


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

Abrir en el lavegador la siguiente URL:

```http://127.0.0.1:8000/login/```

##  Objetivo del proyecto

Mostrar una panel de gestion de stock de productos en una tienda de ropas. dependiendo el rol de quien se logea pueder realizar diferentes acciones.

hay tres roles disponibles:

* admin: puede agregar, eliminar, cambiar y consultar los productos.
* operador: unicamente puede cambiar un producto ya sea el stock o el nombre, pero no puede eliminar ni añadir otro producto.
* consultor: solo puede realizar consulta de productos pero no puede realizar ninguna otra accion.

hay usuarios predefinidos y la password es la misma para todos.
```
Usernames

admin:{
    JuanPE
}
Consultor:{
    RamonR
    Ferchu
}
Operador: {
    EduardoT
}

passwords:awds1234

```
