import streamlit as st
from matplotlib import image
import os
import io
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data", "newdata_fifa.csv")
st.title(":red[FIFA Data Visualization]")
df = pd.read_csv(DATA_PATH)
col1=st.columns(1)
fig_1 = px.histogram(df,x=df['Age'],title='Players Age Distribution')
st.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.pie(df, names= df['IR'], hole=0.5, title='International Reputation Rating Pie Chart')
st.plotly_chart(fig_2,use_container_width=True)

fig_3 = px.bar(df,x = df['foot'],title='Preferred Foot')
st.plotly_chart(fig_3,use_container_width=True)

fig_4 = px.bar(df,x= df['BP'],title = 'Best playing position')
st.plotly_chart(fig_4,use_container_width=True)
fig_5 = px.scatter(df,x=df['Age'],y=df['POT'],title = 'Age vs Potential')
st.plotly_chart(fig_5,use_container_width=True)