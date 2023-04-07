import streamlit as st
st.title("Maximum Of Three \n by *21f2000226(Vasista)* *TDS Assignment 8*")
with st.sidebar:
    x = st.number_input("First Number",step=1,format="%i")
    y = st.number_input("Second Number",step=1,format="%i")
    z = st.number_input("Third Number",step=1,format="%i")
maxi = max(x,y,z)
st.write(f"The maximum of the given numbers is {maxi}")
