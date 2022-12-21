import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
st.title("Map")

path = '/Users/madisongeiger/Desktop/Quiz1/Final Project/Pages/'
skyscrapers = pd.read_csv(path + 'Skyscrapers2021.csv')
skyscrapers.rename(columns={"Latitude":"lat", "Longitude": "lon", "NAME": "Name"}, inplace= True)
for i in skyscrapers.index:
    skyscrapers.at[i, "Feet"] = skyscrapers.loc[i, "Feet"].replace(' ft', '')
    skyscrapers.at[i, "Feet"] = skyscrapers.loc[i, "Feet"].replace(',', '')
    skyscrapers.at[i, "Feet"] = int(skyscrapers.loc[i, "Feet"])
skyscrapers.set_index("RANK", inplace=True)


cities = []
materials = []
functions = []
for i in skyscrapers.itertuples():
    if i.CITY not in cities:
        cities.append(i.CITY)
    if i.MATERIAL not in materials:
        materials.append(i.MATERIAL)
    if i.FUNCTION not in functions:
        functions.append(i.FUNCTION)
cities = sorted(cities)
materials = sorted(materials)
functions = sorted(functions)

options = [" ", "All Skyscrapers", "Material", "Function"]


location = st.sidebar.selectbox("Please select the city you would like to view", cities)
chosen_options = st.sidebar.selectbox("Please select what you want to view", options)

city_df = skyscrapers[skyscrapers["CITY"].str.contains(location)]


city_df["lat"] = city_df["lat"].astype(float)
city_df["lon"] = city_df["lon"].astype(float)


if chosen_options == "All Skyscrapers":
    view_state = pdk.ViewState(
        latitude=city_df["lat"].mean(),
        longitude=city_df["lon"].mean(),
        zoom=11,
        pitch=40.5)
    layer = pdk.Layer(type='HexagonLayer',
        data=city_df,
        get_position='[lon, lat]',
        radius=200,
        elevation_scale=50,
        elevation_range=[0, 1000],
        pickable=True,
        extruded=True,
        coverage=1)
    map1 = pdk.Deck(initial_view_state=view_state,
                    layers=[layer])
    st.pydeck_chart(map1)
elif chosen_options == "Material":
    materials = st.sidebar.multiselect("Please select which materials you would like to see: ", materials)
    newdf = city_df[city_df["MATERIAL"].isin(list(materials))]
    view_state = pdk.ViewState(
        latitude=city_df["lat"].mean(),
        longitude=city_df["lon"].mean(),
        zoom=11,
        pitch=40.5)
    layer = pdk.Layer(type='HexagonLayer',
        data=newdf,
        get_position='[lon, lat]',
        radius=200,
        elevation_scale=50,
        elevation_range=[0, 1000],
        pickable=True,
        extruded=True,
        coverage=1)
    map1 = pdk.Deck(initial_view_state=view_state,
                    layers=[layer])
    st.pydeck_chart(map1)
elif chosen_options == "Function":
    functions = st.sidebar.multiselect("Please select which materials you would like to see: ", functions)
    newdf = city_df[city_df["FUNCTION"].isin(list(functions))]
    view_state = pdk.ViewState(
        latitude=city_df["lat"].mean(),
        longitude=city_df["lon"].mean(),
        zoom=11,
        pitch=40.5)
    layer = pdk.Layer(type='HexagonLayer',
        data=newdf,
        get_position='[lon, lat]',
        radius=200,
        pickable=True,
        extruded=True,
        coverage=1)
    map1 = pdk.Deck(initial_view_state=view_state,
                    layers=[layer])
    st.pydeck_chart(map1)

