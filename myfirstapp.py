import streamlit as st

import numpy as np
import pandas as pd
import altair as alt
from PIL import Image
from datetime import datetime
import time



st.header("Welcome to SweetWalley Bakes")

readme = st.checkbox("readme first")

if readme:

    st.write("""
        You’re going to LOVE the authentic nyonya kuih from our panaderia! We provide free delivery for any purchase above RM50. Preorder yours today!)
        """)

    st.write ("For pre-order, please contact:")

    st.write("https://www.instagram.com/sweetwalley/?hl=en>", unsafe_allow_html=True)


option = st.selectbox(
      'How would you like to be contacted?',
      ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


start_time = st.slider(
       "When do you start your pre-order?",
        value=datetime(2020, 1, 1, 9, 30),
        format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)



st.header("Top Seller")
chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['Kuih Lapis', 'Seri Muka', 'Kuih Bingka Ubi'])

st._arrow_line_chart(chart_data)
    


st.header("Delivery Area")
chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['Putrajaya', 'Klang Valley', 'Cyberjaya'])

st.area_chart(chart_data)


st.header("Menu")
chart_data = pd.DataFrame(
       np.random.randn(50, 3),
       columns=["Ala-carte", "Kuih Box", "Special Gift"])

st.bar_chart(chart_data)



