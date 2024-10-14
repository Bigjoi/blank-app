import streamlit as st
import pandas as pd
from datetime import datetime

# ข้อมูลเครื่องมือ
tools_data = {
    "ชื่อเครื่องมือ": ["เครื่องมือ A", "เครื่องมือ B", "เครื่องมือ C"],
    "รูปภาพ": ["path/to/image_a.jpg", "path/to/image_b.jpg", "path/to/image_c.jpg"],
    "สถานะ": ["ว่าง", "ว่าง", "ว่าง"],
    "วันที่เริ่ม": [None, None, None],
    "วันที่สิ้นสุด": [None, None, None],
    "ชื่อผู้ใช้งาน": [None, None, None]
}

tools_df = pd.DataFrame(tools_data)

# ฟังก์ชันแสดงสถานะเครื่องมือ
def display_tools_status(tools_df):
    for index, row in tools_df.iterrows():
        st.image(row["รูปภาพ"], caption=row["ชื่อเครื่องมือ"])
        if row["สถานะ"] == "ถูกใช้งาน":
            st.write(f"สถานะ: {row['สถานะ']} (ผู้ใช้: {row['ชื่อผู้ใช้งาน']})")
            st.write(f"วันที่ใช้งาน: {row['วันที่เริ่ม']} - วันที่สิ้นสุด: {row['วันที่สิ้นสุด']}")
        else:
            st.write(f"สถานะ: {row['สถานะ']}")

# ฟังก์ชันสำหรับการยืมเครื่องมือ
def borrow_tool(tools_df):
    user_name = st.text_input("ชื่อผู้ใช้งาน")
    tool_name = st.selectbox("เลือกเครื่องมือ", tools_df["ชื่อเครื่องมือ"])
    start_date = st.date_input("วันที่เริ่มใช้งาน", datetime.today())
    end_date = st.date_input("วันที่สิ้นสุดใช้งาน", datetime.today())

    if st.button("ยืมเครื่องมือ"):
        # อัปเดตสถานะของเครื่องมือ
        tool_index = tools_df[tools_df["ชื่อเครื่องมือ"] == tool_name].index[0]
        tools_df.at[tool_index, "สถานะ"] = "ถูกใช้งาน"
        tools_df.at[tool_index, "วันที่เริ่ม"] = start_date
        tools_df.at[tool_index, "วันที่สิ้นสุด"] = end_date
        tools_df.at[tool_index, "ชื่อผู้ใช้งาน"] = user_name
        st.success(f"คุณได้ยืม {tool_name} เรียบร้อยแล้ว!")

# ส่วนหลักของโปรแกรม
st.title("โปรแกรมจัดการสถานะเครื่องมือ")
st.header("สถานะเครื่องมือ")

# แสดงสถานะเครื่องมือ
display_tools_status(tools_df)

# แสดงฟอร์มยืมเครื่องมือ
st.header("ยืมเครื่องมือ")
borrow_tool(tools_df)

# แสดงสถานะอัปเดต (อาจจะต้องใช้ session state หรือ database สำหรับการเก็บข้อมูลจริง)
st.session_state.tools_df = tools_df
