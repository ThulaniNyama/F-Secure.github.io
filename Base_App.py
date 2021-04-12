
import streamlit as st
import joblib,os
import pandas as pd
import altair as alt
from PIL import Image
import numpy as np
import seaborn as sns

#df = pd.read_excel('Individual health and socio economic data.xlsx')

st.markdown("""
<style>
body {
    color: #fff;
    background-color: #808080;
}
</style>
    """, unsafe_allow_html=True)


#option at the side bar
menu = ["Home", "About The App", "Data Visualization", "Location"]
selection = st.sidebar.selectbox("Menu", menu)
    
if selection == "Home":
    st.title('Cape Town Traffic')
    # simple description
    st.write('We are the Safety belt to help ypu reach ypur destination with ease')
    st.write("Compliled by: Thulani Nyama")

    # display media
    image = Image.open('traffic Jam.jpg')

    st.image(image, use_column_width=True)
    st.write("Date: April/2021")
    # display media

# Building out the "About" page
if selection == "About The App":
    st.info("""The App gives you a high level defination of the Capetown Traffic using Twitter Data consumed from the CapetownFreeway account, it shows
    you the most popular hashtags used when traffic is reported in that account and the popular phrases used when people interact with the account, it 
    also give you the idea of the distrivuation of tweets per hour, to give you the idea how the time in the day correlates to the traffic, Fianlly you
    can see the excat location where traffic is""")
		
	# You can read a markdown file from supporting resources folder
    if st.checkbox("Introduction"):
        st.subheader("CONGESTION IN CAPE TOWN")
        st.info("""Congestion is a challenge for major cities across the world,and Cape Town is no exception.
        Our roads are getting more congested as the city’s economy grows and more people choose to live and work in Cape Town or visit as tourists.""")
	
			
	


# Building out the EDA page
if selection == "Data Visualization":


	#plot and visualize the highest school levels
	if st.checkbox("Tweets Per Hour"):
		st.info("We not that there is no correlation between the number of tweets posted to the hours the traffic occurs.")
		st.image('visuals/Tweets_per_hour.png', channels="BGR",use_column_width=True)

        


    #plot and visualize the count of people being admited at different health carea
	if st.checkbox("Which hashtags drives traffic conversations"):
		st.info("""We note that words such as stationery vehicles and roadworks were the most pupolar used phrases in April.""")
		st.image('visuals/word_cloud.png', channels="BGR",use_column_width=True)

if  selection == "Location":
    st.subheader('Google Maps')
data = pd.read_csv("./Cordinates_1.csv")

midpoint = (np.average(data['lat']), np.average(data['long']))


st.markdown("""
  <body>
    <div id="map"></div>

    <!-- Async script executes immediately and must be after any DOM elements used in callback. -->
    <script>
        var map;
        function initMap()
        {
            map = new google.maps.Maps(document.getElementById('map'), {
                center: {lat: -34.397, lng: 150.644}
                zoom: 8
            });
        }
    ></script>
    <style>
        #map {
            height: 100%;
        }
        html, body {
            height: 100%;
            margin: 0;
            padding: 0;
        }
    </style>
  </body>
    """, unsafe_allow_html=True)
# Building out the predication page
#if selection == "Predictions":
    #st.subheader("Naive Bayes Classifier ")
    #st.info("""KNeighbors Classifiers - implements classification based on voting by nearest k-neighbors of target point,
     #t, while RadiusNeighborsClassifier implements classification based on all neighborhood points within a fixed radius, r, of target point, t""")
     
     # Creating a text box for user input
    #def user_input_features():
        #gender = st.sidebar.selectbox('Gender', (2,1,3))
        # HealthStatus = st.sidebar.selectbox("Health status", (4,0,1,2,3))
        # Employer = st.sidebar.selectbox("Employer", (301,302,303,304,305,306,307,308))
        # PregnancyStatus=  st.sidebar.selectbox("PregnancyStatus'", (0,1,2,3,4))

        #data = {

            
                #'gender': gender,
                # 'HealthStatus':HealthStatus,
                # 'Employer': Employer,
                # 'PregnancyStatus': PregnancyStatus
                #}
        #features = pd.DataFrame(data,index=[0])
        #return features
	
    #st.sidebar.header('User Input Features')
    #input_df = user_input_features()
    
    #if st.button("Classify"):
        #predictor = joblib.load(open(os.path.join("G_Naive_Bayes_model.pickle"),"rb"))
        #st.write("""""")
       # prediction = predictor.predict(input_df)
        #st.success("Text Categorized as: {}".format(prediction))

        #if prediction[0] == 1:
            #st.success('The person does not consult to the traditional healers')
        #if prediction[0] == 2:
            #st.success('The person consults the traditional healers')
     
		






