# La Despistá - Sistema de Feedback de Clientes

Este es un proyecto real y personal desarrollado para el negocio local "La Despistá" con el objetivo de implementar un sistema digital de recogida de feedback de los clientes. El sistema permite, a través de un formulario web (accesible, por ejemplo, mediante un código QR en el establecimiento), recopilar opiniones, sugerencias y datos de contacto de los clientes de manera estructurada en una base de datos para su posterior análisis estadístico.

Puedes consultar todos los detalles, el problema inicial y las métricas en el [Caso de Estudio](CASO_DE_ESTUDIO.md).

## Tecnologías Utilizadas

- **Frontend:** HTML, CSS y JavaScript (Vanilla). Se utiliza para construir la interfaz del formulario en el navegador del cliente y recopilar los datos para enviarlos asíncronamente al servidor.
- **Backend:** Python 3 interactuando mediante el framework web Flask y Flask-CORS. Es el responsable de levantar el servidor web, servir la página inicial y abrir los puntos de acceso (endpoints) para recibir la información en formato JSON enviada desde el frontend.
- **Base de Datos:** SQLite. Los datos de los clientes se guardan de forma local y ligera en un archivo relacional (`la_despista.db`), facilitando su posterior exportación o consulta. Se ha incluido soporte estructurado para registrar consentimientos de marketing y política de datos.
- **Análisis de Datos:** Jupyter Notebooks (`Resumen_Proyecto_Feedback.ipynb`), empleado para el estudio de las métricas y generación de reportes basados en la información recolectada de los comensales.

## Entorno y Estructura

El entorno de desarrollo está aislado utilizando entornos virtuales de Python (`.venv`), garantizando que no existan conflictos de dependencias en el sistema operativo anfitrión (Windows).

- **app.py:** Contiene toda la lógica principal de enrutamiento y conexión a la base de datos.
- **templates/:** Directorio en el que se ubican las plantillas principales (como `index.html`) para ser renderizadas por Flask.
- **static/:** Destinado a recursos estáticos que pueda requerir el frontend (hojas de estilo y scripts).

### Pasos para iniciar el entorno en local

1. Activar el entorno virtual de Python:
   ```bash
   .venv\Scripts\activate
   ```

2. Arrancar el servidor de desarrollo:
   ```bash
   python app.py
   ```

3. El servidor correrá localmente en modo "debug" a través del puerto 5000. Se puede acceder a la aplicación navegando a `http://localhost:5000` en cualquier navegador web.

## Consideraciones Relevantes del Proyecto

- **Separación de Responsabilidades (Separation of Concerns):** El proyecto sigue una clara división entre la interfaz de usuario (frontend), el controlador de rutas y almacenamiento (backend) y el análisis de datos (cuadernos de Jupyter). Todo el flujo de datos viaja de forma encapsulada de un extremo a otro, facilitando la escalabilidad del proyecto.
- **Auto-inicialización:** El código está preparado para detectar la ausencia de la base de datos `la_despista.db` durante el arranque de la aplicación y regenerar la tabla `clientes` de manera automática, de modo que el entorno puede desplegarse en una nueva máquina sin necesitar scripts adicionales de migración o configuración previa.
