import streamlit as st
import pandas as pd
from keras.models import load_model
import pickle



st.title("Passenger Survival Chance in the Titanic journey")

pclass=st.slider("Enter the Passeners class for the user",1,3)

sex=st.selectbox("Enter the Passenger Gender",["male","female"])
sibsp=st.slider("Enter the Passener total number of Sibling and Spous",1,8)
parch=st.slider("Enter the Passengers total number of Parents and Child",0,6)
fare=st.number_input("Enter the Fare of The passenger")
embarked=st.selectbox("Enter the passengger station from where they started the journey",["Southampton","Chabourg","Queenstwon"])

data=pd.DataFrame([{"Pclass":pclass,"Sex":sex,"SibSp":sibsp,"Parch":parch,"Fare":fare,"Embarked":embarked}])

model=load_model("model.h5")

with open('label_encoder.pkl',"rb") as file:
    label=pickle.load(file)
    
with open('onehot_encoder.pkl',"rb") as file:
    onehot=pickle.load(file)
    
with open('scaler.pkl',"rb") as file:
    scaler=pickle.load(file)
    
data["Sex"]=label.transform(data["Sex"])
embarked=onehot.transform(data[["Embarked"]])

embarked=pd.DataFrame(embarked,columns=onehot.get_feature_names_out())

data=pd.concat([data.drop(columns=["Embarked"]),embarked],axis=1)

data[["Pclass","Sex","SibSp","Parch","Fare"]]=scaler.transform(data[["Pclass","Sex","SibSp","Parch","Fare"]])

y=model.predict(data)
y=y[0][0]

def chance(y):
    if y>0.5:
        return "The passenger will survive the Journey"
    else:
        return "The Passener will won't survive the Journey"

if st.button("predict Survival Chance"):
    st.write("probability of Passenggers Survival Chance",y)
    st.write(f"Survival Chance:{y*100:.2f}%")