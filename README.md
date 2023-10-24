# Modelo de Predicción de Éxito Académico
Esta aplicación es un prototipo que utiliza un modelo de aprendizaje automático para predecir la probabilidad de éxito académico de un estudiante en función de ciertos parámetros socioeconómicos y académicos.

## Avance del proyecto
```mermaid
gantt
    title Proyecto 2 - Predicción de éxito académico
    dateFormat  YYYY-MM-DD
    section 🐜 Reuniones de trabajo
    🔍 Entendimiento de la tarea:2023-09-10,1d
    💼 Repartición de tareas 1:2023-09-12 17:21,30min
    section 💪🏽 Grace - Modelo
    🔍 Entendimiento de la tarea:2023-09-10,1d
    section 🐴 Caro - Dashboard
    🔍 Structure Learning:2023-09-11,4d
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
- `.gitignore`: Archivo que especifica los archivos que no se deben subir al repositorio.
- `assets/`: Directorio que contiene los recursos utilizados en la interfaz.
    - `assets/logo-deca.png`: Logo creado para el proyecto.
    - `assets/modelo_entrenado.pkl`: Modelo serializado entrenado con los datos de limpios.
    - `assets/parameter_options.JSON`: Archivo JSON con las opciones de los menús desplegables.
- `app.py`: Código principal de la aplicación.

