import streamlit as st
import pandas as pd
import datetime
import numpy as np

col1, col2,col3 = st.columns(3)

col1.write('column1')
with col1:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    col1.line_chart(chart_data)

with col2:
    col2.write('column2')
    txt = col2.text_area("Ali","Hi!\nThis is my first streamlit project")
    col2.write(f'You wrote {len(txt)} characters.')

with col3:
    col3.write('column3')
    color = col3.color_picker('Pick A Color', '#00f900')
    col3.write(f'The current color is {color}')