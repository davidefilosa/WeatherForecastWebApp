import streamlit as st
import plotly.express as px
from backend import get_data

st.header('Weather Forecast for the next days')
st.text_input('City', key='city')
st.slider('Forecast Days', min_value=1, max_value=5, key='days', help='Select the number of forecasted days')
st.selectbox('Select data to show', options=['Temperature', 'Sky'], key='type', help='Choose if you want to see the forecast for the temperature or for the sky')
city = st.session_state['city']
days = st.session_state['days']
fc_type = st.session_state['type']
st.subheader(f'{fc_type} for the next {days if days != 1 else ""} {"day" if days == 1 else "days" } in {city}')


dates, temperatures = get_data(city, days, fc_type)

labels = {'x': 'Date', 'y': 'Temperature (C)'}
figure = px.line(x=dates, y=temperatures, labels=labels)
st.plotly_chart(figure)