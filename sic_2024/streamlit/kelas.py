import streamlit as st
import pandas as pd
import numpy as np

st.write('Hello, *World!* :sunglasses:')
st.write('Hello2, *World!* :sunglasses:')

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.line_chart(df)

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

number = st.number_input("Insert a number")
st.write("The current number is ", number)

st.image('https://static.streamlit.io/examples/cat.jpg', caption='Mentoring hari minggu')

# video_file = open('test_video_short.mp4', 'rb')
# video_bytes = video_file.read()

# st.video(video_bytes)

with st.container():
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 10))

st.write("This is outside the container")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("mentoring.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

