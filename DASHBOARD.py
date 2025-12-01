import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Streamlit Dashboard")
st.text("This is a simple Streamlit dashboard")
st.header("Streamlit Dashboard")
st.subheader("Streamlit Dashboard")
st.write("yo can write anything", 10+5)

name = st.text_input("Enter your name")
age = st.number_input("Enter your age")
st.write("Hello", name, "you are", age, "years old")
st.selectbox("Select your favorite color", ["Red", "Green", "Blue"])
st.checkbox("Do you like cats?")
st.radio("Select your favorite animal", ["Cat", "Dog", "Mouse"])
if st.button("Submit"):
    st.success("Submitted")
file = st.file_uploader("Upload a file")
if file :
    contents = file.read()
    st.write("file uploaded")
    

data = {"name":["Divyansh","harry","rohit"], "age":[20,21,22], "city":["Delhi","Mumbai","Bangalore"]}
df = pd.DataFrame(data)

st.dataframe(df)

data = pd.DataFrame({
    "name":["Divyansh","harry","rohit"],
    "age":[20,21,22],
    "city":["Delhi","Mumbai","Bangalore"]
})
st.line_chart(data, x="name", y="age")
st.bar_chart(data, x="name", y="city")

st.subheader("Age Distribution Pie Chart")
fig = px.pie(data, values='age', names='name', title='Age Distribution by Person')
st.plotly_chart(fig, use_container_width=True)


