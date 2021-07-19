import streamlit as st

import numpy as np
import pandas as pd
import time

st.header("Welcome to SweetWalley Bakes")

readme = st.checkbox("readme first")

if readme:

    st.write("""
        You’re going to LOVE the authentic nyonya kuih from our panaderia! We provide free delivery for any purchase above RM50. Preorder yours today!)
        """)

    st.write ("For pre-order, please contact:")

    st.write("https://www.instagram.com/sweetwalley/?hl=en>", unsafe_allow_html=True)
