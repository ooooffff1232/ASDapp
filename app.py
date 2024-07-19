import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
import json



def get_prediction(data={"A3":0,"A1":1,"A6":1,"A4":1,"A9":0,"A7":1,"A10":1,"Sex":"m","Family_mem_with_ASD":"no","A2":0,"A5":1,"A8":0,"Qchat-10-Score":5,"Jaundice":"no","Age_Mons":72,"Ethnicity":"asian","Class":"Yes"}):
  url = 'https://askai.aiclub.world/2b56adb4-7c6a-4fed-a234-cf4f778cd1b3'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  print(response)
  response = json.loads(response)
  response = json.loads(response["body"])
  response = response["predicted_label"]

  return response



#creating the web app

#title
st.title("ASD Project")

#dashboard
st.subheader("User Dashboard")

genderOptionsVal = ["Male","Female"]
ethnicityVl =["asian","White European","middle eastern","white","black","others","hispanic","latino","Pacifica","mixed","Native Indian","aboriginal","Turkish"]
jaundiceVal = ["no","yes"]
family_mem_with_ASD_val = ["No","yes"]
classval = ["no","Yes"]
A1 = st.selectbox("A1",(0,1))
A2 = st.selectbox("A2",(0,1))
A3 = st.selectbox("A3",(0,1))
A4 = st.selectbox("A4",(0,1))
A5 = st.selectbox("A5",(0,1))
A6 = st.selectbox("A6",(0,1))
A7 = st.selectbox("A7",(0,1))
A8 = st.selectbox("A8",(0,1))
A9 = st.selectbox("A9",(0,1))
A10 = st.selectbox("A10",(0,1))
Sex = st.selectbox("Gender",genderOptionsVal)
Ethnicity = st.selectbox("Ethnicity",ethnicityVl)
Jaundice = st.selectbox("jaundice",jaundiceVal)
family_mem_with_ASD_val = st.selectbox("Any family member with ASD",family_mem_with_ASD_val)
classval = st.selectbox("Class",classval)
age_Mons = st.slider("age_Mons",1,150,20)
Qchat_10_Score = st.slider("Qchat-10-Score",1,10,5)
if Sex ==genderOptionsVal[0]:
  Sex = "m"
else:
  Sex = "f"

input_data = {
               "A1":A1,
               "A2":A2,
               "A4":A4,
               "A5":A5,
               "A7":A7,
               "A8":A8,
               "A10":A10,
               "Sex":Sex,
               "Age_Mons":age_Mons,
               "Family_mem_with_ASD":family_mem_with_ASD_val,
               "Ethnicity":Ethnicity,
               "Class":classval,
               "A3":A3,
               "A6":A6,
               "A9":A9,
               "Qchat-10-Score":Qchat_10_Score,
               "Jaundice":Jaundice
}

prediction = get_prediction(input_data)
st.subheader(f"Education Type: {prediction}")
