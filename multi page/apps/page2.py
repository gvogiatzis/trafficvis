#!/usr/bin/env python

from shapely import wkt
import streamlit as st
import pandas as pd
import geopandas as gpd
import pygwalker as pyg
import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import streamlit.components.v1 as components
from streamlit_card import card


def app():


    res = card(
    title="Streamlit Card",
    text="This is a test card",
    image=" https://images.unsplash.com/photo-1575039837939-11948b3b9907?q=80&w=3862&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    styles={ "card": { "width": "100%", "height": "500px" }})
                        

    
    st.markdown("## Welcome to Traffic Simulator")

    col1, col2 = st.columns(2)
    with col1:
        
      
        df = pd.read_csv(r'.\data\time_based.csv')
        df['geometry'] = df['geometry'].apply(wkt.loads)
        emission = gpd.GeoDataFrame(df, crs='epsg:4326')
        
  
        res = card(
        title="Timed signal control",
        text=f"CO2: {round(emission['@CO2'].sum(),2)} | Waiting Time: {round(emission['@waiting'].sum(),2)}",
        image="https://images.unsplash.com/photo-1513026705753-bc3fffca8bf4?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        styles={ "card": { "width": "100%", "height": "500px" }})
            
            
        res = card(
        title="Timed signal control Emission Cost",
        text=f"CO2: {round(emission['@CO2'].sum(),2)} | Waiting Time: {round(emission['@waiting'].sum(),2)}",
        image="https://images.unsplash.com/photo-1465447142348-e9952c393450?q=80&w=3774&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        styles={ "card": { "width": "100%", "height": "500px" }})
        
        
        
        


        map_1 = KeplerGl( height=700)
        map_1.add_data(emission) 
        keplergl_static(map_1)   
        pyg_html = pyg.to_html(df)
        components.html(pyg_html, height=700, scrolling=True)
                
                

    with col2:
        
     
        df1 = pd.read_csv(r'.\data\rl_based.csv')
        df1['geometry'] = df1['geometry'].apply(wkt.loads)
        emission1 = gpd.GeoDataFrame(df1, crs='epsg:4326')
        
        
        
        res = card(
        title="Deep RL policy-based signal control",
        text=f"CO2: {emission1['@CO2'].sum()} | Waiting Time: {emission1['@waiting'].sum()}",
        image="https://images.unsplash.com/photo-1513026705753-bc3fffca8bf4?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        styles={ "card": { "width": "100%", "height": "500px" }})
        
        res = card(
        title="Deep RL policy-based signal control Cost",
        text=f"CO2: {round(emission1['@CO2'].sum(),2)} | Waiting Time: {round(emission1['@waiting'].sum(),2)}",
        image="https://images.unsplash.com/photo-1465447142348-e9952c393450?q=80&w=3774&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        styles={ "card": { "width": "100%", "height": "500px" }})
            


        map_1 = KeplerGl( height=700)
        map_1.add_data(emission1)
        keplergl_static(map_1)
        pyg_html = pyg.to_html(df1)
        components.html(pyg_html, height=700, scrolling=True)
  

    # pk.eyJ1Ijoiam9obmhhbGRlbWFuIiwiYSI6ImNrMjIxNnBrdTAxN3Mzb3BmbWFzbnV6OGoifQ.HrfAiASrw9EQetZn13xAPg


    # https://api.maptiler.com/maps/streets-v2/style.json?key=Se3Mih2LpHW0zw3QOjH1


    # mapbox://styles/mapbox/navigation-night-v1
    
    
    
    
    
    
    
    
    
    
