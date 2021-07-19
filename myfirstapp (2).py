import streamlit as st 
import numpy as np 
import pandas as pd


st.title("Welcome to SweetWalley Bakes")
st.header("SweetWalley|Nyonya Kuih")
st.subheader("Procut/Servie")

st.sidebar.write("""
You’re going to LOVE the authentic *nyonya kuih* from our panaderia! We provide free delivery for *any purchase above RM50*. Preorder yours today!)
""")
st.sidebar.write ("For pre-order, please contact:")

st.sidebar.write("https://www.instagram.com/sweetwalley/?hl=en>", unsafe_allow_html=True)


st.subheader("SweetWalley|Best Seller")
df = pd.DataFrame(
     np.random.randn(10, 10),
     columns=('col %d' % i for i in range(10)))

>>> st.dataframe(df)  # Same as st.write(df)


st.subheader("SweetWalley|Delivery Area")
>>> df = pd.DataFrame(
...     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
...     columns=['lat', 'lon'])
>>>
>>> st.map(df)


>>> genre = st.radio(
...     "What's your favorite Nyonya Kuih",
...     ('Seri Muka', 'Kuih Bingka Ubi Kayu', 'Kuih Talam'))
>>>
>>> if genre == 'Seri Muka':
...     st.write('You selected Seri Muka.')
... else:
...     st.write("You didn't select Seri Muka.")


>>> option = st.selectbox(
...     'How would you like to be contacted?',
...     ('Email', 'Home phone', 'Mobile phone'))
>>>
>>> st.write('You selected:', option)



