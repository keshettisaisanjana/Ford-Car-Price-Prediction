import streamlit as st 
import pandas as pd
import joblib
       
model=joblib.load("Ford_Car_Model copy.pkl")
columns=joblib.load("Ford_Car_Columns copy.pkl")

st.title("Ford-Car-Price-Prediction")
st.markdown("provide following details")

model_select=st.selectbox("model",[' Fiesta',' Focus', ' Puma', ' Kuga', ' EcoSport' ,' C-MAX' ,' Mondeo' ,' Ka+',
 ' Tourneo Custom', ' S-MAX', ' B-MAX', ' Edge', ' Tourneo Connect',
 ' Grand C-MAX', ' KA' ,' Galaxy' ,' Mustang', ' Grand Tourneo Connect',
 ' Fusion', ' Ranger', ' Streetka', ' Escort' ,' Transit Tourneo', 'Focus'])
year=st.slider("year",2010,2026,2016)
transmission=st.selectbox("transmission",['Automatic','Manual','Semi-Auto'])
mileage=st.slider("mileage",0,10000,50000)
fuelType=st.selectbox("fueltype",['Petrol','Diesel' ,'Hybrid' ,'Electric' ,'Other'])
tax=st.slider("tax",0,600,300)
mpg=st.slider("mpg",20.8,201.8,50.0)
engineSize=st.slider("enginesize",0.0,3.7,2.2)

if st.button("predict Price"):
    input_df = pd.DataFrame({
        "model":[model_select],
        "year":[year],
        "transmission":[transmission],
        "mileage":[mileage],
        "fuelType":[fuelType],
        "tax":[tax],
        "mpg":[mpg],
        "engineSize":[engineSize]
    })
    
    input_encoded = pd.get_dummies(
        input_df,
        columns=["model", "transmission", "fuelType"],
        drop_first=True,
        dtype=int
    )

    input_encoded = input_encoded.reindex(
        columns=columns,
        fill_value=0
    )

    prediction = model.predict(input_encoded)

    st.success(f"Estimated Car Price: ₹ {prediction[0]:,.2f}")