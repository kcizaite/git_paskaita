# Streamlit
# pip install streamlit
import numpy as np
import streamlit as st
import pandas as pd


st.title("Hello **World**")
st.write("This is a simple Streamlit app. **World**")
st.write("# You can add more widgets and functionality here.")
st.write("## You can add more widgets and functionality here.")
st.write("### You can add more widgets and functionality here.")


# TODO
x, y, z = st.columns(3)

i = x.text_input("Enter some text:")
j = y.number_input("Enter a number:")
k = z.text_input("Enter some text: ")
# h = y.number_input("Enter a number: ")

x, y, z = st.columns(3)

x.write(f"You entered: {i}")
y.write(f"You entered: {j}")
z.write(f"You entered: {k}")


d = pd.read_csv("movies.csv")
st.write(d)

dt = pd.DataFrame(np.random.randn(30, 4), columns=["v1", "v2", "v3", "v4"])
st.bar_chart(dt)
st.line_chart(dt)