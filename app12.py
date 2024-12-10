import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
st.title('Visualization with plotly')
df=pd.read_csv('/Users/khushboogupta/Files/Streamlit/tips.csv')
st.dataframe(df.head())
st.text('1. Pie Chart')
fig=px.pie(df,values='total_bill',names='day')
st.plotly_chart(fig)
st.text('2. Pie Chart with Hole')
fig=px.pie(df,values='total_bill',names='day',opacity=.8,hole=.5,color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)
st.title('Interractive Graphs with Plotly')
x1=np.random.randn(200)+2
x2=np.random.randn(200)
x3=np.random.randn(200)-2
hist_data=[x1,x2,x3]
group_lbls = ['G1','G2','G3']
fig = ff.create_distplot(hist_data, group_lbls, bin_size = [.1, .1,.1])
st.plotly_chart(fig, use_container_width = True)
