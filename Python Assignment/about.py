import streamlit as st
import json 
from streamlit_lottie import st_lottie 
import os
  
  
path = "D:\\Python Assignment\\Animation.json"
with open(path,"r") as file: 
    url = json.load(file) 

path1 = "D:\\Python Assignment\\Animation1.json"
with open(path1,"r") as file: 
    url1 = json.load(file) 
def about_page():
    st.title("About")
    st.subheader("Heyy There 🙋!!, This is Developed by Samarth A")
    st.write("Welcome to My Dashboard! Here you can explore the capabilities of DataWhisper - the Generative AI, and Data Analysis.")
    
    st_lottie(url, 
              height=400, 
              width=400, 
              speed=1, 
              loop=True, 
              quality='high', 
              key='Gemini AI'
    )
    st.header("DataWhisper - the Generative AI")
    st.write("I have integrated the Gemini API into our application to power our Chatbot, providing users with a seamless and interactive experience. By leveraging the Gemini API's capabilities, our Chatbot is able to efficiently process user queries, provide relevant information, and perform actions based on user inputs. This integration enhances the overall functionality of our application, making it more user-friendly and responsive.")
    
    st_lottie(url1, 
              height=400, 
              width=400, 
              speed=1, 
              loop=True, 
              quality='high', 
              key='Data Analysis'
    )
    st.header("Generative AI Data Analysis")
    st.write("My project utilizes Generative AI to analyze data, specifically focusing on the Generative AI Impact dataset. This dataset provides valuable insights into various aspects of AI's impact, helping us understand its influence on different aspects. By leveraging Generative AI, I aim to uncover meaningful patterns and trends, driving innovation and informed decision-making.")
    

about_page()
