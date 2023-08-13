import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime
import requests
import sklearn
import streamlit as st
# from streamlit_lottie import st_lottie
from PIL import Image
import pandas as pd
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn import preprocessing
PRIMARY_COLOR = "#1E88E5"
SECONDARY_COLOR = "#EEEEEE"
TEXT_COLOR = "#FFFFFF"
from streamlit_option_menu import option_menu




image_url = 'xyzz.png'  # replace with your image URL





def page1():
#        
        selected =option_menu(menu_title=None,
                              options=["home","Contact","about"],
                              orientation="horizontal",)
    

        if selected=="Contact":
           
            st.title(f" Personal Details")
            st.write("Name: Shivangi Singh")
            st.write("Email: shivangi.singh.btech.2021@sitpune.edu.in")
            st.write("Phone: 7388090977")
                       
            st.write("Name: Shivansh Nautiyal")
            st.write("Email: shivansh.nautiyal.btech.2021@sitpune.edu.in")
            st.write("Phone: 7388090977")
        if selected=="about":
            st.write("""
            <div style='text-align:center'>
                <h1>PROGNOSIS</h1>
                <h5>Predicting the Future of Engineering Skills, Today.</h5>
            </div>
            """, unsafe_allow_html=True)
            
            
            
            
            col1, col2 = st.columns(2)

            # Add the image to the first column
            with col1:
                st.image('assets/xrr.png', use_column_width=True)

            # Add the text to the second column
            with col2:
                st.write("The Prognosis project involves predicting which skills will be relevant for a particular job in the future. The project uses data that has been scraped from naukri.com, a job listing website, and then cleans and transforms it to create a time-series dataset. The project's primary goal is to analyze the frequency of different skills mentioned in job postings over time to predict which skills will be in demand in the future.                                                                                                   To create the dataset of different skills, the project uses web scraping techniques to extract data from job postings on naukri.com. This involves using a web automation tool like Selenium to navigate to job postings, extract the relevant data, and save it to a structured format like a CSV file. The team behind the project would have likely had to write custom scripts to handle different types of job postings, as well as dealing with any anti-scraping measures on the website.                                                                Once the raw data has been collected, the team then needs to clean and transform it to a format that is suitable for analysis. This involves removing any irrelevant data, handling missing values, and potentially combining data from different sources. For example, they might need to normalize skill names to a standard format to make them comparable across different job postings.                           To analyze the data, the team uses linear regression, a machine learning algorithm that can model the relationship between a dependent variable (in this case, the frequency of a skill in job postings) and one or more independent variables (such as time). By fitting a linear regression model to the dataset, the team can estimate the future trend of a skill's demand based on historical data.The Prognosis project is useful for providing evidence-based recommendations for students and job seekers regarding which skills to acquire for future job prospects. By using data and machine learning techniques, the project can provide concrete and reliable predictions about which skills will be in demand in the future. This information can be valuable for students who are trying to decide which courses to take or which skills to focus on, as well as for job seekers who are looking to improve their chances of getting hired.")

            
         
            
            
        if selected=="home":
            st.title(" " )
                    
            st.write("""
            <div style='text-align:center'>
                <h1>Select The Job In Which You Are Interest</h1>
                
            </div>
            """, unsafe_allow_html=True)
            job_options = ["Cloud Solutions Architect","Software Architect","Network Architect","Software Applications Architect","Data Architect","Solutions Architect","Computer and Information Research Scientist","Data Scientist","Information Systems Manager","Development Operations Engineer","IT Operations Manager","Data Engineer","Information Technology Manager","Hardware Engineer","Senior Web Developer","Software Engineer","Computer Hardware Engineer","Wireless RF Network Engineer"]
            
            job = st.selectbox("Select your job interest", options=job_options)
            col1, col2, col3 = st.columns(3)
            st.write("""
            <div style='text-align:center'>
            <h3>Please enter your graduation date Above.</h3>
            </div>
            """, unsafe_allow_html=True)        
            
            year = col1.number_input("Year Of Graduation", value=2023, step=1)
            month = col2.selectbox("Month", options=["January", "February", "March", "April", "May", "June", 
                                                     "July", "August", "September", "October", "November", "December"])
            day = col3.number_input("Day", value=1, min_value=1, max_value=31, step=1)

            # Save the graduation date as a string
            graduation_date = f"{day} {month} {year}"
            date_obj = datetime.strptime(graduation_date, '%d %B %Y')
            # Convert back to string in %Y-%m-%d format
            new_date_str = datetime.strftime(date_obj, '%Y-%m-%d')
            graduation_date =new_date_str


            if st.button("Submit"):
                st.markdown(
                f"""
                <style>
                div.stButton > button:first-child {{
                    background-color: {PRIMARY_COLOR} !important;
                }}
                </style>
                """,
                unsafe_allow_html=True
                )
                # Save the user's job interest and graduation date in session state
                st.session_state.job_interest = job
                st.session_state.graduation_date = graduation_date
                st.session_state["job"] = job
                st.experimental_rerun()

def page2():
    st.write("""
            <div style='text-align:center'>
                <h1>Job Interest Summary</h1>
                
            </div>
            """, unsafe_allow_html=True)

    st.markdown(f"Your job interest is: {st.session_state.job_interest}")
    st.markdown(f"You are graduating on: {st.session_state.graduation_date}")
    st.write("""
            <div style='text-align:center'>
                <h3>These are the top skills  that will be required in your desired job in the future </h3>
                
            </div>
            """, unsafe_allow_html=True)
    st.write("""
            <div style='text-align:center'>
                <h3>With Links to Online courses </h3>
                
            </div>
            """, unsafe_allow_html=True)
    job=st.session_state.job_interest
    job=str(job)
    graduation_date=st.session_state.graduation_date
    data = pd.read_csv("assets/"+job+'.csv')
    df=data
    # Convert the dates in the 'skills/dates' column to timestamps
    X = [datetime.strptime(date, '%Y-%m-%d').timestamp() for date in data['skills/dates']]
    X = np.array(X).reshape(-1, 1)

    # Train a linear regression model for each skill
    models = {}
    for skill in data.columns[1:]:
        y = data[skill].values
        model = LinearRegression()
        model.fit(X, y)
        models[skill] = model

    # Convert the future date string into a timestamp
    future_date = datetime.strptime('2028-01-01', '%Y-%m-%d').timestamp()

    # Use the models to predict the relevance of each skill on the future date
    predicted_values = {}
    for skill, model in models.items():
        
        predicted_values[skill] = model.predict([[future_date]])[0]
    top_skills = sorted(predicted_values.items(), key=lambda x: x[1], reverse=True)[:3]

    
    dataC=pd.read_csv("assets/Cloud Solutions Architect course.csv")
    

    top_skills_courses = {}
    Link={}
    p=[]
    
    for skill, value in top_skills:
        # Find the row in the dataC DataFrame that matches the skill
        row = dataC.loc[dataC['Skill'] == skill]

        # Extract the related courses for the skill
        courses = row['Name of the course'].values[0]

        # Add the skill and its related courses to the dictionary
        top_skills_courses[skill] = courses

        # Print the skill and its related courses
#         st.write(f"{skill}: {value}")
        
        
                # label_encoder object knows how to understand word labels.
        
        st.write(f"{skill}: {value}")
#         st.write(f" {courses}")
        x=(f"{skill}")
        p.append(x)
        label_encoder = preprocessing.LabelEncoder()
        # Encode labels in column 'species'.
        df['skills/dates']= label_encoder.fit_transform(df['skills/dates'])
        df['skills/dates'].unique()

        for i, row in row.iterrows():
            st.write(f"- {row['Name of the course']}: {row['Link']}")
    
    
    
    
    
    
    first = list(df.columns)
    l=[]
    # Set plot style
    plt.style.use('dark_background')

    # Set line colors
    colors = ['red', 'green', 'blue']
    st.write("""
            <div style='text-align:center'>
                <h3>Graphs showing trends of the skills Recommended   </h3>
                
            </div>
            """, unsafe_allow_html=True)
    # Loop over the data frames
    for i in range(3):
        # Fit linear regression
        x = np.arange(df['skills/dates'].size)
        fit = np.polyfit(x, df[p[i]], deg=1)
        l.append(str(fit[0]))
        fit_function = np.poly1d(fit)

        # Create plot figure
        fig = plt.figure(figsize=(7,4))

        # Plot linear regression line
        plt.plot(df['skills/dates'], fit_function(x), color=colors[i], linewidth=2)

        # Plot time series data
        plt.plot(df['skills/dates'], df[p[i]], color=colors[i], linewidth=1, alpha=0.7)

        # Set plot labels and title
        plt.xticks(rotation=90)
        plt.xlabel('Dates')
        plt.ylabel('Trends')
        plt.title(p[i], fontsize=16)

        # Save plot to file and display in streamlit
        plt.savefig("xyzz.png", bbox_inches='tight', dpi=150)
        image = Image.open("xyzz.png")
        st.image(image, width=700)
        

    

def main():
    

    from PIL import Image
    image_directory = "assets/image.jpg"
    image = Image.open(image_directory)
    PAGE_CONFIG = {"page_title":"Prognosis", 
                   "page_icon":image, 
                   "layout":"wide", 
                   "initial_sidebar_state":"auto"}

    st.set_page_config(**PAGE_CONFIG)
    
    # Define the pages of the app
    pages = {"Page 1": page1, "Page 2": page2}
    
    # Check if the user has visited the app before
    if "visited" not in st.session_state:
        st.session_state.visited = False
    
    # Show the appropriate page based on whether the user has visited the app before
    if st.session_state.visited:
        pages["Page 2"]()
    else:
        pages["Page 1"]()
    
    # Set visited to True after the user submits their name
    if "job" in st.session_state:
        st.session_state.visited = True

if __name__ == "__main__":
    main()