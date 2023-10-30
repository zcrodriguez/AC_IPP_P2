### 🏇🏽 Orden de próximas tareas
- [x] Crear un lienzo en blanco para las visualizaciones.
    - [x] Crear un archivo `visualizaciones.py` para contener las visualizaciones.
    - [x] Temporalmente, trabajarlo de forma independiente al dashboard.
    - [x] Colocarle contenido dummie para probarlo.
    - [x] Hacer wireframes final de las visualizaciones para determinar qué datos se incluirán en la base de datos.
- [x] Crear una base de datos con los datos necesarios para las visualizaciones.
- Incorporar los datos a las visualizaciones de forma local.
- Subir los datos a base virtual e integrar.

## Oct 30: Analizando utilidad de visualizaciones
Estas visualizaciones proporcionan una herramienta poderosa para el monitoreo y la mejora continua de la calidad educativa en la universidad. Ayudan a la dirección
 académica a comprender mejor el rendimiento de los estudiantes y a tomar medidas basadas en datos para garantizar el éxito académico de sus estudiantes.

### ⚖️ ¿Cuál es el valor de las visualizaciones que he proyectado?
- **Diagrama de barras y Monitoreo del Éxito de Programas Académicos:** Las comparaciones entre carreras y el % de graduados y % de deserción académica por carrera 
ayudarían a evaluar la efectividad de los programas académicos individuales y realizar mejoras según sea necesario.
    - El seguimiento de la trayectoria de notas de los estudiantes a través de un diagrama Sankey proporciona una visión detallada de cómo los estudiantes progresan
     a lo largo de su educación. Esto puede ayudar a identificar puntos críticos en los que los estudiantes pueden necesitar apoyo adicional.
    - 🐴: Leí por ahí que el desempeño de los primeros dos semestres es un indicador claro de lo que espera el resto de la carrera. Vale la pena revisar esto
    y agregarlo a la justificación.
- **Sankey e identificación de Tendencias**: Las visualizaciones permiten a la dirección académica identificar tendencias a lo largo del tiempo.
Pueden detectar patrones en el rendimiento de los estudiantes y la deserción académica y tomar medidas proactivas en función de esas tendencias.
- **Identificación de Factores de Riesgo:** El análisis de la relación entre el éxito/deserción y variables como la beca o la deuda estudiantil puede ayudar a 
identificar factores de riesgo para la deserción académica. Esto permitiría a la dirección académica implementar programas de apoyo específicos para aquellos 
estudiantes en riesgo.

## Oct 28: Wireframes de visualizaciones
### 👩🏽‍🎨 Bocetos de visualizaciones
#### 🧰 Insumos
- [Diagrama de waffle/Icon Array](https://stackoverflow.com/questions/41400136/how-to-do-waffle-charts-in-python-square-piechart): Interesante opción para representar la deserción escolar usando como íconos los birretes de graduación.
- **Tarjetas:** Quizás para representar el número de estudiantes.
    - Opción 1: [Tarjetas con ícono según AnnMarieW](https://community.plotly.com/t/how-to-create-card-with-icon-on-the-right/51832/4)
    - Opción 2: [Tarjetas para KPI's](https://blog.finxter.com/plotly-dash-bootstrap-card-components/)
- **Gráficos de barras:** Para representar % de grados y deserción por programa de estudio.
- **Cheat sheets de visualización**:
    - **Hoja de referencia principal de hoy**: 
    - Múltiples opciones presentadas por [ML4Devs](https://www.ml4devs.com/newsletter/006-data-visualization-chart-cheatsheets/)
    - [Which Visualization?](https://experception.net/Franconeri_ExperCeptionDotNet_ChartChooser.pdf)
- **Diagrama Sankey**: https://www.data-to-viz.com/graph/sankey.html

### Otras ideas
- **Agrupar por escuelas:** Quizás se puedan separar los programas en Licenciaturas vs CTESP. También podrían verse los gráficos por escuela.
    - Encontré la [lista de programas de estudios](https://www.ipportalegre.pt/pt/oferta-formativa/?d=1) del IPP. Esta lista está conectada con [las escuelas que integran](https://www.ipportalegre.pt/pt/ensino/departamentos/).
    - Programa de estudios [versión infografía](https://www.ipportalegre.pt/media/filer_public/06/b3/06b393b2-9473-49fb-8094-661a2c5ac5ae/flyer_oferta_formativa_politecnico_portalegre_2023.pdf).

## Oct 26: 🤯 Implementación exitosa de persistencia de datos
### 🛠️ Implementación de persistencia de datos
- En uno de mis maravillosos viajes astrales descubrí que:
    - `persistence` es un atributo de los elementos de la app que permite que los datos se mantengan entre sesiones.
    - No funcionaba porque el botón `🧹Clear Form` estaba mal formulado y anulaba el efecto de la persistencia.
        - Corregí el botón funcionamiento del botón `🧹Clear Form` con la propiedad `prevent_initial_call` en el callback, la cual impide que el callback se ejecute al inicio de la app.
        Esto a su vez hace que la barra de progreso y el gauge se inicialicen correctamente.

## Oct 25: 🛠️ Multi-Page Apps v2
### 🤡 "Primera implementación exitosa de dcc.Store"
- Esto está entre comillas porque hice una prueba dummie con `visualizations.py` y funcionó.
- El problema de esta implementación es que pensaba que su éxito se debía a usar `dcc.Store` en lugar de `persistence`. Eso lo descubrí en la madrugada y se implementó
en el siguiente commit.

### 🛠️ Implementación de Multi-Page Apps with Pages v2 (Clean)
- Modifiqué el archivo `app.py` para contener la app multi-página.
- Creé archivo `test_app.py` para probar la app multi-página antes de implementarla en la app final.
    - Creé los archivos `home.py` y `visualizations.py`, almacenados en la carpega `pages/` para contener el contenido de cada página.
    - Añadí `__pycache__` a `.gitignore` para evitar que se suba a GitHub.

### 💔 Intento de implementación de dcc.Store
- Intenté utilizar todas las herramientas humanamente posibles para guardar la info del formulario. Fracasé estrepitosamente.
- Intenté usar `persistence`, `dcc.Store`y _callbacks_ sin éxito.
- Encontré [este artículo](https://stackoverflow.com/questions/63860623/plotly-dash-how-to-store-input-data-in-multipage-app) que explica revisiones que tengo que hacer a la forma del callback para que funcione.
- 🕯️ En [este repo](https://github.com/AnnMarieW/dash-multi-page-app-demos#7-multi_page_layout_functions) de Anne Marie W hay ejemplos de implementaciones que vale la pena mirar.

## Oct 24: 🛠️ Implementación de Multi-Page Apps without Pages v1 (Rústica)
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

## 💾 Flujo de trabajo detallado (Copia de seguridad) 
````mermaid
gantt
    title Proyecto 2 - Predicción de éxito académico
    dateFormat  YYYY-MM-DD
    section 🐜 Reuniones de trabajo
    💼 Repartición de tareas 1:2023-10-24 17:21,30m
    section 💪🏽 Grace - Modelo
    🔍 Entendimiento de la tarea:2023-10-24 16:30,40m
    🛠️ Implementación de aprendizaje de estructura: 2023-10-25 12:00, 5d
    section 🐴 Caro - Dashboard + Visualizaciones
    🔍 Entendimiento de la tarea:2023-10-20 8:00,4h
    📝 Lluvia de ideas y propósitos posibles para visualizaciones:2023-10-23,1d
    🛠️ Creación de app multi-página v1 (Rústica):2023-10-24,1d
    💔 Intento de implementación de dcc.Store:2023-10-25 6:30, 6h
    🛠️ Creación de app multi-página v2 (Clean):2023-10-25 21:00, 2h
    🤡 "Primera implementación exitosa de dcc.Store":2023-10-25 23:00, 1h
    🤯 Implementación exitosa de persistencia de datos:2023-10-26 00:00, 3h
    🔀 Merge y documentación de rama multipage-app-v2 y merge:2023-10-26 8:30, 1h
    📝 Mejoras en documentación y limpieza de código:2023-10-26 9:30, 40m
    📝 Construcción de wireframe:2023-10-28 8:30, 4h
     🤔 Decisiones sobre boceto de visualizaciones:2023-10-30 6:45, 2h
    🛠️ Creación de BD para visualizaciones (B1):2023-10-30 9:10, 2h
    🛠️ Creación de BD para visualizaciones (B2):2023-10-30 12:30, 1h
    🛠️ Creación de BD para visualizaciones (B3):2023-10-30 15:40, 1h
```