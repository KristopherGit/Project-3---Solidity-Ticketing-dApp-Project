import subprocess
import os
import streamlit as st
import sys
from streamlit.components.v1 import html

from streamlit_grid


# def open_tk():
# subprocess.Popen([<interpreter>, <filepath>])
# os.system(<filepath>)
# os.system("seating.py")

@st.cache(allow_output_mutation=True)
def launch_tk():

    try:
        subprocess.run(["python", "seating.py"])
    except Exception as e:
        print(str(e))


st.sidebar.button("Test Button Layout", launch_tk)

button_grid = st.multiselect([
    st.button('Button 1'),
    st.button('Button 2'),
    st.button('Button 3'),
    st.button('Button 4')
])

button_grid()
