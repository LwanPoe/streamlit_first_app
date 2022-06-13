import tkinter
import streamlit as st
import pandas as pd
import utils as ul
from urllib.error import URLError


def draw_graph(df):
    st.markdown('''<br>
    The following data illustrates the estimation of burned down houses in each village around Kanbalu and Ye U District.
    <br><br>
    ''', unsafe_allow_html = True)
    condition = st.multiselect("Choose Region:", list(df.Region.unique()), ["Kanbalu"])
    select_region = df[df['Region'].isin(condition)]
    #st.bar_chart(df.Number)
    if select_region.empty :
        st.bar_chart(df.Number)

    else:
        st.bar_chart(select_region.Number)
    
st.subheader("Data Visualization with Chart 📊")
#file_path = "C:\\Users\\Nwe Ni\\Desktop\\Python\\house.csv" 
try:
    df = ul.read_file()
    draw_graph(df)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: ...
        The updated data cannot be shown
    """
        
    )
    df = ul.read_local_data()
    #st.write(df)
    draw_graph(df)

