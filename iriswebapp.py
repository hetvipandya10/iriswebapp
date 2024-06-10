import streamlit as st

st.title("Welcome to Iris App")

sl=st.slider("Select Sepal Length=",4.3,7.9)
sw=st.slider("Select Sepal Width=",2.0,4.4)
pl=st.slider("Select Petal Length=",1.0,6.9)
pw=st.slider("Select Petal Width=",0.1,2.5)

import pickle
model=pickle.load(open("irisml.pkl","rb"))
if st.button("Predict"):
    prd=model.predict([[sl,sw,pl,pw]])
    st.success("The Flower is "+ prd[0])


