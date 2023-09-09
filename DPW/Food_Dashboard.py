import streamlit as st
from PIL import Image, ImageDraw, ImageOps
import streamlit as st
import numpy as np
import pandas as pd
import Breakfast
import Dinner
import Lunch
import Snacks 
import Special
import testing
# Set page config
st.set_page_config(layout="wide")

# Create a function to display the homepage
def testing():
    import streamlit as st
    testing.test() 
def BREAKFAST():    
    import streamlit as st    
    tab1, tab2 = st.tabs(["VEG", "NON-VEG"]) 
    with tab1:    
        st.write( f'<h1 style="color:#009999;">BREAKFAST VEG RECEPIES</h1>', unsafe_allow_html=True )
        Breakfast.breakfast_veg()
              
    with tab2:
        st.write( f'<h1 style="color:#009999;">BREAKFAST NON-VEG RECEPIES</h1>', unsafe_allow_html=True )
        Breakfast.breakfast_nonveg()
    
def LUNCH():
    import streamlit as st    
    tab1, tab2 = st.tabs(["VEG", "NON-VEG"]) 
    with tab1:    
        st.write( f'<h1 style="color:#009999;">LUNCH VEG RECEPIES</h1>', unsafe_allow_html=True )
        Lunch.lunch_veg()
              
    with tab2:
        st.write( f'<h1 style="color:#009999;">LUNCH NON-VEG RECEPIES</h1>', unsafe_allow_html=True )
        Lunch.lunch_nonveg()
            
def SNACKS():   
    import streamlit as st    
    tab1, tab2 = st.tabs(["VEG", "NON-VEG"]) 
    with tab1:    
        st.write( f'<h1 style="color:#009999;">SNACKS VEG RECEPIES</h1>', unsafe_allow_html=True )
        Snacks.snacks_veg()
              
    with tab2:
        st.write( f'<h1 style="color:#009999;">SNACKS NON-VEG RECEPIES</h1>', unsafe_allow_html=True )
        Snacks.snacks_nonveg()

    
def DINNER():
    import streamlit as st    
    tab1, tab2 = st.tabs(["VEG", "NON-VEG"]) 
    with tab1:    
        st.write( f'<h1 style="color:#009999;">DINNER VEG RECEPIES</h1>', unsafe_allow_html=True )
        Dinner.dinner_veg()
              
    with tab2:
        st.write( f'<h1 style="color:#009999;">DINNER NON-VEG RECEPIES</h1>', unsafe_allow_html=True )
        Dinner.dinner_nonveg()
       
                        
def SPECIAL():
    import streamlit as st    
    tab1, tab2 = st.tabs(["SOUPS", "JUICES"]) 
    with tab1:    
        st.write( f'<h1 style="color:#009999;">SPECIAL VEG RECEPIES</h1>', unsafe_allow_html=True )
        Special.special_soups()
              
    with tab2:
        st.write( f'<h1 style="color:#009999;">SPECIAL NON-VEG RECEPIES</h1>', unsafe_allow_html=True )
        Special.special_juices


   
        
# Define the pages dictionary
pages = {
    "BREAKFAST": BREAKFAST,    
    "LUNCH": LUNCH,
    "SNACKS": SNACKS,
    "DINNER": DINNER,
    "SPECIAL": SPECIAL,
    "testing":testing,

}

# Add a navigation menu to the sidebar
selection = st.sidebar.radio('', list(pages.keys()))
# Call the appropriate page based on the user's menu choice
pages[selection]()
with st.container():
    st.write("")
    st.write("")
    st.write("")
    st.write( f'<p style="color:#334d4d;">Created by Tulasi NND</p>', unsafe_allow_html=True )
    
 
