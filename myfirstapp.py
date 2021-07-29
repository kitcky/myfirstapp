import streamlit as st
import numpy as np 
import pandas as pd 
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import pydotplus

from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot as plt 




st.sidebar.write("""
**This is a web app demo using python libraries such as Streamlit, Sklearn etc**
""")

st.sidebar.write ("Use this app to perform machine learning analysis and predict the species of the Palmer Penguins:")

st.sidebar.write ("<a href='https://www.kaggle.com/muhammadnoumangul/penguins-dataset'>Kaggle</a>", unsafe_allow_html=True)



option = st.sidebar.selectbox(
    'Kindly select the Menu here',
     ['Home','Penguin Prediction App'])

if option=='Home':
    st.write(f"# <font color='red'>Machine Learning</font>", unsafe_allow_html=True)
    
    st.header('*Introduction*')
    st. write("""
      **Machine learning (ML)** is the study of computer **algorithms** that improve automatically through experience and by the use of data.
        It is seen as a part of artificial intelligence. 

        Machine learning algorithms build a model based on sample data, known as **"training data"**, in order to make predictions or decisions without being explicitly programmed to do so.

        Machine learning algorithms are used in a wide variety of applications, such as in medicine, email filtering, speech recognition, and computer vision, where it is difficult or unfeasible to develop conventional algorithms to perform the needed tasks.

""")
    
    
    st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
    show = st.checkbox('I agree the terms and conditions')
    if show:
        st.write(f"<font color='Aquamarine'>Thank you for your response.Please select the Peguin Prediction App in the Menu for next action.</font>", unsafe_allow_html=True
        )

    

  
elif option=='Penguin Prediction App':
    st.write("""
    # Penguin Prediction App

    This app is used to predicts the **Palmer Penguin** species!
    """)

    st.sidebar.header('User Input Features')

    st.sidebar.markdown("""
    [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
    """)

    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file",type=["csv"])
    if uploaded_file is not None:
       input_df = pd.read_csv(uploaded_file)
    else:
        def user_input_features():
            island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgerson'))
            sex = st.sidebar.selectbox('Sex',('male','female'))
            bill_length_mm = st.sidebar.slider('Bill Length (mm)',32.1,59.6,43.9)
            bill_depth_mm = st.sidebar.slider('Bill depth (mm)',13.1,21.5,17.2)
            flipper_length_mm = st.sidebar.slider('Flipper Length (mm)', 172.0,231.0,201.0)
            body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
            data = {'island': island,
                    'bill_length_mm': bill_length_mm,
                    'bill_depth_mm' : bill_depth_mm,
                    'flipper_length_mm' : flipper_length_mm,
                    'body_mass_g' : body_mass_g,
                    'sex':sex}

            features = pd.DataFrame(data, index=[0])
            return features
        input_df = user_input_features()

    penguins_data = pd.read_csv('PENGUINS.csv')
    penguins = penguins_data.drop(columns=['species'])
    df = pd.concat([input_df,penguins],axis=0)


    encode = ['sex','island']
    for col in encode:
        dummy = pd.get_dummies(df[col],prefix=col)
        df = pd.concat([df,dummy], axis=1)
        del df[col]
    df = df[:1]


    st.subheader('User Input features')

  

 
    if uploaded_file is not None:
     st.write(df)
    else:
      st.write('Awaiting csv file to be uploaded, you may refer to the example CSV input file')
      st.write(df)


    load_clf = pickle.load(open('PENGUINS_clf.pkl','rb'))


    prediction = load_clf.predict(df)
    prediction_proba = load_clf.predict_proba(df)


    st.subheader('Prediction')
    penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
    st.write(penguins_species[prediction])
   

    st.subheader('Prediction Probability')
    st.write(prediction_proba)  


    st.subheader('Palmer Penguin Heatmap Plot')
    fig = plt.figure()
    sns.heatmap(penguins_data.corr(),annot=True, linewidths=.5)
    st.pyplot(fig)
    

