import streamlit as st
import plotly.express as px
from backend import get_data
import time

st.header('Weather Forecast for the next days')
st.text_input('City', key='city')
st.slider('Forecast Days', min_value=1, max_value=5, key='days', help='Select the number of forecasted days')
st.selectbox('Select data to show', options=['Temperature', 'Sky'], key='type', help='Choose if you want to see the forecast for the temperature or for the sky conditions')
city = st.session_state['city']
days = st.session_state['days']
fc_type = st.session_state['type']
st.subheader(f'{fc_type} for the next {days if days != 1 else ""} {"day" if days == 1 else "days" } in {city}')

if city:
    try:
        filtered_data = get_data(city, days)

        if fc_type == 'Temperature':
            temperatures = [(dict['main']['temp']-273.15) for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            labels = {'x': 'Date', 'y': 'Temperature (C)'}
            figure = px.line(x=dates, y=temperatures, labels=labels)
            st.plotly_chart(figure)

        if fc_type == 'Sky':
            sky_condition = [dict['weather'][0]['main'] for dict in filtered_data]
            images = {'Clear': 'images/clear.png',
                      'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png',
                      'Sun': 'images/sun.png'}
            images_path = [images[condition] for condition in sky_condition]

            st.image(images_path, width=150)
    except KeyError:
        warning = st.error('You selected a city that does not exist. Please choose a different city.')
        time.sleep(5)
        warning.empty()
