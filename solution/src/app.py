import streamlit as st
from src.password_generator import PinCodeGenerator,MemorablePasswordGenerator,RandomPasswordGenerator
from nltk.corpus import words

#Title of the application
st.image('./src/image/banner.jpeg')
st.title(":zap: Password Generator")

option = st.radio('Password Type', ['PinCodeGenerator', 'MemorablePasswordGenerator', 'RandomPasswordGenerator'])

if option == 'PinCodeGenerator':
    length = st.slider('Length', min_value=2, max_value=10, value=4)
    generator = PinCodeGenerator(length)

elif option == 'MemorablePasswordGenerator':
    no_of_words = st.slider("Number of Words", min_value=2, max_value=10, value=4)
    seperator = st.text_input('Seperator', value='-')
    capitalization = st.toggle("Capitalization")
    generator = MemorablePasswordGenerator(no_of_words, seperator, capitalization, words.words())

else:
    length = st.slider("Length", min_value=5, max_value=50, value=8)
    include_numbers = st.toggle("Include Numbers")
    include_symbols = st.toggle("Include Symbols")
    generator = RandomPasswordGenerator(length, include_numbers, include_symbols)


password = generator.generate()
st.write('Your Password is:')
st.header(fr'``` {password} ```')