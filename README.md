# Modelo de Predicción de Éxito Académico
Esta aplicación es un prototipo que utiliza un modelo de aprendizaje automático para predecir la probabilidad de éxito académico de un estudiante en función de ciertos parámetros socioeconómicos y académicos.

## Avance del proyecto
```mermaid
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
    🔍 Construcción de wireframe:2023-10-23,1d
    🛠️ Creación de app multi-página v1 (Rústica):2023-10-24,1d
    💔 Intento de implementación de dcc.Store:2023-10-25 6:30, 6h
    🛠️ Creación de app multi-página v2 (Clean):2023-10-25 21:00, 2h
    🤡 "Primera implementación exitosa de dcc.Store":2023-10-25 23:00, 1h
    🤯 Implementación exitosa de persistencia de datos:2023-10-26 00:00, 3h
```

## Requisitos
- Python 3.6 o superior
- Instalar las dependencias:
    - `Dash`
    - `Dash Bootstrap Components`
    - `Dash Bootstrap Templates`
    - `Pgmpy`

## Uso
1. Completa los parámetros en el formulario de la izquierda.
2. Observa la probabilidad de éxito académico en el gráfico de la derecha.
3. Ajusta los parámetros y observa cómo cambia la probabilidad de éxito académico.

## Estructura del Proyecto
- `assets/`: Directorio que contiene los recursos utilizados en la interfaz.
    - `logo-deca.png`: Logo creado para el proyecto.
    - `modelo_entrenado.pkl`: Modelo serializado entrenado con los datos de limpios.
    - `parameter_options.JSON`: Archivo JSON con las opciones de los menús desplegables.
- `Caro's_files/`: Carpeta que contiene archivos de experimentación y apuntes sobre investigación y avance del proyecto.
    - `P2_Notas_Dashboard.md`: Archivo que contiene notas sobre el avance del proyecto.
- `Pages/`: Carpeta que contiene los archivos de las páginas del dashboard.
    - `home.py`: Archivo que contiene el cuerpo de la página de inicio (app v.1.).
    - `visualizations.py`: Archivo que contiene el cuerpo de la página de visualizaciones.	
- `.gitignore`: Archivo que especifica los archivos que no se deben subir al repositorio.
- `app.py`: Código principal de la aplicación.

