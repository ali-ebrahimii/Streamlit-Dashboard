import streamlit as st
import pandas as pd
import datetime

st.write('Hello World!!!')
st.button('hi')
'''__________________________________________________'''

x = st.slider('slider test', 0, 50, 25)
st.write(f'x value is {x}')

'''__________________________________________________'''

choice = st.selectbox('SelectBox test',['a','b','c','ali'])
st.write(f'choice value is {choice}')
'''__________________________________________________'''

choice = st.multiselect('MultiSelect test',['a','b','c','ali'])
st.write(f'choice value is {choice}')

'''__________________________________________________'''

st.download_button('DownloadButton', data='ali')

'''__________________________________________________'''

choice = st.radio('DownloadButton', ['good', 'bad', 'verybad'])
st.write(f'choice value is {choice}')

'''__________________________________________________'''

if st.checkbox('show'):
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['col1','col2','col3'])
    df
    st.bar_chart(df)

'''__________________________________________________'''

d = st.date_input("when is your birthday?", datetime.date(2019,7,6))
date = st.write('your birthday is :', d)

'''__________________________________________________'''


