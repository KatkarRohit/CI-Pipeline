import streamlit as st 

st.title('Power Calculator') 
st.write('enter the number to calculate the square , cube and fith power') 


n = st.number_input("Enter the number: " , value=1 , step=1) 


square = n**2
cube = n**3 
fith_power = n**5 


st.write(f"the square of {n} is {square}")
st.write(f"the cube of {n} is {cube}")
st.write(f"the fifth power of {n} is {fith_power}")