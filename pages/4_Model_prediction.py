import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "image", "image_3.jpeg")
DATA_PATH = os.path.join(dir_of_interest, "data", "newdata_fifa.csv")

st.title(":orange[FIFA market value Prediction]")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)



import pickle
#import streamlit.components.v1 as components

st.title('Fifa Player Market Value')
Age = st.number_input("Enter Age",0,100)
Best_overall = st.number_input("Enter Best Overall",0,100)
Overall_rating = st.number_input("Enter Overall Rating",0,100)
Potential = st.number_input("Enter Potential",0,100)

if st.button("Predict"):

    pickle_in = open(r'C:\Users\LENOVO X1 YOGA\Desktop\innomatics\project\resources\data\model_Random.pkl', 'rb') 
    r = pickle.load(pickle_in)
    
    X = pd.DataFrame([[Best_overall,Overall_rating,Potential,Age]], columns = ['Best_overall','Overall_rating','Potential','Age'])
    prediction = r.predict(X)
    
    st.success(f'The Market Value of Player is {prediction} Euro')

    st.balloons()


