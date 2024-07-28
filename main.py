import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open('C:\Users\haris\Downloads\Data science Project\House Price Prediction\House_prediction_model.pkl','rb'))

st.header('Banglore House Prices Predictor')
data = pd.read_csv('C:\Users\haris\Downloads\Data science Project\House Price Prediction\Cleaned_data.csv')

loc = st.selectbox('Choose the location', data['location'].unique())
sqft = st.number_input('Enter Total Sqft')
beds = st.number_input('Enter No. of Bedrooms')
bath = st.number_input('Enter No of Bathrooms')
balc = st.number_input('Enter No of Balconies')

input = pd.DataFrame([[loc,sqft,bath,balc,beds]],columns=['location','total_sqft','bath','balcony','bedroom'])

if st.button("Predict Price"):
    output = model.predict(input)
    out_str = 'Price of the House is' + str(output[0]*100000) 