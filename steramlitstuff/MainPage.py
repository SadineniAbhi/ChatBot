import streamlit as st
st.title('Build your ChatBots')

st.header("Overview")
st.text('''
Take the Dockerfile, attach it with your data, and you will get
your personal deployable chatbot (LLM) built with RAG. Exposed as an api''')

""#THROW AWAY LINE

# Requirements
st.subheader('Requirements')
st.text('- Your data should be provided in a text file (.txt)')

""

st.text('''If you're building a chatbot for your website, check out the
web scraper on the site through which you can get your text file.
Note: This scraper only works if you are given scraping permission on
your website''')


