#import tensorFlow as tf
#from keras.models import load_model
import requests
import pickle
import streamlit as st
import numpy as np
import pandas as pd

#with open(r'best_model.h5','rb') as file:
 #   CHURN_module = load_model('best_model.h5')
#with open(r'scaler.pkl','rb') as file:
 #   scaler_module = pickle.load(file)

st.set_page_config(
    page_title="CUSTOMER CHURN PREDICTIONS",
    page_icon=":wave:",
    layout="centered",
    initial_sidebar_state="expanded",
  
)

st.sidebar.header("Enter Customer Details", divider='rainbow')

gender = st.radio("What is your gender",["Male","Female"])
SeniorCitizen = st.radio("Are you a senior citizen ",["YES","NO"])
tenure = st.slider("How long have you been a customer",1,100)
InternetService = st.radio("What is your internet service",["DSL","Fiber optic","No"])
OnlineSecurity = st.radio("Do you have online security",["YES","NO"])
OnlineBackup = st.radio("Do you have online backup",["YES","NO"])
TechSupport = st.radio("Do you have tech support",["YES","NO"])
Contract = st.radio("What is your contract",["Month-to-month","One year","Two year"])
PaymentMethod = st.radio("What is your payment method",["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"])
MonthlyCharges = st.slider("What is your monthly charges",0,120)
TotalCharges = st.slider("What is your total charges",0,10000)
submit =st.button("Submit")
user_response = [gender,SeniorCitizen,tenure,InternetService,OnlineSecurity,
                 OnlineBackup,TechSupport,Contract,PaymentMethod,MonthlyCharges,TotalCharges]

attributes = ['gender', 'SeniorCitizen', 'tenure', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'TechSupport', 'Contract',
       'PaymentMethod', 'MonthlyCharges', 'TotalCharges']
if submit:
        newData = pd.DataFrame([user_response],columns= attributes)
        scaledData = scaler_module.transform(newData)
        predict = CHURN_module.predict(scaledData)
        print(scaledData)
        st.subheader("The customer churn rate is "+str( round(predict[0])),divider='rainbow')
        print(predict[0]+(0.8809915725973115*1.96))
        print(predict[0]+(0.8809915725973115-1.96))
        st.text("There's a 95% chance that the rating is between " + str(round(predict[0]+(0.8809915725973115-1.96))) +" and "+str(round(predict[0]+(0.8809915725973115*1.96))))
