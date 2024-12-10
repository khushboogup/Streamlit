import time
import numpy as np
import pandas as pd
import streamlit as st
st.set_page_config(page_title="Hello World",page_icon='❤️',layout='wide')
with st.spinner('wait for it'):
     time.sleep(5)
     st.write('Thanks for being patient!')
with st.empty():
     for percent_completed in range(100):
         time.sleep(.1)
         st.progress(percent_completed+1,text='Processing')
     st.success('congratulations')
st.balloons()
st.snow()