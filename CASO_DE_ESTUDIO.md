# Caso de Estudio: Sistema Integrado de Feedback para "La Despistá"

![Banner Placeholder](/static/assets/la_despita_logo.jpg)

## 📌 Resumen Ejecutivo
Desarrollo y despliegue de un sistema digital de *customer feedback* (retroalimentación del cliente) para el negocio local "La Despistá". El proyecto digitaliza la recogida de opiniones mediante códigos QR situados físicamente en el local, conectándolos con un backend ágil alojado en la nube que procesa los datos para su posterior analítica estratégica.

---

## 1. El Problema de Negocio (El "Por qué")
Todo negocio local moderno necesita escuchar a su cliente, pero existen barreras significativas:
* **Fricción:** Pedir a los clientes que rellenen largas encuestas de papel o vayan a links complejos resulta en una tasa de respuesta nula.
* **Sesgo Público:** Las reseñas de Google o TripAdvisor son públicas. Una queja interna a menudo termina en una baja calificación pública si no se le da al cliente un canal de desahogo *privado y directo*.
* **Organización:** Las opiniones verbales a los empleados suelen perderse. Faltaba una base de datos unificada, tabulada y lista para ser analizada cuantitativamente.

---

## 2. La Solución (El "Qué")
La creación de una "pasarela de feedback" de escasa fricción:
1. **Punto de Entrada Físico:** Códigos QR de alta redundancia, serigrafiados e integrados en el local (mesas).
2. **Interfaz de Usuario (UI):** Una Web-App extremadamente ligera (carga casi instantánea con 4G/5G) con un diseño intuitivo *Mobile-First*.
3. **Clasificación en Tiempo Real:** El usuario categoriza su contacto (Sugerencia, Queja, Felicitación), lo que permite triage inmediato en la base de datos.

---

## 3. Arquitectura y Stack Tecnológico (El "Cómo")
Se ha primado la agilidad, la fiabilidad (sin caídas del servidor) y el bajo coste computacional usando el siguiente *Stack*:

### Frontend (User Interface)
* **HTML5 / CSS3 (Vanilla):** Sin frameworks pesados para garantizar un peso de descarga de apenas unos Kilobytes. Fundamental para dispositivos móviles.
* **JavaScript (Vanilla) & Fetch API:** El formulario se envía de manera asíncrona (AJAX). La pantalla no sufre el clásico y molesto "refresco/pantalla en blanco" al dar al botón enviar, ofreciendo confirmaciones animadas e instantáneas (Experiencia de Usuario / UX fluida).

### Backend (Lógica y Almacenamiento)
* **Python (Flask):** micro-framework elegido por su escalabilidad. El servidor actúa recibiendo los paquetes JSON asíncronos del frontend y parseándolos.
* **Bases de Datos Relacionales (SQLite3):** Enfoque *zero-configuration*. Al no necesitar conexiones expuestas, la base de datos de los clientes (con tablas tipificadas con campos dinámicos `categoria`, `email`, `consentimiento`) vive íntegramente protegida junto a la aplicación backend.

### Despliegue (Infraestructura Web)
* **PythonAnywhere (PaaS):** Despliegue del entorno en producción, resolviendo el ruteo relativo mediante *Web Server Gateway Interface* (WSGI) y albergando el motor servidor 24/7.
* **Cumplimiento Legal (RGPD):** Desarrollo de plantillas aisladas y lógica booleana en Base de Datos para asegurar la trazabilidad del consentimiento de privacidad del usuario según la normativa europea.

---

## 4. Retos Técnicos Superados
* **Ruteo Mixto Seguro:** Diferenciación en Flask entre *Assets Estáticos* (`/static`) para que los móviles descarguen la interfaz rápidamente, y vistas renderizadas (`render_template`) para evitar el visionado o exploración de directorios de la lógica de negocio.
* **Evolución del Esquema de Datos:** Ampliación dinámica del esquema inicial de *SQLite* para acoger nuevas casuísticas y parámetros empresariales, integrando todo ello de vuelta a los endpoints ya estructurados (prevención de rotura del servicio o *breaking changes*).

---

## 5. Próximos Pasos (Fase II: Analisis de Datos)* 
*(Para ser completado 30 días tras la inserción en producción)*

El sistema no termina en la recolección; la Fase II consiste en la toma de decisiones empresariales basadas en datos (Data-Driven Decisions).

**Pipeline Analítico Previsto:**
1. **Extracción y Transformación:** Descarga periódica del corpus SQLite desde la nube.
2. **ETL y Limpieza (Pandas):** Filtrado de datos atípicos, formateo y normalización.
3. **Visualización de Datos (Matplotlib / Seaborn):**
   * Gráficas de Pastel para analizar el medio de descubrimiento ("¿Cómo nos conoció?").
   * Gráficas de Barras temporales evaluando el Ratio (Felicitación vs. Queja).
   * Generación de *Nubes de Palabras (Wordclouds)* a partir de los campos abiertos de texto de Sugerencias.

---
> 💡 *Caso de Estudio documentado para la integración y despliegue del sistema La Despistá V1.0.*
