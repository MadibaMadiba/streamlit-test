import time
import streamlit as st
import pandas as pd
import numpy as np
from urllib3.filepost import writer

st.balloons()
@st.dialog("muh") # creates a dialoge box
def box():
    st.title("bwaaaag")
    st.write("Yello agane")

# box() # function must be called for it to trigger

# streamlit is basically markdown but for python
st.header("Yello")
st.write("Test djschksd")
st.caption("text")

st.code("""
print("Hello World")
""") # This is basically just a code block

with st.echo(): # essentially the same as st.code but runs the code as a function
    st.write("Hello World")

st.divider()
df = pd.read_csv("data/data.csv")
# st.dataframe(df) # displays the dataframe on the page

# edited_df = st.data_editor(df)

st.metric("Temp", 16, -3)
st.metric("humidity %", 77, 8)

if st.button("Run"):
    st.write("Hello World")

ufeeb = st.feedback()

if ufeeb == 1:
    st.write("awsum :  )")
elif ufeeb == 0:
    st.write("okay :(((")

stars = st.feedback("stars")

st.checkbox("Sequence 5")
st.toggle("sequence 6")

st.radio("Sequences", ["None", 1, 2, 3, 4, 5, 6])

st.selectbox("Select Option", ["None", 1, 2, 3, 4, 5, 6])

st.multiselect("Select Option", ["None", 1, 2, 3, 4, 5, 6])

st.select_slider("Select Option", [0, 1, 2, 3, 4, 5, 6], 0)

age = st.number_input("Age", 1, 100)

date = st.date_input("Date")

time_appointment = st.time_input("Time")

st.text_input("Guh? :")

st.text_area("Bluh", height=100)

echo_json = st.file_uploader("Upload File")

st.camera_input("nyehehe") # does the thing you think it does

# st.image("image.png") # displays an image

col1, col2, col4 = st.columns(3)

with st.expander("Explanation"):
    st.write("information")
    st.write("right here can you believe it! :)")

with st.popover("Tiny"):
    st.write(":3c")

with st.sidebar:
    st.write("glug glug")

with st.spinner("Spin Spinner"):
    time.sleep(4)
    st.write("Spin Spinner")

def prog_bar():
    for i in range(100):
        time.sleep(0.1)
        return i

st.progress(prog_bar())

st.toast("wake uuuuup :wilted_flower:", icon="👹")

st.balloons()
st.info("aboba")

progress_bar = st.progress(0, text="In progress")

for progress_percent in range(100):
    time.sleep(0.1)
    progress_bar.progress(progress_percent)

time.sleep(1)
progress_bar.empty()
st.success("Done")
st.warning("erm")
st.error("ERM")