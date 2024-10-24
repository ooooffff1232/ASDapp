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
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


#creating the web app

#title
st.markdown('<h1 class="centered-title">Divergence AI</h1>', unsafe_allow_html=True)

#dashboard


genderOptionsVal = ["Male","Female"]
ethnicityVl =["Asian","White European","Middle eastern","White","Black","Others","Hispanic","Latino","Pacifica","Mixed","Native Indian","Aboriginal","Turkish"]
jaundiceVal = ["No","Yes"]
family_mem_with_ASD_val = ["No","Yes"]
classval = ["No","Yes"]

S1 = st.selectbox("Q1. How often does your child look at you when you call their name?",("Always","Usually","Sometimes","Rarely", "Never"), index= None)
if S1 =="Always":
   Q1 = 0
   A1 = 1
elif S1 =="Usually":
   Q1 = 0
   A1 = 1
elif S1 =="Sometimes":
   Q1 = 1
   A1 = 1
elif S1 =="Rarely":
   Q1 = 1
   A1 = 0
else :
   Q1 = 1
   A1 = 0
Q2 = st.selectbox("Q2. How easy is it for you to get eye contact with your child?",("Very easy", "Quite easy", "Quite difficult", "Very difficult", "Impossible"), index= None)
if Q2 =="Very easy":
   Q2 = 0
   A2 = 1
elif Q2 =="Quite easy":
   Q2 = 0
   A2 = 1
elif Q2 =="Quite difficult":
   Q2 = 1
   A2 = 0
elif Q2 =="Very difficult":
   Q2 = 1
   A2 = 0
else:
   Q2 = 1
   A2 = 0
Q3 = st.selectbox("Q3. How often does your child point to indicate that they want something? (e.g. a toy that is out of reach)",("Many times a day", "A few times a day",  "A few times a week", "Less than once a week", "Never"), index= None)
if Q3 =="Many times a day":
   Q3 = 0
   A3 = 1
elif Q3 =="A few times a day":
   Q3 = 0
   A3 = 1
elif Q3 =="A few times a week":
   Q3 = 1
   A3 = 1
elif Q3 =="Less than once a week":
   Q3 = 1
   A3 = 0
else:
   Q3 = 1
   A3 = 0
Q4 = st.selectbox("Q4. How often does your child point to share interest with you? (e.g. pointing at an  interesting sight)",("Many times a day", "A few times a day",  "A few times a week", "Less than once a week", "Never"), index= None)
if Q4 =="Many times a day":
   Q4 = 0
   A4 = 1
elif Q4 =="A few times a day":
   Q4 = 0
   A4 = 1
elif Q4 =="A few times a week":
   Q4 = 1
   A4 = 1
elif Q4 =="Less than once a week":
   Q4 = 1
   A4 = 0
else:
   Q4 = 1
   A4 = 0
Q5 = st.selectbox("Q5. How often does your child pretend? (e.g. care for dolls, talk on a fake phone)",("Many times a day", "A few times a day",  "A few times a week", "Less than once a week", "Never"), index= None)
if Q5 =="Many times a day":
   Q5 = 0
   A5 = 1
elif Q5 =="A few times a day":
   Q5 = 0
   A5 = 1
elif Q5 =="A few times a week":
   Q5 = 1
   A5 = 1
elif Q5 =="Less than once a week":
   Q5 = 1
   A5 = 0
else:
   Q5 = 1
   A5 = 0
Q6 = st.selectbox("Q6. How often does your child follow where your looking?",("Many times a day", "A few times a day",  "A few times a week", "Less than once a week", "Never"), index= None)
if Q6 =="Many times a day":
   Q6 = 0
   A6 = 1
elif Q6 =="A few times a day":
   Q6 = 0
   A6 = 1
elif Q6 =="A few times a week":
   Q6 = 1
   A6 = 1
elif Q6 =="Less than once a week":
   Q6 = 1
   A6 = 0
else:
   Q6 = 1
   A6 = 0
Q7 = st.selectbox("Q7. If you or someone else in the family is visibly upset, does your child show signs  of wanting to comfort them?  (e.g. stroking hair, hugging them) ",("Always","Usually","Sometimes","Rarely", "Never"), index= None)
if Q7 =="Always":
   Q7 = 0
   A7 = 1
elif Q7 =="Usually":
   Q7 = 0
   A7 = 1
elif Q7 =="Sometimes":
   Q7 = 1
   A7 = 1
elif Q7 =="Rarely":
   Q7 = 1
   A7 = 0
else:
   Q7 = 1
   A7 = 0
Q8 = st.selectbox("Q8. How would you describe your child's first words?",("Very easy", "Quite easy", "Quite difficult", "Very difficult", "Impossible"), index= None)
if Q8 =="Very easy":
   Q8 = 0
   A8 = 1
elif Q8 =="Quite easy":
   Q8 = 0
   A8 = 1
elif Q8 =="Quite difficult":
   Q8 = 1
   A8 = 0
elif Q8 =="Very difficult":
   Q8 = 1
   A8 = 0
else:
   Q8 = 1
   A8 = 0
Q9 = st.selectbox("Q9. How often does your child use simple gestures? (e.g.  wave  goodbye) ",("Many times a day", "A few times a day",  "A few times a week", "Less than once a week", "Never"), index= None)
if Q9 =="Many times a day":
   Q9 = 0
   A9 = 1
elif Q9 =="A few times a day":
   Q9 = 0
   A9 = 1
elif Q9 =="A few times a week":
   Q9 = 1
   A9 = 1
elif Q9 =="Less than once a week":
   Q9 = 1
   A9 = 0
else:
   Q9 = 1
   A9 = 0
Q10 = st.selectbox("Q10. How often does your child stare at nothing with no apparent purpose?",("Many times a day", "A few times a day",  "A few times a week", "Less than once a week", "Never"), index= None)
if Q10 =="Many times a day":
   Q10 = 1
   A10 = 1
elif Q10 =="A few times a day":
   Q10 = 1
   A10 = 1
elif Q10 =="A few times a week":
   Q10 = 1
   A10 = 1
elif Q10 =="Less than once a week":
   Q10 = 0
   A10 = 0
else:
   Q10 = 0
   A10 = 0
Sex = st.selectbox("Q11. Gender",genderOptionsVal, index= None)
Ethnicity = st.selectbox("Q12. Ethnicity",ethnicityVl, index = None)
Jaundice = st.selectbox("Q13. Does your child have jaundice (yellowish discoloration of the skin)?",jaundiceVal, index = None)
family_mem_with_ASD_val = st.selectbox("Q14. Do you have any family members with ASD?",family_mem_with_ASD_val, index = None)
age_Mons = st.slider("Q15. Age In Months",1,150,20)
Qchat_10_Score = Q1+Q2+Q3+Q4+Q5+Q6+Q7+Q8+Q9+Q10
if Qchat_10_Score < 4:
  classvall = "No"
else:
  classvall = "Yes"
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
               "Class":classvall,
               "A3":A3,
               "A6":A6,
               "A9":A9,
               "Qchat-10-Score":Qchat_10_Score,
               "Jaundice":Jaundice
}

if st.button("Get Predictions"):
    prediction = get_prediction(input_data)
    st.subheader(f"Education Type: {prediction}", divider="blue")
    if prediction =="Antecedent based Intervention":
      st.caption("Antecedent-based intervention focuses on modifying the environment or conditions before a behavior occurs to prevent challenging behaviors. For children with autism, this might involve changing the physical setting, providing clear instructions, or offering choices to reduce triggers and promote positive behavior.")
    if prediction =="Task Analysis":
      st.caption("Task analysis involves breaking down complex tasks into smaller, manageable steps. For children with autism, this method helps in teaching daily living skills, academic tasks, and social behaviors by providing clear, sequential instructions and reinforcing each step as it is mastered.")
    if prediction =="Pivotal Response Training":
      st.caption("Pivotal Response Training (PRT) targets key areas of a child's development, such as motivation and self-management, to produce broad improvements in communication, behavior, and social skills. This method uses natural learning opportunities and child-initiated interactions to reinforce desired behaviors.")
    if prediction =="Picture Exchange Communication":
      st.caption("PECS is a communication system that uses pictures to help children with autism develop functional communication skills. Children are taught to exchange pictures for desired items or activities, gradually progressing to constructing simple sentences and engaging in more complex communication.")
    if prediction =="Technology aided Instruction":
      st.caption("Technology-aided instruction uses devices such as tablets, computers, and specialized software to facilitate learning. For children with autism, this can include interactive apps, video modeling, and virtual reality environments that provide engaging and personalized learning experiences.")
    if prediction =="Peer-mediated Instruction":
      st.caption("Peer-mediated instruction involves teaching typically developing peers strategies to interact and support their classmates with autism. This method enhances socialization and communication skills for children with autism through structured play, group activities, and peer modeling.")
    if preduction =="dfdf":
      st.caption("dfsdf")
  
      
