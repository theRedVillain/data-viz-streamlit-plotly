import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('india.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')
primary_feature=  list(df.columns[[2,3,4,8,9]])
secondary_feature=  list(df.columns[[2,3,4,8,9]])
st.set_page_config('wide')
st.sidebar.title('India Data Visualization')
select_state = st.sidebar.selectbox('Select One',list_of_states)
st.sidebar.subheader('Primary Parameters')
select_primary = st.sidebar.selectbox('Select Primary Feature',primary_feature)
st.sidebar.subheader('Secondary Parameters')
select_secondary = st.sidebar.selectbox('Select Secondary Feature',secondary_feature)
btn = st.sidebar.button('Plot Visualisation')
if btn:
    if select_state == 'Overall India':
        fig = px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size = select_primary,color=select_secondary,zoom=3,mapbox_style = "carto-positron",size_max=40,height=700,width=1000)

        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df= df[df['State'] == select_state]
        fig = px.scatter_mapbox(state_df,lat='Latitude',lon='Longitude',size = select_primary,color=select_secondary,zoom=6,mapbox_style = "carto-positron",size_max=20,height=700,width=1000,hover_name='District name',color_continuous_scale=px.colors.cyclical.IceFire)

        st.plotly_chart(fig,use_container_width=True)


