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
A1 = st.selectbox("Does your child look at you when you call his/her name?",("no","Yes"))
if A1 ==["no"]:
  A1 = 0
else:
  A1 = 1
A2 = st.selectbox("Is it easy for you to get eye contact with your child?",("no","Yes"))
if A2 ==["no"]:
  A2 = 0
else:
  A2 = 1
A3 = st.selectbox("Does your child point to indicate that s/he wants something?",("no","Yes"))
if A3 ==["no"]:
  A3 = 0
else:
  A3 = 1
A4 = st.selectbox("Does your child point to share an interest with you?",("no","Yes"))
if A4 ==["no"]:
  A4 = 0
else:
  A4 = 1
A5 = st.selectbox("Does your child pretend? e.g. care for dolls, talk on a toy phone?",("no","Yes"))
if A5 ==["no"]:
  A5 = 0
else:
  A5 = 1
A6 = st.selectbox("Does your child follow where you are looking?",("no","Yes"))
if A6 ==["no"]:
  A6 = 0
else:
  A6 = 1
A7 = st.selectbox("If you or someone else in the family is visibly upset, does your child show signs of waning to comfort them? e.g. stroking hair, hugging them)",("no","Yes"))
if A7 ==["no"]:
  A7 = 0
else:
  A7 = 1
A8 = st.selectbox("Would you describe your child's first word as:",("no","Yes"))
if A8 ==["no"]:
  A8 = 0
else:
  A8 = 1
A9 = st.selectbox("Does your child use simple gestures (e.g.wave goodbye)?",("no","Yes"))
if A9 ==["no"]:
  A9 = 0
else:
  A9 = 1
A10 = st.selectbox("Does your child stare at nothing with no apparent purpose?",("no","Yes"))
if A10 ==["no"]:
  A10 = 0
else:
  A10 = 1
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
