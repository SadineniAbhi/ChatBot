import streamlit as st
st.title('Build your ChatBots')

st.header("Overview")
st.text('''
Take the Dockerfile, attach it with your data, and you will get
your personal deployable chatbot (LLM) built with retreival augumentation 
generation(RAG) which is exposed as an api.''')

""#THROW AWAY LINE

# Requirements
st.subheader('Requirements')
st.text('- Your data should be provided in a text file (.txt)')

""

st.text('''If you're building a chatbot for your website, check out the
web scraper on the site through which you can get data from your website
as an text file.
        
Note: This scraper only works if you give scraping permission on
your website''')


