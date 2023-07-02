import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

tag = st.selectbox('Choose a topic',['love','humor','life','books'])

generate=st.button("CSV")
url = f"https://quotes.toscrape.com/tag/{tag}/"

res = requests.get(url)
content = BeautifulSoup(res.content, 'html.parser' )

quotes = content.find_all('div', class_='quote')
quotes_files=[]
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    link=quote.find('a')
    st.success(text)
    st.write(author)
    st.markdown(f"<a href=https://quotes.toscrape.com{link['href']}>{author}</a>",unsafe_allow_html=True)
    quotes_files.append([text,author,link['href']])
if generate:
    df=pd.DataFrame(quotes_files)
    df.to_csv('quotes.csv',index=False,header=['Quotes','Authore','Link'],encoding='cp1252')





