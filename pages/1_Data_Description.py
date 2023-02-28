import streamlit as st
from matplotlib import image
import os
import pandas as pd
st.title(':blue[FIFA Players Market Value Prediction]')

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "image", "image_1.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "newdata_fifa.csv")




img = image.imread(IMAGE_PATH)
st.image(img,width=700)

#df = pd.read_csv(DATA_PATH)
#st.dataframe(df)

st.header(":orange[Introduction]")
st.write("""Although football is the most popular sport worldwide, it is also a major industry. Numerous clubs generate significant revenue by nurturing young players and then selling them to larger clubs for substantial sums of money. The transfer of players has a significant influence on a club's potential success, with market values playing a crucial role in transfer negotiations. Our aim is to examine the data and pinpoint the key factors that impact the determination of a player's market value. Subsequently, we construct a model to forecast a player's market value, providing club managers with a valuable tool for negotiation.



""")
st.header(':red[Business Use Case]')
st.write("""Every year, football clubs invest a substantial amount of money in buying professional football players during the transfer window. One of the most challenging tasks for club managers is predicting player values in the transfer market. This project seeks to predict FIFA players' market values with precision, providing a baseline that simplifies the negotiation process and objectively estimates a player's market value in quantitative terms.""")

st.header("Dataset")
url = 'https://sofifa.com/'
st.markdown("""The data utilized in this analysis was scraped from sofifa({}) and comprises information on 18,179 players. The dataset comprises roughly 74 attributes, such as height, weight, age, preferred foot, skill moves, skill ratings, international reputation, and more. Each skill rating is divided into domains that are scored on a scale of 0 to 100. The skill ratings were scraped from the web by computing the mean of their respective domains. Below are the footballers' skill ratings and their corresponding domains.""".format(url))

st.header(':green[Attribute Description]')
st.markdown(
    """
    Given as:
    - Ball Skills: Ball Control, Dribbling
    - Passing: Crossing, Short Pass, Long Pass
    - Defense: Marking, Slide Tackle, Stand Tackle
    - Mental: Aggression, Reactions, Attack Position, Interceptions, Vision, Composure
    - Physical: Acceleration, Stamina, Balance, Sprint Speed, Agility, Jumping
    - Shooting: Heading, Short Power, Finishing, Long Shots, Curve, Free Kick, Accuracy, Penalties, Volleys
    - Goalkeeping: Positioning, Diving, Handling, Kicking, Reflexes
""")