import streamlit as st

import numpy as np
import pandas as pd

st.title("Welcome to SweetWalley Bakes")
st.header("SweetWalley|Nyonya Kuih")
st.subheader("Procut/Servie")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['Kuih Seri Muka', 'Kuih Bingka Ubi Kayu', 'Kuih Bingka Beras'])

st.line_chart(chart_data)


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

