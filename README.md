# 🧩 Mini ERP PyData — Simulador de Implementación SAP

Este proyecto fue creado con el objetivo de **aprender Flask, PostgreSQL, Docker y despliegue en la nube**, simulando un entorno real de **implementación de proyectos SAP**.  
La idea es combinar la gestión de proyectos tipo ERP con un enfoque educativo y práctico, simulando las fases de **SAP Activate** (Prepare, Build, Test, Cutover, Go Live).

---

## 🎯 Objetivos del proyecto

- Aprender a desarrollar una aplicación web y de consola con **Flask**.
- Conectarla a una base de datos **PostgreSQL**.
- Dockerizar el proyecto para portabilidad y despliegue.
- Publicarlo como un **SaaS gratuito** en la nube (Render o Railway).
- Documentar el proceso completo de desarrollo, buenas prácticas y licencia MIT.

---

## 🏗️ Arquitectura del proyecto

```bash
mini_erp_pydata/
│
├── app/
│   ├── __init__.py          # Inicialización del app Flask
│   ├── models.py            # Modelos SQLAlchemy (DB)
│   ├── routes.py            # Endpoints Flask
│   ├── cli.py               # Comandos en consola
│   ├── templates/           # HTML con Jinja2
│   └── static/              # CSS, JS, imágenes
│
├── config.py                # Configuración general
├── requirements.txt         # Dependencias del proyecto
├── Dockerfile               # Imagen Docker
├── docker-compose.yml       # Orquestación Docker
├── .env                     # Variables de entorno (DB, secret key)
├── README.md                # Documentación (este archivo)
└── LICENSE                  # Licencia MIT
