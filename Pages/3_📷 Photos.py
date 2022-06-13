import streamlit as st
import utils as ul

st.subheader("Loss of houses after burning down")
'''The residents lost storehouses full of crops and food for animals as well as their homes, built over generations.'''

#https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/6/2017/11/04133712/waterfall.jpg
img1 = "https://drive.google.com/file/d/1OWShSQ20smQ7fooo5No0qZpivbNAaro7/view?usp=sharing"
img2 = "https://drive.google.com/file/d/1Oq1XxfKZ5dCO0vsvD4bHVwV0UkpeuBJG/view?usp=sharing"
img3 = "https://drive.google.com/file/d/1OlysiA11hEV0w7UAaaKCQQECMFYp92if/view?usp=sharing"
img4 = "https://drive.google.com/file/d/1OYQamIQrNGvwfXHb021FHbhgJrIHo5zp/view?usp=sharing"

img_arr = [img1, img2, img3, img4] 

col1, col2, col3 = st.columns(3)

with col1:
    img = ul.get_data_from_google(img_arr[3])
    st.image(img, caption = "Ref : facebook pages")

with col2:
    img = ul.get_data_from_google(img_arr[1])
    st.image(img, caption = "Ref : facebook pages")

with col3:
    img = ul.get_data_from_google(img_arr[2])
    st.image(img, caption = "Ref : facebook pages")
