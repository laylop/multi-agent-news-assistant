## Descripción del Proyecto

El **Asistente de Noticias Multiagente** está compuesto por varios agentes especializados:

1. **Agente de Rastreo**: Extrae noticias de fuentes web utilizando técnicas de scraping con `BeautifulSoup`.
2. **Agente de Procesamiento de Lenguaje Natural (PNL)**: Utiliza modelos de la librería `transformers` para resumir las noticias y analizar su sentimiento.
3. **Agente de Personalización**: Personaliza las noticias mostradas a los usuarios basándose en sus preferencias (aún en desarrollo).
4. **Agente de Interacción**: Gestiona las interacciones con los usuarios a través de la interfaz web, utilizando LangChain para mantener la conversación.

El sistema también cuenta con una **base de datos SQLite** para almacenar las noticias y un **servidor web** construido con **Flask** y **Chainlit** para la interfaz de usuario.

## Tecnologías Utilizadas

- **LangChain**: Para crear cadenas de conversación y gestionar el flujo del asistente de IA.
- **Chainlit**: Para crear la interfaz de usuario interactiva.
- **BeautifulSoup**: Para extraer noticias de sitios web mediante web scraping.
- **Transformers**: Para procesar el lenguaje natural (resumen y análisis de sentimiento).
- **Flask**: Para crear la interfaz web que interactúa con el asistente.
- **SQLite**: Para almacenar las noticias extraídas y procesadas.
- **NLTK**: Para análisis de sentimientos en el texto de las noticias.

## Instalación

Para instalar y ejecutar el proyecto en tu entorno local, sigue los siguientes pasos:

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/multi-agent-news-assistant.git
   cd multi-agent-news-assistant
   ```

2. **Instala las dependencias necesarias**:

   ```bash
   pip install langchain openai chainlit beautifulsoup4 requests transformers nltk flask
   ```

3. **Configura tu clave de API de OpenAI**:

   Asegúrate de tener una clave de API de OpenAI y configúralo en el archivo `config.py`.

   ```python
   # config.py
   OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
   ```

4. **Ejecuta la aplicación**:

   Inicia el servidor Flask:

   ```bash
   python interfaz/app.py
   ```

5. **Accede a la interfaz de usuario**:

   Abre tu navegador y dirígete a `http://127.0.0.1:5000/` para interactuar con el asistente.

## Funcionalidades

- **Rastreo de Noticias**: Extrae automáticamente las últimas noticias de fuentes como **El País** y **BBC News**.
- **Procesamiento de Noticias**: Utiliza modelos de IA para resumir las noticias y analizar su sentimiento (positivo, negativo, neutral).
- **Interacción con el Usuario**: Responde a las consultas del usuario sobre las noticias disponibles a través de un chat interactivo.
- **Personalización de Noticias**: (Próximamente) Proporcionará recomendaciones personalizadas basadas en los intereses del usuario.

## Contribución

Este proyecto está en constante desarrollo. Si deseas contribuir, por favor sigue estos pasos:

1. Forkea el repositorio.
2. Crea una rama con tu nueva funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube los cambios a tu repositorio (`git push origin feature/nueva-funcionalidad`).
5. Crea un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.

## Autor

**Laymon Lopez**  
Email: [info@laylop.com](mailto:info@laylop.com)  
Portfolio: [laylop.com](https://laylop.com)

## Agradecimientos

- A **LangChain** y **Chainlit** por sus poderosas herramientas para la creación de asistentes conversacionales.
- A los desarrolladores de **BeautifulSoup**, **Transformers**, y **Flask** por sus bibliotecas open-source que facilitan la creación de este sistema.
- A OpenAI por sus modelos avanzados de procesamiento de lenguaje natural.

---

Este README proporciona una visión general del proyecto **Multi-Agent News Assistant**. Si tienes alguna pregunta o sugerencia, no dudes en contactar conmigo.
