import streamlit as st
import pandas as pd

#title
st.title("This is a title for the streamlit web app.")

#subheader
st.subheader("This is a subheader for the web app")

#header
st.header("This is a header")

#text
st.text("I am a text function")

#markdown
st.markdown("*Hello* this is a **markdown** and below is a test for accessing a website")
st.markdown("[check this out](https://youtu.be/w4BoNlGa7gM?si=wTUui3g5aAqWSJQ-&t=7)")
st.markdown("---")

#caption
st.caption("This is a caption")

#latex for math
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
st.latex(r"\begin{pmatrix}matrices&are\\so&cool\end{pmatrix}")

#json
json={"a":"1,2,3" , "b":"4,5,6"}
st.json(json)

#code block
code="""
print("hello world")
def function():
    return 0;
"""
st.code(code, language="python")

#write
st.write("## H2")

#metric
st.metric(label="Wind Speed", value="120ms\^-1", delta="1.4ms\^-1")

#table and dataframe
table=pd.DataFrame({"Column 1": [1,2,3,4,5,6,7], "Column 2":[11,12,13,14,15,16,17]})
st.table(table)
st.dataframe(table)

#image
st.image("shrek.jpeg", caption="this is a caption", width=200)

#audio
st.audio("audio.mp3")

#video
st.video("man.mp4")

#checkbox
state=st.checkbox("Checkbox", value=False)
if state:
    st.write("Hi")
else:
    pass   

def change():
    print("Changed")
state2=st.checkbox("Checkbox 2", value=False, on_change=change)

def change2():
    print(st.session_state.checker)
state2=st.checkbox("Checkbox 3", value=False, on_change=change2, key="checker")

#radio button
radio_btn=st.radio("In which country do you live?", options=("US", "India", "China"))
print(radio_btn)

#button
def btn_click():
    print("Button Clicked!")
btn=st.button("Click me!!!", on_click=btn_click)

#select box
select=st.selectbox("What is your favourite car?", options=("BMW", "Audi", "Honda"))
print(select)

#multi select box
multi_select=st.multiselect("What is your favourite Tech Brand?", options=("Microsoft", "Apple", "Samsung"))
st.write(multi_select)
print(multi_select)

st.markdown("---")
#upload files
st.title("Uploading Files")
images=st.file_uploader("Please upload an Image", type=['png','jpg'], accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image, width=200)

#slider
val=st.slider("This is a Slider", min_value=-100, max_value=100)
print(val)

#text input
val=st.text_input("Enter your Course Title", max_chars=10)
print(val)

#text area
val=st.text_area("Enter your Description", max_chars=100)
print(val)

#time app with progress bar
import time as ts
from datetime import time

def converter(value):
    m,s,mm=value.split(":")
    t_s=int(m)*60+int(s)+int(mm)/1000
    return t_s

val=st.time_input("Set Timer", value=time(0,0,0))
if str(val) == "00:00:00":
    st.write("Please set a timer")
else:
    sec=converter(str(val))
    print(sec)
    bar=st.progress(0)
    per=sec/100
    progress_status=st.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i+1) + " %")
        ts.sleep(per)

#form
st.markdown("<h1 style='text-align: center;'>User Registration</h1>", unsafe_allow_html=True)
with st.form("Form 1", clear_on_submit=True):
    col1,col2=st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last Name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day, month, year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    s_state=st.form_submit_button("Submit")
    if s_state:
        if f_name == "" and l_name == "":
            st.warning("Please fill above fields")
        else:
            st.success("Submitted Successfully")
            