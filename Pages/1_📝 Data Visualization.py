import streamlit as st
import pandas as pd
import utils as ul
from urllib.error import URLError
st.subheader("Data Visualization with Table 📝")

# read data from csv  
#file_path = "C:\\Users\\Nwe Ni\\Desktop\\Python\\house.csv"
def draw_table(df):
    df.rename(columns = {'Number' : 'Number of Burned Down Houses' }, inplace = True)

    #description
    st.markdown('''<br>
    The following data illustrates the estimation of burned down houses in each village around Kanbalu and Ye U District.
    <br><br>
    ''', unsafe_allow_html = True)

    condition = st.multiselect("Choose Region:", list(df.Region.unique()))
    select_region = df[df['Region'].isin(condition)]
    if select_region.empty :
        st.write(df)

    else:
        st.write(select_region)
        
try:
    df = ul.read_file()
    draw_table(df)

        
        
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
    draw_table(df)