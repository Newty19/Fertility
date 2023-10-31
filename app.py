import streamlit as st
import pandas as pd
import joblib 

# Cargar el modelo entrenado
model = joblib.load('modelos/svm.pkl')  # Reemplaza 'tu_modelo_entrenado.joblib' con la ubicación de tu modelo
#Funciones para convertir inputs en variables viables
def temporadas(season):
    if(season == 'Invierno'):
        season = -1
    elif(season == 'Primavera'):
        season = -0.33
    elif(season == 'Verano'):
        season = 0.33
    else:
        season = 1
def fiebres(fiebre):
    if(fiebre == 'No'):
        fiebre = 1
    elif(fiebre =='Hace mas de 3 meses'):
        fiebre = 0
    else:
        fiebre = -1
def print_result(result):
    if(result == 0):
        return 'Fertilidad Alterada'
    else:
        return 'Fertilidad Normal'
    
# Configuración de la aplicación de Streamlit
st.title('App de Predicción de Fertilidad')
st.header('Configuración de Entrada')

# Widgets de entrada
age = st.number_input('Edad', min_value=1, max_value=36, value=25)
season = st.selectbox('Temporada', ('Invierno', 'Verano', 'Otoño', 'Primavera'))
childish_disease = st.checkbox('Enfermedad infantil')
accident = st.checkbox('Accidente o trauma grave')
surgical_int = st.checkbox('Intervencion Quirurgica')
fever = st.selectbox('Fiebres altas en el ultimo año', ('No','Hace mas de 3 meses', 'Hace menos de 3 meses'))
alcohol = st.checkbox('Es alcoholico')
smoker = st.checkbox('Es fumador')
sitting_hours = st.number_input('Horas sentado al dia', min_value=1, max_value=24, value=1)

# Realizar la predicción cuando se presione el botón
if st.button('Predecir'):
    input_data = pd.DataFrame({
        'Season': [temporadas(season)],
        'Age': [age/36],  # Ajusta esto para que coincida con las características de tu conjunto de datos
        'Childish Diseases': [int(childish_disease)],
        'Accident': [int(accident)],
        'Surgical': [int(surgical_int)],
        'High fevers': [fiebres(fever)],
        'Alcohol': [int(alcohol)],
        'Smoking': [int(smoker)],
        'Sitting Hours':[sitting_hours/24]
        # Agrega más columnas de características según sea necesario
    })
    input_data = input_data.fillna(0)
    prediction = model.predict(input_data)
    st.write('Resultado de la predicción:', print_result(prediction[0]))

    