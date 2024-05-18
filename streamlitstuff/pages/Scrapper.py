import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)
from crawlers.scrapper import scrape_website

import streamlit as st
st.title('Scrape your website here')

with st.form("my_form"):
   st.write("Enter the url:-")
   url = st.text_input("Enter URL")
   submit_button = st.form_submit_button("Submit")

if submit_button:
    with st.status("Downloading data...", expanded=True) as status:
        st.write("Searching for data...")
        st.write("Found URL.")
        st.write("Downloading data...")
        scrape_website(url)
        status.update(label="Download complete!", state="complete", expanded=False)
    st.write("Downloading zip file...")

    # Downloads the zip file
    zip_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/zipeddata"
    with open(zip_path, "rb") as f:
        data = f.read()
    st.download_button(label="Download Zip", data=data, file_name="scrapped_data & log_files.zip", mime="application/zip")


