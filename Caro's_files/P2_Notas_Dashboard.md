## Oct 25: 🛠️ Día de trabajo
### 🏇🏽 Orden de próximas tareas
- Crear un lienzo en blanco para las visualizaciones.
    - Crear un archivo `visualizaciones.py` para contener las visualizaciones.
    - Temporalmente, trabajarlo de forma independiente al dashboard.
    - Colocarle contenido dummie para probarlo.
    - Hacer wireframes final de las visualizaciones para determinar qué datos se incluirán en la base de datos.
- Crear una base de datos con los datos necesarios para las visualizaciones.
    - De acuerdo con el wireframe, limpiar la base de datos.
- Incorporar los datos a las visualizaciones de forma local.
- Subir los datos a base virtual e integrar.

### 🛠️ Implementación de Multi-Page Apps with Pages
- Modifiqué el archivo `app.py` para contener la app multi-página.
- Creé archivo `test_app.py` para probar la app multi-página antes de implementarla en la app final.
    - Creé los archivos `home.py` y `visualizations.py`, almacenados en la carpega `pages/` para contener el contenido de cada página.
    - Añadí `__pycache__` a `.gitignore` para evitar que se suba a GitHub.

### 💔 Intento de implementación de dcc.Store
- Intenté utilizar todas las herramientas humanamente posibles para guardar la info del formulario. Fracasé estrepitosamente.
- Usé persistence, dcc.Store, callbacks, y hasta intenté guardar la info en un archivo JSON sin éxito.
- Encontré [este artículo](https://stackoverflow.com/questions/63860623/plotly-dash-how-to-store-input-data-in-multipage-app) que explica revisiones que tengo que hacer a la forma del callback para que funcione.
- 🕯️ En [este repo](https://github.com/AnnMarieW/dash-multi-page-app-demos#7-multi_page_layout_functions) de Anne Marie W hay ejemplos de implementaciones que vale la pena mirar.

## Oct 24: 🛠️ Implementación de Multi-Page Apps without Pages
### 👩🏽‍🎨 Creación de app multi-página
- Encapsulé el contenido original de la app en la función `home_contents()` que retorna el `html.Div` de la página correspondiente.
- Creé una nueva página en blanco (Page 1).
- Creé los hipervínculos en la navigation bar para cada página.
- Creé una función que cambia el contenido de la página según el hipervínculo seleccionado.
- 👁️ En [Multi-Page Apps and URL Support](https://dash.plotly.com/urls#dynamically-create-a-layout-for-multi-page-app-validation) explican una solución más elegante que vale la pena explorar.

## Oct 23: ⛈️ Investigación y lluvia de ideas
### 👩🏽‍🎨 Avances en: Adiciones obligatorias al dashboard
- Se creó en un `canvas` de **🪨 Obsidian** moodboard/wireframe de visualizaciones sobre éxito académico.
    - Debe agregarse un nuevo tab/página al dashboard para contener las visualizaciones.
        - En caso de agregarse página (mejor opción), se debe agregar un hipervínculo en la navigation bar.
- En mi WhatsApp personal y en mi libreta dejé una lista de insights/conceptos que justificarían la necesidad de las visualizaciones.

### 🤔 Opcionales: modificaciones al dashboard
- Enriquecer visualmente las pestañas de servicios estudiantiles:
    - Convertir los servicios estudiantiles en una galería o minicards.
    - Agregar un botón de "ver más" para cada servicio estudiantil.   
