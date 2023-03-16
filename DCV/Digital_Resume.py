import streamlit as st
from PIL import Image, ImageDraw, ImageOps
import streamlit as st
import numpy as np
import pandas as pd
# Set page config
st.set_page_config(layout="wide")

# Create a function to display the homepage
def About():    
    import streamlit as st
    # CAREER OBJECTIVE
    st.write( f'<h1 style="color:#e600ac;">CAREER OBJECTIVE</h1>', unsafe_allow_html=True )   
    #my_col='#660066'
    my_col='rgb(230, 0, 172,0.1)'
    # Define function to create block with colored content
    def create_block(content, color):
        st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:4px; margin-bottom:10px;"><p style="color:#e600ac; font-size: 20px;">{content}</p></div>', unsafe_allow_html=True)

    intro = [
        {'data1': '''
        \tHello! I'm Tulasi, an Information Technology student with a passion for data science. I love working with 
    data, analyzing it, and using it to gain insights. For me, data is not just numbers and figures, but a language 
    that speaks volumes when analyzed with the right tools and techniques. ''',
        'data2':'''
    \tI believe that data has the power to transform businesses and societies, and I am excited to be a part of this
    revolution by utilizing my skills and knowledge as a data scientist.
    '''},
    ]

    for i, intr in enumerate(intro):
        create_block(f"{intr['data1']}<br><br>{intr['data2']}",my_col )

    # CONTACT INFORMATION
    st.write( f'<h1 style="color:#e600ac;">CONTACT INFORMATION</h1>', unsafe_allow_html=True )

    contact=[{
                        
                     
            'Email Address':          'tulasinnd@gmail.com ' ,        
                 
            'LinkedIn Profile':      ' https://www.linkedin.com/in/tulasi-n-49b6111b0/',

            'GitHub Profile':         'https://github.com/tulasinnd'
            
             
           }]
    for i, c in enumerate(contact):
        create_block(f"EMAIL: {c['Email Address']}<br>LINKEDIN: {c['LinkedIn Profile']}<br>GITHUB: {c['GitHub Profile']}",my_col )

    
def Education():
    import streamlit as st
    # EDUCATION DETAILS
    st.write( f'<h1 style="color:#009999;">EDUCATION DETAILS</h1>', unsafe_allow_html=True )

    # Define function to create block with colored heading
    def create_block(heading, content, color):
        st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px; margin-bottom:10px;"><h4 style="color:#009999">{heading}</h4><p style="color:#009999; font-size: 20px">{content}</p></div>', unsafe_allow_html=True)

    # Define educational qualifications
    qualifications = [
        {'period': '2022-2023', 'course': "1 Professional Master data science program", 'institute': 'IITM with GUVI', 'percentage': 80},
        {'period': '2014-2018', 'course': '2 B.Tech (Information Technology)', 'institute': 'Aditya Engineering College', 'percentage': 78},
        {'period': '2012-2014', 'course': '3 Intermediate', 'institute': 'Aditya Junior College', 'percentage': 92},
        {'period': '2011-2012', 'course': '4 SSC', 'institute': 'Mary Immaculate High School', 'percentage': 93}
    ]

    # Print each qualification as a block with different color
    colors = 'rgb(51, 204, 255,0.2)'
    col1, col2 = st.columns(2)
    for i, qualification in enumerate(qualifications):
        if i % 2 == 0:
            with col1:
                create_block(f"{qualification['course']}", f"Period: {qualification['period']}<br>Institute: {qualification['institute']}<br>Percentage: {qualification['percentage']}", colors)
        else:
            with col2:
                create_block(f"{qualification['course']}", f"Period: {qualification['period']}<br>Institute: {qualification['institute']}<br>Percentage: {qualification['percentage']}", colors)
        
def Skills():    
    import streamlit as st
    st.write( f'<h1 style="color:rgb(255, 0, 170,0.7);">TECHNICAL SKILLS</h1>', unsafe_allow_html=True )
    # Define function to create block with colored heading
    def create_block(heading, content, color,col):
        st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px; margin-bottom:10px;"><h4 style="color:{col}">{heading}</h4><p style="color:{col}; font-size: 20px">{content}</p></div>', unsafe_allow_html=True)

    # Define educational qualifications
    skills = [
        {'skill': '1 PYTHON',
         'd1':'DATA STRUCTURES: &nbsp;&nbsp;&nbsp;Lists, Dictionaries, Sets, and Tuples',
         'd2':'LIBRARIES: &nbsp;&nbsp;&nbsp;NumPy, Pandas and Scikit-Learn ',
         'd3':'File Handling, Regular Expression',
         'd4':'Object Oriented Programming, JSON',
         'd5':'hello'},

        {'skill': '2 DESCRIPTIVE STATISTICS',
         'd1':'DISTRIBUTIONS:&nbsp;&nbsp;&nbsp;Normal, Exponential, Power-Law etc',
         'd2':'HYPOTHESIS TESTING:&nbsp;&nbsp;&nbsp;Normality tests, Correlation Tests',
         'd3':'STATISTICAL MEASURES:&nbsp;&nbsp;&nbsp;Central Tendency, Dispersion',
         'd4':'PDF, CDF, Central limit Theorem, Population, Sample',
         'd5':'hello'},

        {'skill': '3 DATA VISUALIZATION',
         'd1':'MATPLOTLIB: Line, Bar, Box, Pie, Scatter Plots etc',
         'd2':'SEABORN: Regression, Distribution and Categorical plots,',
         'd3':'PLOTLY:3D Plots, Geo-Maps and Animations',
         'd4':'AutoViz, SweetViz, D-Tale',
         'd5':'hello'},

         {'skill': '4 EDA & FE',
         'd1':'Data Cleaning, Descriptive Statistics',
         'd2':'Data Visualization, Correlation Analysis',
         'd3':'Outlier Detection, Dimensionality Reduction',
         'd4':'Data Imputation, Hypothesis Testing',
         'd5':'hello'},

        {'skill': '5 MACHINE LEARNING',
         'd1':'Supervised Learning: Linear, Logistic, Decision Tree, Random Forest',
         'd2':'SVM, Ada-Boost, Gradient Boost, XG-Boost',
         'd3':'Unsupervised Learning: K-Means, PCA',         
         'd4':'Regularization, Cross-Validation, Bias-Variance',
         'd5':'hello'},

        {'skill': '6 DEEP LEARNING',
         'd1':'Activation Functions: ReLU ( and variants), sigmoid, tanh',
         'd2':'Optimizers: Stochastic Gradient Descent, Adam, Adagrad',
         'd3':'Convolutional Neural Networks (CNN), Recurrent Neural Networks (RNN)',
         'd4':'LSTM, GAN, Autoencoders',
         'd5':'hello'},

        {'skill': '7 DATABASES',
         'd1':'MySQL: CRUD, Constraints, Joins, Normalization',
         'd2':'DDL, DML, DQL, Pymysql, mysql-connector-python',
         'd3':'MongoDB: CRUD (CREATE, READ, UPDATE, DELETE) ',
         'd4':'Aggregation Pipeline, Pymongo',
         'd5':'hello'},
        
        {'skill': '8 GUI & DEPLOYMENT',
         'd1':'Plotly',
         'd2':'Streamlit',
         'd3':'Streamlit Cloud, GitHub',
         'd4':'AWS-RDS',
         'd5':'hello'},
    ]

    # Print each qualification as a block with different color
    #colors = ['rgb(255, 102, 102, 0.2)', 'rgb(102, 255, 178, 0.2)', 'rgb(255, 178, 102, 0.2)', 'rgb(102, 204, 255, 0.2)']
    colors = ['rgb(255, 102, 255,0.2)', 'rgba(54, 162, 235, 0.4)', 'rgba(255, 206, 86, 0.4)', 'rgba(75, 192, 192, 0.4)', 'rgba(153, 102, 255, 0.4)', 'rgb(0, 102, 255,0.3)', 'rgba(37, 121, 140, 0.4)', 'rgba(238, 130, 238, 0.4)']
    colors1 = ['#ff66ff', '#36A2EB', '#ffcc00', '#4BC0C0', '#bf80ff', '#4d94ff', '#00b300', '#ff99ff']

    col1, col2 = st.columns(2)
    for i, skill in enumerate(skills):
        if i % 2 == 0:
            with col1:
                create_block(f"{skill['skill']}", f"{skill['d1']}<br>{skill['d2']}<br>{skill['d3']}<br>{skill['d4']}", colors[i % len(colors)], colors1[i % len(colors)])
        else:
            with col2:
                create_block(f"{skill['skill']}", f"{skill['d1']}<br>{skill['d2']}<br>{skill['d3']}<br>{skill['d4']}", colors[i % len(colors)],  colors1[i % len(colors)])    
         
def Projects():

    import streamlit as st    
    tab1, tab2, tab3,tab4 = st.tabs(["PROJECT 1", "PROJECT 2", "PROJECT 3","PROJECT 4"]) #,"PROJECT 5","PROJECT 6"])

    with tab1:
        import streamlit as st

        st.write( f'<h1 style="color:#a31aff;">POPULATION PREDICTION</h1>', unsafe_allow_html=True )
        # Define function to create block with colored heading
        def create_block(content, color):
            st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px; margin-bottom:10px;"><p style="color:#a31aff; font-size: 20px">{content}</p></div>', unsafe_allow_html=True)
        st.write("""
            <style>
                .no-underline {
                    text-decoration: none;                   
                    color: #a31aff ;
                }
            </style>
        """, unsafe_allow_html=True)
        # Define PROJECTS 
        projects = [
            {'a':'''<b>INTRODUCTION:</b><br>
            Welcome to the Population Prediction System! This system is designed to predict the population of any country 
            in the world for a given year. With just the input of the country name and year, this system uses a 
            polynomial regression algorithm to make an accurate prediction.Our system is built on a vast amount of 
            historical data on population trends, which allows us to train our algorithm to recognize patterns and 
            make predictions based on those patterns. The polynomial regression algorithm is especially useful for 
            this task because it can capture complex non-linear relationships between population and time.'''},
            {'a':'''<b>SKILLS:</b><br>
            PYTHON, PANDAS, MACHINE LEARNING<br>
            STREAMLIT, SEABORN <br>
            '''},  
            {'a': '''<a href="https://tulasinnd-population-prediction-system-population-app-x6rrby.streamlit.app/" class="no-underline" style="color: #a31aff;">CLICK HERE TO VIEW APP NOW</a><br><br>
                     <a href="https://github.com/tulasinnd/Population-Prediction-System.git" class="no-underline" style="color: #a31aff;">CLICK HERE TO VIEW CODE NOW</a>'''}        
                ]

        # Print each projects as a block with different color
        colors = 'rgb(153, 51, 255,0.2)'

        create_block(f"{projects[0]['a']}", colors)

        col1, col2,  = st.columns([6,4])

        with col1:
            create_block(f"{projects[1]['a']}", colors)
            
        with col2:
            create_block(f"{projects[2]['a']}", colors)
                      
    with tab2:
        st.write( f'<h1 style="color:#009999;">BUSINESS CARD DATA EXTRACTION</h1>', unsafe_allow_html=True )
        # Define function to create block with colored heading
        def create_block(content, color):
            st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px; margin-bottom:10px;"><p style="color:#009999; font-size: 20px">{content}</p></div>', unsafe_allow_html=True)
        st.write("""
            <style>
                .no-underline {
                    text-decoration: none;                   
                    color: #006666 ;
                }
            </style>
        """, unsafe_allow_html=True)
        # Define PROJECTS 
        projects = [
            {'a':'''<b>INTRODUCTION:</b><br>
            This is a powerful tool that utilizes the EasyOCR library to extract text from images uploaded by users.
            Once the text has been extracted, our app goes a step further and processes the text to extract valuable 
            information using regular expressions such as email addresses, phone numbers, pin codes, addresses, and 
            website URLs. This information is then presented on a sleek and intuitive Streamlit web app interface, 
            making it easy for users to quickly and efficiently retrieve the information they need. Our app is perfect 
            for businesses or individuals looking to streamline their data entry process and save time.'''},
            {'a':'''<b>SKILLS:</b><br>
            PYTHON, PANDAS, IMAGE PROCESSING, OCR<br>
            STREAMLIT, REGULAR EXPRESSIONS <br>
            '''},  
            {'a': '''<a href="https://tulasinnd-text-extraction-from-business-card-usi-ocr-app-c78inw.streamlit.app/" class="no-underline"  style="color: #009999;">CLICK HERE TO VIEW APP NOW</a><br><br>
                     <a href="https://github.com/tulasinnd/Text-Extraction-From-Business-Card-Using-OCR.git" class="no-underline" style="color: #009999;" >CLICK HERE TO VIEW CODE NOW</a>'''}        
                ]

        # Print each projects as a block with different color
        colors = 'rgb(0, 128, 128,0.2)'

        create_block(f"{projects[0]['a']}", colors)

        col1, col2,  = st.columns([6,4])

        with col1:
            create_block(f"{projects[1]['a']}", colors)
            
        with col2:
            create_block(f"{projects[2]['a']}", colors)

        

    with tab3:
        st.write( f'<h1 style="color:#b300b3;">PHONEPE DATA ANALYSIS & VISUALIZATION</h1>', unsafe_allow_html=True )
        # Define function to create block with colored heading
        def create_block(content, color):
            st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px; margin-bottom:10px;"><p style="color:#b300b3; font-size: 20px">{content}</p></div>', unsafe_allow_html=True)
        st.write("""
            <style>
                .no-underline {
                    text-decoration: none;                   
                    color: #e600e6 ;
                }
            </style>
        """, unsafe_allow_html=True)
        # Define PROJECTS 
        projects = [
            {'a':'''<b>INTRODUCTION:</b><br>
            PhonePe Data Analysis and Visualization is a project that involves the analysis of data related to PhonePe 
            transactions and user data from the years 2018 to 2022. The project is based on the Phonepe pulse Github 
            repository data and the analysis is visualized using Streamlit and Plotly in Python. The main components 
            of the project include Geo-visualization, Transactions Analysis, User Data Analysis, and Top States Data. 
            The web application developed as a part of this project allows users to explore and analyze the PhonePe 
            data in an interactive and user-friendly manner.'''},
            {'a':'''<b>SKILLS:</b><br>
            PYTHON, PANDAS, AWS-RDS, Data analysis, Data visualization<br>
            STREAMLIT, SEABORN , PLOTLY, MATPLOTLIB<br>
            '''},  
            {'a': '''<a href="https://tulasinnd-phonepe-pulse-data-2018-2022-phonepe-dashboard-2drsrt.streamlit.app/" class="no-underline" style="color: #b300b3;">CLICK HERE TO VIEW APP NOW</a><br><br>
                     <a href="https://github.com/tulasinnd/PhonePe-Pulse-Data-2018-2022-Analysis.git" class="no-underline" style="color: #b300b3;">CLICK HERE TO VIEW CODE NOW</a>'''}        
                ]

        # Print each projects as a block with different color
        colors = 'rgb(255, 0, 255, 0.15)'

        create_block(f"{projects[0]['a']}", colors)

        col1, col2,  = st.columns([6,4])

        with col1:
            create_block(f"{projects[1]['a']}", colors)
            
        with col2:
            create_block(f"{projects[2]['a']}", colors)
        

    with tab4:
        st.write( f'<h1 style="color:#0099e6;">TWITTER SCRAPING</h1>', unsafe_allow_html=True )
        # Define function to create block with colored heading
        def create_block(content, color):
            st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px; margin-bottom:10px;"><p style="color:#0099e6; font-size: 20px">{content}</p></div>', unsafe_allow_html=True)
        st.write("""
            <style>
                .no-underline {
                    text-decoration: none;                   
                    color: #a31aff ;
                }
            </style>
        """, unsafe_allow_html=True)
        # Define PROJECTS 
        projects = [
            {'a':'''<b>INTRODUCTION:</b><br>
             In this project, I have developed an interactive Graphical User Interface (GUI) using Streamlit that enables 
             users to scrape tweets from official twitter website based on a given keyword or hashtag. The user can also select the starting and ending 
             date for the search and specify the number of tweets to be scraped. After the scraping is completed, the user 
             can choose to download the data in CSV or JSON format, or display all the scraped tweets.'''},
            {'a':'''<b>SKILLS:</b><br>
            PYTHON, PANDAS<br>
            STREAMLIT, SNSCRAPE  <br>
            '''},  
            {'a': '''<a href="https://tulasinnd-twitter-scraping-with-snscrape-twitter-scraper-sm39k5.streamlit.app/" class="no-underline" style="color:#0099e6;">CLICK HERE TO VIEW APP NOW</a><br><br>
                     <a href="https://github.com/tulasinnd/Twitter-scraping-with-snscrape-and-streamlit.git" class="no-underline" style="color:#0099e6;">CLICK HERE TO VIEW CODE NOW</a>'''}        
                ]

        # Print each projects as a block with different color
        colors = 'rgb(102, 204, 255,0.2)'

        create_block(f"{projects[0]['a']}", colors)

        col1, col2,  = st.columns([6,4])

        with col1:
            create_block(f"{projects[1]['a']}", colors)
            
        with col2:
            create_block(f"{projects[2]['a']}", colors)
        

    # with tab5:
    #     st.header("PROJECT 5")
        

    # with tab6:
    #     st.header("PROJECT 6")
                     
    
def Certifications():
    st.write( f'<h1 style="color:#2eb82e;">CERTIFICATIONS & ACHIEVEMENTS</h1>', unsafe_allow_html=True )   
    expander_style = """
        <style>
            .streamlit-expanderHeader {
                background-color: rgb(51, 204, 51, 0.2) !important;
                color: black !important;
                font-weight: bold !important;
            }
        </style>
    """
    st.write("""
            <style>
                .no-underline {
                    text-decoration: none;                   
                    color: #a31aff ;
                }
            </style>
        """, unsafe_allow_html=True)

    # Render the custom CSS style
    st.markdown(expander_style, unsafe_allow_html=True)
    with st.expander("AI FOR WOMEN "):           
        cont='<a href="https://drive.google.com/file/d/1O5xSAbzK6vfjfmRCp8dZpKzG7uljpqUz/view?usp=sharing" class="no-underline" style="color: #145214;"><br>CLICK HERE TO VIEW CERTIFICATION ON AI FOR WOMEN</a>'      
        st.markdown(cont, unsafe_allow_html=True)

    with st.expander("PROGRAMMING WITH PYTHON "):       
        cont='<a href="https://drive.google.com/file/d/1iw8_fa6dUqPEYPac0KnHBd6I6v7mBiR7/view?usp=sharing" class="no-underline" style="color: #145214;"><br>CLICK HERE TO VIEW PYTHON CERTIFICATION</a>'      
        st.markdown(cont, unsafe_allow_html=True)    
    with st.expander("CLEARED GATE EXAM "):       
        cont='<a href="https://drive.google.com/file/d/1O5xSAbzK6vfjfmRCp8dZpKzG7uljpqUz/view?usp=sharing" class="no-underline" style="color: #145214;"><br>CLICK HERE TO VIEW GATE SCORE CARD</a>'      
        st.markdown(cont, unsafe_allow_html=True)            
    
    with st.expander("MASTER DATA SCIENCE PROGRAM "):        
        cont='<a href="https://drive.google.com/file/d/1O5xSAbzK6vfjfmRCp8dZpKzG7uljpqUz/view?usp=sharing" class="no-underline" style="color: #145214;"><br>CLICK HERE TO VIEW DATA SCIENCE CERTIFICATE</a>'      
        st.markdown(cont, unsafe_allow_html=True)            

        
# Define the pages dictionary
pages = {
    "ABOUT": About,    
    "EDUCATION": Education,
    "SKILLS": Skills,
    "PROJECTS": Projects,
    "CERTIFICATIONS": Certifications,

}

#********************************** ROUND IMAGE***************************************************************************************
img_url =r"DCV/mydp.jpg"
st.sidebar.image(img_url, caption='Tulasi NND (tulasinnd@gmail.com)', use_column_width=True, output_format='JPEG')
# Apply CSS styling to create circular border
st.markdown(
    """
    <style>
    img {
        border-radius: 50%;
        border: 5px solid white;
        box-shadow: 0px 0px 5px 2px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)


#*********************************************************************************************************************
# Add a navigation menu to the sidebar
selection = st.sidebar.radio('', list(pages.keys()))
# Call the appropriate page based on the user's menu choice
pages[selection]()
with st.container():
    st.write("")
    st.write("")
    st.write("")
    st.write( f'<p style="color:#334d4d;">Created by Tulasi NND</p>', unsafe_allow_html=True )
    
    
    # r"DCV/AI.png" , r"DCV/DATA_SCIENCE.png", r"DCV/GATE_2019.jpg", r"DCV/PY.jpg"
import streamlit as st

# Define CSS styles
css = """
/* Set max height for thumbnail images */
.thumbnail {
    height: 100px;
}

/* Set max height for full-size images */
.full-image {
    max-height: 80vh;
}

/* Remove padding and margins from modal */
.modal {
    padding: 0;
    margin: 0;
}
"""

# Define image URLs
image_urls = [
    'https://picsum.photos/200',
    'https://picsum.photos/200',
    'https://picsum.photos/200',
    'https://picsum.photos/200',
    'https://picsum.photos/200',
    'https://picsum.photos/200',
    'https://picsum.photos/200',
    'https://picsum.photos/200',
    'https://picsum.photos/200',
    'https://picsum.photos/200',
    'https://picsum.photos/200',
    'https://picsum.photos/200',
    'https://picsum.photos/200',
    'https://picsum.photos/200',
    'https://picsum.photos/200',
    'https://picsum.photos/200',
]

# Use st.markdown to display the CSS styles
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Define modal content
def modal_content(image_url):
    return f'<img class="full-image" src="{image_url}" />'

# Use the image URLs to display the images in a grid
for i in range(0, len(image_urls), 4):
    row = image_urls[i:i+4]
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if i < len(image_urls):
            image_url = row[0]
            if st.button(f'<img class="thumbnail" src="{image_url}" />', key=i):
                st.markdown(modal_content(image_url), unsafe_allow_html=True)
    with col2:
        if i+1 < len(image_urls):
            image_url = row[1]
            if st.button(f'<img class="thumbnail" src="{image_url}" />', key=i+1):
                st.markdown(modal_content(image_url), unsafe_allow_html=True)
    with col3:
        if i+2 < len(image_urls):
            image_url = row[2]
            if st.button(f'<img class="thumbnail" src="{image_url}" />', key=i+2):
                st.markdown(modal_content(image_url), unsafe_allow_html=True)
    with col4:
        if i+3 < len(image_urls):
            image_url = row[3]
            if st.button(f'<img class="thumbnail" src="{image_url}" />', key=i+3):
                st.markdown(modal_content(image_url), unsafe_allow_html=True)
