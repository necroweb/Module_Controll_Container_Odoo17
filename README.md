# Modulo Controll_Container 

Odoo: v17 community,
Python 3.12.0,
postgres SQL server 18 

Modulo desarrollado con ERP Odoo v17 para apoyo en area de coordinacion operativa
Puerto Alto S.A.S (empresa ficticia). El objetivo:  Facilitar la gestion container, llevando control de  seguimiento para ingreso, depositos y salidas durante su descarga en el puerto. 
Alcance: Reducir sobrecostos por mal calculo de tarifas y tiempos en la recepcion de container. 

Contradiccion encontrada: 
Marcela (coordinadora operativa) Vs Jorge (Facturación)
Existe una toma de decisiones no articulada con las reglas de negocio debido a que marcela 
registra fecha de ingreso del container y tiene encuenta el dia de descarega para calcular los dias libres, mientras que jorge inica el conteo sin el dia de descarga. 

# Creación de repo
1- git clone https://github.com/odoo/odoo.git
2- Instalar requirement.txt y dependencias 
3- crear entorno virtual: python -m venv venv
4- Añadir atributos de conexion archivo odoo.conf
5- Configurar base de datos en pgadmin4:
        -contraseña: puerto123
        -port: 5433
6- GIT:
    git Branch main
    git add.
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

Dia 3 --> 
    T08 Backend- Definir Modelos
        -shipping.line
        -shipping.line.tariff
        -shipping.line.tariff.range
        -customer.shipping.condition
        -demurrage.bl
        -demurrage.container    


# Ejecución:
1- ingresamos a la raiz del proyecto 
    - Odoo/
2- Activamos el entorno virtual    
    - "venv\Scripts\activate.bat"
    "venv\Scripts\activate.ps1"
3- iniciar el servidor: incluyendo el archivo de configuracion
    - "" python odoo-bin -c odoo.conf ""
   
4-Entra en tu navegador a http://localhost:8017
5-Iniciar sesion login Odoo
    Usuario: admin
    Contraseña: Admin1234

6- Crear Modulo Container_ctl_mod 
se vincula con el archivo odoo.conf
; Directorios de modulos
addons_path = C:\Odoo17\odoo\odoo\addons,C:\Odoo17\odoo\addons,C:\Odoo17\custom_addons

# Comando de pruebas
Ingresar psql terminal:
    "psql -h localhost -p 5433 -U odoo postgres"  

crear tablas bd odoo = container_mod
    "python odoo-bin -c odoo.conf -d container_mod -i base"

# Casos de estidio: Control de container
Puerto Alto SAS empresa ficticia requiere automatizar la gestion de containers: Actualmente se lleva control de  tiempos y  tarifas de manera manual registrando informacion en excel y no se lleva trazabilidad de container. Se han presentado algunas dificultades cuando no se encuentra fecha de salida de cada container en el area contable, debido a que el puerto debe asumir unos sobre costos si supera los dias estipulados en libro "BL" de contratos de la naviera.

# DIAGRAMA DE FLUJO OPERACIONAL
<img width="686" height="393" alt="Diagrama_flujo_Container drawio" src="https://github.com/user-attachments/assets/12d3ed11-748d-4b5f-b813-952d3ec2ca11" />

# Modelo de datos
res.partner (Cliente)
│
├── customer_shipping.condition
│   ├── customer_id
│   ├── shipping_id
│   ├── extra_free_days
│   └── admin_percentage
│

shipping.company (Naviera)
│
├── shipping.tariff
│   ├── shipping_id
│   ├── container_type
│   ├── date_from
│   ├── date_to
│   └── tariff_range_ids
│
└── shipping.tariff.range
    ├── tariff_id
    ├── sequence
    ├── day_from
    ├── day_to
    └── price_usd


book.lading (BL)
│
├── bl_number
├── customer_id
├── shipping_id
├── arrival_date
├── discharge_date
├── container_ids
└── state

container.record
│
├── container_number
├── container_type
├── bl_id
├── customer_id
├── shipping_id
├── discharge_date
├── return_date
├── eir_file
├── eir_filename
│
├── days_out
├── free_days
├── delay_days
│
├── shipping_cost_usd
├── customer_cost_usd
│
├── carrier_invoice_id
│
└── state

carrier.invoice
│
├── container_id
├── invoiced_usd
├── calculated_usd
├── difference_usd
└── state

# Rf
Requeriientos Funcionales: 

RF01
Operaciones (Marcela)

Crear BL
Registrar contenedores
Registrar descarga
Registrar devolución
Adjuntar EIR
Consultar vencimientos

RF02
Facturación (Jorge)

Configurar tarifas
Revisar demoras
Registrar valor facturado por naviera
Facturar cliente
Bloquear modificaciones

RF03
Gerencia (Patricia)

Consultar reportes
Consultar rentabilidad
Consultar diferencias con navieras


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
