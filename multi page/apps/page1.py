#!/usr/bin/env python

from shapely import wkt
import streamlit as st
import geopandas as gpd
import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
from streamlit_card import card
import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components


def app():



    st.markdown("## Welcome to Traffic Simulator")


    res = card(
                title="Welcome to Traffic & Air Quality Simulator Dashboard",
                text="A Traffic & Air Quality Simulator is software that models how traffic affects air pollution. \n It predicts how changes in traffic flow and vehicle types impact air quality, helping planners \n and policymakers make decisions to reduce pollution.",
                image=" https://images.unsplash.com/photo-1575039837939-11948b3b9907?q=80&w=3862&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                styles={"card": {"width": "100%", "height": "500px"}})



    with st.form("my_form"):
        st.write("Select City")
        option = st.selectbox(
                             'Select City to start simulation',
                            ('Birmingham',
                             'Cambridge',
                             'Bicester',
                             'Coventry',
                             'Oxford',
                             'London'))
        option = option[:3]


        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
    if submitted:
            

            fp=f'.\\data\\{option}.csv'
            df = pd.read_csv(fp)
            df['geometry'] = df['geometry'].apply(wkt.loads)
            emission = gpd.GeoDataFrame(df, crs='epsg:4326')



            # st.write("This is a kepler.gl map with data input in streamlit")
            
            map_1 = KeplerGl( height=700)
            map_1.add_data(emission) 
            keplergl_static(map_1)
            

            
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                res = card(
                title="Mean PMX Amount",
                text=f"{round(emission['@PMx'].astype('float').mean(),2)}",
                image="https://images.unsplash.com/photo-1513026705753-bc3fffca8bf4?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                styles={ "card": { "width": "100%", "height": "500px" }})

            with col2:
                res = card(
                title="Mean CO Amount",
                text=f"{round(emission['@CO'].astype('float').mean(),2)}",
                image="https://images.unsplash.com/photo-1561620831-9b2d86d81226?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                styles={ "card": { "width": "100%", "height": "500px" }})
        

            with col3:
                res = card(
                title="Mean CO2 Amount",
                text=f"{round(emission['@CO2'].astype('float').mean(),2)}",
                image="https://images.unsplash.com/photo-1578604665675-9aee692f6ddc?q=80&w=3931&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                styles={ "card": { "width": "100%", "height": "500px" }})
                        
                        
                
            with col4:
                res = card(
                title="Mean NOx Amount",
                text=f"{round(emission['@NOx'].astype('float').mean(),2)}",
                image="https://images.unsplash.com/photo-1580133750060-05e667fe0318?q=80&w=3871&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                styles={ "card": { "width": "100%", "height": "500px" }})
                        

        
            
   
            
            pyg_html = pyg.to_html(df)
            components.html(pyg_html, height=1000, scrolling=True)


 



        # pk.eyJ1Ijoiam9obmhhbGRlbWFuIiwiYSI6ImNrMjIxNnBrdTAxN3Mzb3BmbWFzbnV6OGoifQ.HrfAiASrw9EQetZn13xAPg


        # https://api.maptiler.com/maps/streets-v2/style.json?key=Se3Mih2LpHW0zw3QOjH1


        # mapbox://styles/mapbox/navigation-night-v1