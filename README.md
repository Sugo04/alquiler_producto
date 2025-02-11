# alquiler_producto

El siguiente proyecto tiene como objetivo desarrollar un nuevo módulo 
para odoo que gestione el alquiler de los productos desarrollados en
ElectroWord

Lo vamos a dividir de la siguiente manera:

```
.
├── __init__.py
├── __manifest__.py
├── models
│   ├── alquiler_producto.py
│   └── __init__.py
├── README.md
├── security
│   └── ir.model.access.csv
├── static
│   ├── description
│   │   └── icon.png
│   └── src
└── views
    └── alquiler_producto_views.xml 

```
## Requisitos del módulo

```
1. Nombre del módulo: alquiler_producto.

2. Se deberá buscar un icono arbitrario que represente al módulo.

3. Funciones clave del módulo:

- Asignar al préstamo un cliente de la base de datos.

- Asignar al préstamo un producto de la base de datos siempre y cuando el producto esté disponible. Se utilizará para ello un decorador @api.onchange

- Asignar una fecha de inicio del préstamo

- Asignar de forma automática con un api.depends el final del préstamo (30 días a partir del inicio)

- Crear un estado para los préstamos (En Alquiler, Entregado, No Entregado) Con un "cron jobs" conseguiremos que No entregado aparezca siempre que hayan pasado los 30 días del préstamo.

- Campo sobre observaciones del préstamo

4. Roles: Solo los usuarios con el perfil de ventas pueden editar los préstamos, el resto sólo puede visualizarlos.

```