import streamlit as st
from predict import pred

st.title("TEST")
st.write("Enter the measurements:")

sL=st.number_input("Sepal length",min_value=0.0,max_value=10.0,value=5.1)
sW=st.number_input("Sepal width",min_value=0.0,max_value=10.0,value=3.5)
pL=st.number_input("Petal length",min_value=0.0,max_value=10.0,value=1.4)
pW=st.number_input("Petal width",min_value=0.0,max_value=10.0,value=0.2)

if st.button("---PREDICT---"):
    feats = [sL,sW,pL,pW]
    species=pred(feats)
    st.success(f"The predicted Iris species is **{species.capitalize()}**")
