import streamlit as st
from datetime import datetime
from PIL import Image

# สร้างฟังก์ชันเพื่อแสดงสถานะเครื่องมือ
def display_tool_status(image_path, date, user):
    st.image(image_path, caption="Tool Image", use_column_width=True)
    st.write(f"**Date Used:** {date}")
    st.write(f"**User:** {user}")

# ชื่อแอป
st.title("Tool Status App")

# ตัวแปรสำหรับเก็บข้อมูลสถานะ
if 'tool_status' not in st.session_state:
    st.session_state.tool_status = {
        'image_path': None,
        'date': datetime.now().strftime("%Y-%m-%d"),
        'user': ''
    }

# ฟอร์มสำหรับกรอกข้อมูล
with st.form(key='tool_status_form'):
    image_file = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])
    if image_file is not None:
        st.session_state.tool_status['image_path'] = image_file
        st.session_state.tool_status['image'] = Image.open(image_file)

    date = st.text_input("Date Used", st.session_state.tool_status['date'])
    user = st.text_input("User", st.session_state.tool_status['user'])
    
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.session_state.tool_status['date'] = date
        st.session_state.tool_status['user'] = user

# แสดงสถานะเครื่องมือเมื่อเปิดโปรแกรม
if st.session_state.tool_status['image_path']:
    display_tool_status(st.session_state.tool_status['image'], st.session_state.tool_status['date'], st.session_state.tool_status['user'])
