# CRM Básico - Proyecto Django

![Django](https://img.shields.io/badge/Django-v4.2-green) ![Python](https://img.shields.io/badge/Python-3.10-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Descripción

Este es un sistema **CRM (Customer Relationship Management)** desarrollado con **Django** para la gestión de clientes, empresas e interacciones comerciales.  
El objetivo es ofrecer una plataforma sencilla, moderna y responsive para que cualquier negocio pueda organizar su información comercial y tomar decisiones basadas en datos.

Incluye un **dashboard interactivo** con estadísticas en tiempo real y visualizaciones gráficas usando **Chart.js** y estilos con **Bootstrap 5**.

---

## ✨ Funcionalidades

- Registro y autenticación de usuarios (login/logout).
- Gestión de **clientes**, **empresas** y **tipos de interacciones**.
- Dashboard con:
  - 📊 **Gráfico de pastel**: Interacciones por tipo.
  - 📊 **Gráfico de barras**: Clientes por empresa.
  - 📈 **Gráfico de líneas**: Interacciones por mes.
  - 📌 Contadores de clientes, empresas e interacciones.
- Interfaz responsive con **Bootstrap 5**.
- Sistema de mensajes y alertas para acciones de usuario.

---

## 🚀 Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/tuusuario/Proyecto_CRM_Django.git
    cd Proyecto_CRM_Django
    ```

2. Crear y activar entorno virtual:
    ```bash
    python -m venv env
    source env/bin/activate  # Linux/macOS
    env\Scripts\activate     # Windows
    ```

3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Configurar variables de entorno (opcional, como `SECRET_KEY`, `DEBUG`, `DATABASE_URL`).

5. Aplicar migraciones:
    ```bash
    python manage.py migrate
    ```

6. Crear superusuario (opcional, para acceder al panel de administración):
    ```bash
    python manage.py createsuperuser
    ```

7. Ejecutar el servidor:
    ```bash
    python manage.py runserver
    ```

8. Abrir en el navegador: [http://localhost:8000](http://localhost:8000)

---

## 🖥️ Uso

- Inicia sesión o regístrate.
- Agrega empresas y clientes.
- Registra interacciones (llamadas, correos, reuniones, etc.).
- Visualiza estadísticas en el Dashboard.
- Administra todos los datos desde el panel de Django Admin.

---

## 🛠️ Tecnologías

- **Python 3.10**
- **Django 4.x**
- **Bootstrap 5**
- **Chart.js**
- **SQLite** (por defecto, fácil de cambiar a PostgreSQL, MySQL, etc.)

---

## 👨‍💻 Autor

**Lomello Baltasar** – [baltasarlomello@live.com](mailto:baltasarlomello@live.com)  

Sígueme en [GitHub](https://github.com/Balti2003)

---

¡Gracias por visitar el proyecto! 🚀
