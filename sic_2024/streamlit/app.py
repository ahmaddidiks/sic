import streamlit as st
import pandas as pd
import numpy as np


st.title('SIC class')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")


df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

number = st.number_input("Insert a number")
st.write("The current number is ", number)

st.image('mentoring.jpg', caption='mentoring offline SIC')






st.balloons()