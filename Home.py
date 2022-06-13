import streamlit as st

#This is the first app created using streamlit
st.set_page_config(
    page_title="Houses info",
    page_icon="🔥",
)

#streamlit run "C:\\Users\\Nwe Ni\\Desktop\\Python\\Home.py"
st.header("Burned Down Houses in Myanmar 🔥")
st.markdown("**(_Sagaing Division_)**")
st.markdown('''
    This app will show the data of houses that are burned down by Military during May and June 2022 in Sagaing Region.<br>
    The data may be a little difference from ground information.<br><br><br>
    Referrence : Kotaungbo Facebook Page and Ye U Facebook Pages
    
''', unsafe_allow_html=True)