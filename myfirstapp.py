import streamlit as st 
import numpy as np 
import pandas as pd

#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import classification_report

st.title("Welcome to SweetWalley Bakes")
st.header("SweetWalley|Nyonya Kuih")
st.subheader("Procut/Servie")

st.sidebar.write("""
        You’re going to LOVE the authentic *nyonya kuih* from our panaderia! We provide free delivery for *any purchase above RM50*. Preorder yours today!)
        """)
st.write ("For pre-order, please contact:")

st.write("https://www.instagram.com/sweetwalley/?hl=en>", unsafe_allow_html=True)



