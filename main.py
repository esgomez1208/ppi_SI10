import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Cargar el conjunto de datos
df = pd.read_csv('DailyDelhiClimateTrain.csv')

# Configurar la aplicación Streamlit
st.title('Análisis de Datos Climáticos')
st.write('Este aplicativo está destinado a explorar y comprender los datos meteorológicos en Delhi, India'\
        'de una manera accesible e interactiva, brindando una experiencia que permite descubrir'\
            ' y entender los patrones climáticos a través de la visualización'\
                ' y el análisis exploratorio de datos.')
st.write("### Visualización de Datos Climáticos")

# Mostrar una tabla con los datos
st.write("#### Tabla de Datos")
st.write(df)  # Muestra los datos en una tabla

# Visualización de la temperatura a lo largo del tiempo
st.write("#### Gráfico de Temperatura a lo largo del Tiempo")
st.line_chart(df.set_index('date')['meantemp'])
# Aquí puedes usar matplotlib, seaborn o plotly para graficar la temperatura en función del tiempo


# Convertir la columna 'date' a tipo datetime
df['date'] = pd.to_datetime(df['date'])

# Calcular promedio mensual de temperaturas
df['month'] = df['date'].dt.month
monthly_avg = df.groupby('month')['meantemp'].mean()

# Mostrar promedio mensual de temperaturas
st.line_chart(monthly_avg)


# figura
fig, ax = plt.subplots()
