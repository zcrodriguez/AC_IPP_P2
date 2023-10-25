## Oct 25: 🛠️ Día de trabajo
### Preguntas y posibles mejoras
- Hacer un borrador de las visualizaciones que se quieren incluir en el dashboard.

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
