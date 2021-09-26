import streamlit as st
import numpy as np
#import pandas as pd
#from PIL import Image
import time

st.title('Streamlit Test')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')  
    bar.progress(i + 1)                        
    time.sleep(0.001)                            

'Done!!!!!!'


left_column, right_column = st.beta_columns(2)

button = left_column.button('Display text in right column')
if button:
    right_column.write('This is the right column.')

expander1 = st.beta_expander('Inquiry 1')
expander1.write('Answer to inquiry 1')
expander2 = st.beta_expander('Inquiry 2')
expander2.write('Answer to inquiry 2')
expander3 = st.beta_expander('Inquiry 3')
expander3.write('Answer to inquiry 3')
