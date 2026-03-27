import pandas as pd
import numpy as np

import pickle as pk
import streamlit as st

model = pk.load(open('model.pkl', 'rb'))

st.title("🚗 Car Price Prediction Model")

st.write("Enter car details to predict the price")

car_data = pd.read_csv("car_data.csv")

present_price = st.slider("Present price(in lakhs)", 1.0, 50.0)
kms_driven = st.slider("Number of kms driven: ", 11, 200000)
fuel_type = st.selectbox("Fuel Type", car_data['Fuel_Type'].unique())
seller_type = st.selectbox("Seller Type", car_data['Seller_Type'].unique())
transmission = st.selectbox(
    "Transmission Type", car_data['Transmission'].unique())
owner = st.selectbox("Owner", car_data['Owner'].unique())
car_age = st.slider("Age of the Car: ", 0, 20)

fuel_map = {'Petrol': 1, 'Diesel': 0, 'CNG': 2}
seller_map = {'Dealer': 1, 'Individual': 0}
transmission_map = {'Manual': 0, 'Automatic': 1}

fuel_type = fuel_map[fuel_type]
seller_type = seller_map[seller_type]
transmission = transmission_map[transmission]

if st.button("Predict Price"):
    input_data = pd.DataFrame([[present_price, kms_driven, fuel_type, seller_type, transmission, owner, car_age]],
                              columns=['Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner', 'Car_Age'])

    prediction = model.predict(input_data)

    st.success(f"Predicted Selling Price: ₹ {prediction[0]:.2f} lakhs")
