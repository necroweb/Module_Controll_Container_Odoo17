# MODULO CONTROL_DE_CONTAINER

Odoo: v17 community
Python 3.12.0
postgres SQL server 18 

Modulo desarrollado con ERP Odoo para apoyo en coordinacion operativa
Puerto Alto S.A.S (empresa ficticia) con el objetivo de gestionar y llevar
seguimiento ingrso y salida de container para tener control de tarifas 
establecidas por los los contratos de  naviera (cliente).

# CRACION REPO
1- git clone https://github.com/odoo/odoo.git
2- Instalar requirement.txt y dependencias 
3- crear entorno virtual: python -m venv venv
4- Añadir atributos de conexion archivo odoo.conf
5- Configurar base de datos en pgadmin4:
        -contraseña: puerto123
        -port: 5433


# EJECUCIÓN:
1- ingresamos a la raiz del proyecto 
    - Odoo/
2- Activamos el entorno virtual    
    - "venv\Scripts>activate.bat"
3- Ejecuta el comando para iniciar el servidor incluyendo el archivo de configuracion
    - "" python odoo-bin -c odoo.conf ""
4-Entra en tu navegador a http://localhost:8069
    

# CASO DE ESTUDIO: CONTROL DE CONTAINER  
Puerto Alto SAS empresa ficticia requiere automatizar la gestion de containers: Actualmente se lleva control de  tiempos y  tarifas de manera manual registrando informacion en excel y no se lleva trazabilidad de container. Se han presentado algunas dificultades cuando no se encuentra fecha de salida de cada container en el area contable, debido a que el puerto debe asumir unos sobre costos si supera los dias estipulados en libro "BL" de contratos de la naviera.

# DIAGRAMA DE FLUJO OPERACIONAL
<img width="686" height="393" alt="Diagrama_flujo_Container drawio" src="https://github.com/user-attachments/assets/12d3ed11-748d-4b5f-b813-952d3ec2ca11" />

# DIAGRAMA DE CLAES


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
