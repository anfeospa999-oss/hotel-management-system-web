<div align="center">

# 🏨 Hotel Gales — Sistema de Gestión Hotelera Web
### **Solución Web para Administración Hotelera con Python, Flask y PostgreSQL**

[![Demo en Producción](https://img.shields.io/badge/Demo_En_Línea-htg.proyecto.lol-0052CC?style=for-the-badge&logo=google-chrome&logoColor=white)](https://htg.proyecto.lol)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_Framework-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker_Compose-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Ecosistema Desktop](https://img.shields.io/badge/Módulo_Escritorio-Java_Swing-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](https://github.com/anfeospa999-oss/hotel-management-system-desktop)

<p align="center">
  Módulo web del ecosistema Hotel Gales. Proporciona administración en tiempo real de habitaciones, reservas, huéspedes y facturación, compartiendo una base de datos PostgreSQL unificada con el cliente de escritorio en Java.
</p>

</div>

---

## 📌 Ecosistema Dual Hotel Gales

Este proyecto forma parte de una arquitectura dual donde dos aplicaciones independientes comparten y sincronizan datos sobre la misma base de datos PostgreSQL:

```text
                     🏨 HOTEL GALES (ECOSISTEMA)
                                │
              ┌─────────────────┴─────────────────┐
              ▼                                   ▼
      🌐 Módulo Web (Flask)              🖥️ Módulo Desktop (Java)
   [Repositorio Actual]               [hotel-management-system-desktop]
              │                                   │
              └─────────────────┬─────────────────┘
                                ▼
                   🗄️ PostgreSQL Centralizado
```

| Componente | Módulo Web (Este Repositorio) | [Módulo de Escritorio](https://github.com/anfeospa999-oss/hotel-management-system-desktop) |
| :--- | :--- | :--- |
| **Tecnología** | Python 3, Flask, Jinja2, Bootstrap 5.3 | Java 24, Swing, FlatLaf, JDBC |
| **Enfoque** | Acceso remoto, consultas web y administración ágil | Terminal de alta velocidad para recepción y auditoría |
| **Base de Datos** | PostgreSQL 16 unificada | PostgreSQL 16 unificada |

---

## ✨ Características Principales

- 🛏️ **Control de Habitaciones:** Monitoreo visual de disponibilidad, estados (disponible, ocupada, mantenimiento, limpieza) y tarifas por tipo.
- 📅 **Motor de Reservaciones:** Gestión de reservas, control de fechas de check-in / check-out y asignación de cuartos.
- 👤 **Gestión de Huéspedes:** Historial de clientes, registro de documentos de identidad y datos de contacto.
- 💵 **Facturación y Cobros:** Emisión y cálculo de cuentas, cargos adicionales por servicios y reportes de ingresos.
- 🔐 **Control de Acceso:** Sistema de autenticación con protección de rutas y permisos diferenciados por roles.
- 🐳 **Despliegue con Docker Compose:** Empaquetado completo listo para desplegar en servidores locales o en la nube.

---

## 🛠️ Stack Tecnológico

- **Backend:** Python 3.11+, Flask 3.0.
- **Base de Datos:** PostgreSQL 16.
- **Frontend:** HTML5, CSS3, JavaScript, Jinja2, Bootstrap 5.3.
- **Despliegue & Contenedores:** Docker, Docker Compose, Nginx.

---

## 📁 Estructura del Proyecto

```text
hotel-management-system-web/
├── app/
│   ├── models/        # Modelos relacionales y lógica de datos
│   ├── routes/        # Blueprints y controladores de endpoints
│   ├── static/        # Hojas de estilo CSS, JS y recursos multimedia
│   └── templates/     # Vistas dinámicas con Bootstrap y Jinja2
├── scripts/           # Scripts de mantenimiento y base de datos
├── config.py          # Configuración por entornos (Development / Production)
├── Dockerfile         # Definición del contenedor web
├── docker-compose.yml # Orquestación del servicio web y PostgreSQL
├── requirements.txt   # Dependencias de Python
└── run.py             # Script principal de ejecución
```

---

## 🚀 Despliegue y Ejecución

### Opción 1: Con Docker Compose (Recomendada)

1. Clona el repositorio:
   ```bash
   git clone https://github.com/anfeospa999-oss/hotel-management-system-web.git
   cd hotel-management-system-web
   ```

2. Inicia los servicios:
   ```bash
   docker compose up -d --build
   ```
   La aplicación estará disponible en `http://localhost:5000`.

### Opción 2: Entorno Local de Python

1. Crea y activa tu entorno virtual:
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux/macOS:
   source venv/bin/activate
   ```

2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Define tus credenciales de PostgreSQL en `config.py` o variables de entorno.

4. Inicia la aplicación:
   ```bash
   python run.py
   ```

---

## 👨‍💻 Autor

- **Andrés Felipe Ospina Pardo**
- GitHub: [@anfeospa999-oss](https://github.com/anfeospa999-oss)
- LinkedIn: [Andrés Ospina](https://www.linkedin.com/in/andres-ospina-5a382b413)

