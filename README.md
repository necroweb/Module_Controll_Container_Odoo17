# Modulo Odoo Controll_Containers 
    
    Odoo: v17 community,
    Python 3.12.0,
    postgres SQL server 18 

    Repo: https://github.com/necroweb/Module_Controll_Container_Odoo17.git
    
    Historial de commit:
        1d62c948 (HEAD -> main, origin/main) actualizacion dia 4 model y views
        ff417ba7 Modulo, tres modelos: shipping, vistas xml, tarif, range
        a4544215 repo container_ctl new module
        f2000f8f shanges image diagram proces
        da0b13f9 firts commit repo base


    Introduccion:
    Modulo desarrollado con ERP Odoo v17 para apoyo en area de coordinacion operativa Puerto Alto S.A.S (empresa ficticia). 
    
    objetivo: Gestionar contenedores marítimos, controlar sus estados, calcular tiempos de permanencia y administrar tarifas de         clientes y navieras. 

    -Alcance: Pasar la operacion comercial de excel a plataforma Odoo; Reduciendo sobrecostos operativos por informacion 
    faltante, mal calculo de tarifas y control de tiempos en la recepcion de container. 

# A-¿Cómo instalar nuevo modulo?;

    1- Ubícate en el directorio para clonar repositorio:
    https://github.com/necroweb/Module_Controll_Container_Odoo17.git
    2-cd Module_Controll_Container_Odoo17

    2- Verifica version python: 
        """ python --version """

    3- Crea el entorno virtual 
        python -m venv venv

    4- Activamos el entorno virtual
        - Desde powershell vscode:  
        """ venv\Scripts\activate.ps1 """    
        - Desde cmd: 
        """venv\Scripts\activate.bat"""
    
    5- Configurar PostgreSQL
        Parámetro /	Valor
        Host: localhost
        Puerto:	5433
        Usuario: odoo
        Base de datos (pruebas): container_mod

    6- Comprueno que postgreSQL funcione en el equipo
        """psql -h localhost -p 5433 -U odoo -d postgres"""
        consultar base de datos: """ \l """
        salir: """ \q """

        Si no existe base de datos:
        crearla desde pgAdmin4 o psql:
        """ CREATE DATABASE container_mod
            WITH OWNER odoo; """

    7- Configurar el archivo odoo.conf
        [options]

        ; Conexion PostgreSQL
        db_host = localhost
        db_port = 5433
        db_user = odoo
        db_password = puerto123
        database = container_mod

        ; Directorios de modulos: 
        addons_path = C:\Odoo17\odoo\odoo\addons,C:\Odoo17\odoo\addons,C:\Odoo17\odoo\custom_addons

        ; Puerto de acceso web
        http_port = 8017

    8- instalar modulo personalizado por primera vez:
        """ python .\odoo-bin -c .\odoo.conf -d container_mod -i container_ctl_mod --stop-after-init """ 

    9- Ejecutar servidor: 
        """ python .\odoo-bin -c .\odoo.conf -d container_mod """

    NOTA: Se  utiliza a modo de prueba user:admin y password:Admin1234 como credenciales de referencia, pero no debes asumir que serán las credenciales de tu instalación.

    10- actualizar modulo instalado: 
        """ python .\odoo-bin -c .\odoo.conf -d container_mod -u container_ctl_mod --stop-after-init """

# ¿Como probar nuevo modelo?

    Para realizar estas pruebas debemos ejecutar previamente nuestro servicios dentro del entorno virtual: 

    1- Inicialmente se ejecutan pruebas funcionales validando accesibilidad a la plataforma odoo, luego buscamos el nuevo modulo entre las categorias para este caso se adjunta a la categoria services como aparece en el archivo odoo.cong. 
    otra forma de validar es revisando la consola donde se compila el codigo, deberiamos obtener un mensaje similar donde nos indica version de odoo. 
    carga de base de datos, conexion httmp, puerto, carga de modulos, y carga de registro si existen. 

        mensaje terminal vs code: 
        """ 
        venv) PS C:\Odoo17\odoo> python .\odoo-bin -c .\odoo.conf -d container_mod               
        2026-11-13 23:35:09,074 27004 INFO ? odoo: Odoo version 17.0 
        2026-11-13 23:35:09,076 27004 INFO ? odoo: Using configuration file at C:\Odoo17\odoo\odoo.conf 
        2026-11-13 23:35:09,076 27004 INFO ? odoo: addons paths: ['C:\\Odoo17\\odoo\\odoo\\addons', 'c:\\users\\julia\\appdata\\local\\openerp s.a\\odoo\\addons\\17.0', 'c:\\odoo17\\odoo\\odoo\\addons', 'c:\\odoo17\\odoo\\addons', 'c:\\odoo17\\odoo\\custom_addons'] 
        2026-11-13 23:35:09,077 27004 INFO ? odoo: database: odoo@localhost:5433 
        2026-11-13 23:35:09,531 27004 INFO ? odoo.addons.base.models.ir_actions_report: You need Wkhtmltopdf to print a pdf version of the reports. 
        2026-11-13 23:35:09,991 27004 INFO ? odoo.service.server: HTTP service (werkzeug) running on JDark:8017 
        2026-11-13 23:35:10,121 27004 INFO container_mod odoo.modules.loading: loading 1 modules... 
        2026-11-13 23:35:10,165 27004 INFO container_mod odoo.modules.loading: 1 modules loaded in 0.04s, 0 queries (+0 extra) 
        2026-11-13 23:35:10,199 27004 INFO container_mod odoo.modules.loading: loading 12 modules... 
        2026-11-13 23:35:10,447 27004 INFO container_mod odoo.modules.loading: 12 modules loaded in 0.25s, 0 queries (+0 extra) 
        2026-11-13 23:35:10,492 27004 INFO container_mod odoo.modules.loading: Modules loaded. 
        2026-11-13 23:35:10,496 27004 INFO container_mod odoo.modules.registry: Registry loaded in 0.515s 
        
        """

     2- se pueden implementar pruebas manuales validando accesibilidad, funcionalidad y comportamiento de datos en diferentes acciones; registro, actualizacion y eliminacion de campos en cada uno de los modelos:
        -shipping_company --> registravos compañias navieras 
        -shipping_tariff --> registro de tarifas
        -shipping_tariff_range --> registros de tarifas por tramos
        -shipping_customer --> registrar clientes y sus condiciones
        -shipping_book_lading --> registrar libro de carga
        -shipping_container --> registro de container

# Modelo de datos: qué modelos creaste, cómo se relacionan y por qué;
    A- Modelo de datos
    
    Naviera
    └── Tarifas
            └── Tramos de tarifa

    Cliente
    └── Condiciones específicas por naviera

    BL / Embarque
    └── Contenedores

    b- Cómo funcionan las relaciones
    Naviera → Tarifas: una naviera puede tener varias tarifas; cada 
    
    tarifa pertenece a una naviera.
    Tarifa → Tramos: una tarifa puede tener varios tramos; cada tramo apunta a una tarifa.
    
    Cliente → Condiciones: un cliente puede tener varias condiciones, una para cada naviera.
    
    Naviera → Condiciones: una naviera puede aparecer en las condiciones de muchos clientes.
    
    BL → Contenedores: un BL puede tener varios contenedores; cada contenedor pertenece a un BL.

    Diagrama de claes: 
    <img width="680" height="672" alt="Diagrama_clases_container_mod" src="https://github.com/user-attachments/assets/c3440eb5-835f-45c3-91b5-9abb21f2133d" />



# Contradiccion encontrada: 

    Marcela (coordinadora operativa) Vs Jorge (Facturación)
    Existe una toma de decisiones no articulada con las reglas de negocio debido a que marcela registra fecha de ingreso del container y tiene encuenta el dia de descarega para calcular los dias libres, mientras que jorge inicia el 
    conteo sin tener encuenta el dia de descarga. 

    ¿ Decision tomada ?
    Tener en cuenta la fecha de descarga para contar los dias libres por que es la fecha con la que se registra el naviera y se hereda en la fecha incial de contendor. 

    para esta caso en la funcion se le sumo + dia mas al final 

    las preguntas que le harías al cliente antes de salir a producción;
    a- que son los EIR y TRM 
    b- que informacion los conforma. 

# Errores encontrados en la muestra Excel
    2-Atendiendo al documento de la prueba se conformo un excel de muestra y se ingreso en formato csv, validando errores por consola y normalizando formato para su ingreso.        

        -shipping.book.lading.csv
        -shipping.container.csv 
       
        Hallazgos: 
        1- Restriccion al subir registros por que no coincide texto con el campo tipo de container. 
        2- Restriccion por campo vacio en fecha de dovolucion cuando esta declarado como requerido en el modelo "date_return". 
        3- Diferentes formatos de fecha no validos con repecto al formato trabajado 
        dd/mm/aaaa
        4- Texto no coincide con el formato de texto de navieras y clientes
        5- formato no definido en el texto uppercase y lowercase


  # Resultados esperado caso 6 a 9
    Por tiempo y conocimientos tecnicos solo se resuleven del punto 1 al punto 3.
     
    1.Registrar navieras y sus tarifas por tipo de contenedor, con vigencia y tramos. Cadanaviera puede tener una cantidad distinta de tramos.
    2.Configurar por cliente sus días libres extra con cada naviera y su porcentaje deadministración.
    3.Registrar un BL con todos sus contenedores en una sola pantalla. La fecha de descargase toma del BL, pero cada contenedor puede tener la suya.

    4.No se realizan Calcular solo, por contenedor: días afuera, días libres, días de demora, cobro de lanaviera y cobro al cliente en dólares, según las reglas de negocio.
    5. se aplican solo dos reglas de negocio: 
    - Dias libres contando el dia de carga
    - Cargos especiales por cliente 
    - No se convierte moneda dolares  USD a COP pesos colombianos
    6. No se agregan estados al contenedor
    7. No se agrega campo para aduntar archivo EIR.
    8. No se condiciona el filtro 2 dias antes para el visualizar: vencidos, afuera y sin facturar
    9. No se crean grupos de permisos para facturacion o gerencia segun decision. 

    vista de datos en modelo container: 
    <img width="1259" height="511" alt="imagen" src="https://github.com/user-attachments/assets/45a375a7-42d9-4b50-84dd-5d42de7fc668" />

     comprobacion de tabla shipping_container en postgreSQL
     <img width="378" height="448" alt="imagen" src="https://github.com/user-attachments/assets/db63497a-7672-4580-aeb2-516742d0721f" />

    
# Flujo propuesto
    <img width="556" height="338" alt="Flujo_Container_propuesta drawio" src="https://github.com/user-attachments/assets/118b95df-18c0-4748-add8-6a144033ecb8" />
# Cronograma 
    1- git clone https://github.com/odoo/odoo.git
    2- Instalar requirement.txt y dependencias 
    3- crear entorno virtual: python -m venv venv
    4- Añadir atributos de conexion archivo odoo.conf
    5- Configurar base de datos en pgadmin4:
            -contraseña: puerto123
            -port: 5433
    6- GIT:
        git Branch main
        git add .
        git status
        git remote set-url origin https://github.com/necroweb/Module_Controll_Container_Odoo17.git
        git commit -m "first commit"
        git push origin main

    -> Plan de trabajo <-
        Día 1 -->
            T01 Instalación Odoo 17
            T02 Crear repositorio Git
            T03 Diagrama flujo operaciones 
            T04 Crear README inicia
            
        
    Día 2 -->
        T05 Diagrama flujo propuesta 
        T06 Estructura módelos - Diagrama clases
        T07 Crear archivo modelos
        T08 Nuevo modulo odoo: Configurar adomm-patch en odoo.conf
        actualizar repo:

    Dia 3 --> 
        T08 Backend- Definir Modelos
            -shipping.company -> OK
            -shipping.tariff -> OK
            -shipping.tariff.range -> OK
            actualizar repo:

    Dia 4 -->         
            -shipping_book_lading
            -shipping_container
            -shipping_customer
            -shippping_customer_condition
            actualizar repo:

    Dia 5 --> actualizar repo:
            -git branch
            -git status
            -git add.
            -git commit -m "mensaje commit"
            -git push origin main
            - pruebas funcionales
            - se documentan algunos casos de prueba
            - se suben registros de prueba excel de muestra

# Casos de estudio: Control de containers
    Puerto Alto SAS empresa ficticia requiere automatizar la gestion de containers: Actualmente se lleva control de  tiempos y  tarifas de manera manual registrando informacion en excel y no se lleva trazabilidad de container. Se han presentado algunas dificultades cuando no se encuentra fecha de salida de cada container en el area contable, debido a que el puerto debe asumir unos sobre costos si supera los dias estipulados en libro "BL" de contratos de la naviera.

# Diagrama de flujo de proceso
 Diagrama de procesos para llevar control de container Puerto Alto S.A.S
<img width="686" height="393" alt="Diagrama_flujo_Container drawio" src="https://github.com/user-attachments/assets/12d3ed11-748d-4b5f-b813-952d3ec2ca11" />


# Odoo

[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Documentation](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/17.0)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](https://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](https://nightly.odoo.com/)

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an [Open Source CRM](https://www.odoo.com/page/crm),
[Website Builder](https://www.odoo.com/app/website),
[eCommerce](https://www.odoo.com/app/ecommerce),
[Warehouse Management](https://www.odoo.com/app/inventory),
[Project Management](https://www.odoo.com/app/project),
[Billing &amp; Accounting](https://www.odoo.com/app/accounting),
[Point of Sale](https://www.odoo.com/app/point-of-sale-shop),
[Human Resources](https://www.odoo.com/app/employees),
[Marketing](https://www.odoo.com/app/social-marketing),
[Manufacturing](https://www.odoo.com/app/manufacturing),
[...](https://www.odoo.com/)

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured [Open Source ERP](https://www.odoo.com) when you install several Apps.

## Getting started with Odoo

For a standard installation please follow the [Setup instructions](https://www.odoo.com/documentation/17.0/administration/install/install.html)
from the documentation.

To learn the software, we recommend the [Odoo eLearning](https://www.odoo.com/slides),
or [Scale-up, the business game](https://www.odoo.com/page/scale-up-business-game).
Developers can start with [the developer tutorials](https://www.odoo.com/documentation/17.0/developer/howtos.html).

## Security

If you believe you have found a security issue, check our [Responsible Disclosure page](https://www.odoo.com/security-report)
for details and get in touch with us via email.
