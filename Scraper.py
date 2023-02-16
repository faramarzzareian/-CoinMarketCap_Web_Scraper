import streamlit as st
import requests
from bs4 import BeautifulSoup

# Set up the default URL and class name
default_url = 'https://coinmarketcap.com/currencies/ethereum/'
class_name = 'sc-d13d1ec-0 eNSKxK'

# Get the user input for the URL
url = st.text_input('Enter the URL:', default_url)

# Create a "Refresh" button to refresh the entire webpage
if st.button('Refresh'):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the <div> tag with the specified class
    div_tag = soup.find('div', {'class': class_name})

    # Check if the <div> tag was found
    if div_tag:
        # Extract the HTML content of the <div> tag
        div_html = str(div_tag)

        # Display the HTML content in a Streamlit app
        st.write(div_html, unsafe_allow_html=True)
    else:
        st.write(f"No <div> tag found with class: {class_name}")
