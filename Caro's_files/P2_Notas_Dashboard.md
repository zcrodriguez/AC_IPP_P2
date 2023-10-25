## Oct 25: 🛠️ Día de trabajo
### Preguntas y posibles mejoras
- Revisar la posibilidad de usar `dcc.Store` o `Tabs` en vez de `Pages` para la navegación entre páginas.
    - ¿Cómo hacer que el `dcc.Store` se actualice con los valores del formulario?
- En caso de continuar las páginas, utilizar los elementos dbc.Page y dbc.PageLayout para crear las páginas.
- Hacer un borrador de las visualizaciones que se quieren incluir en el dashboard.

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
