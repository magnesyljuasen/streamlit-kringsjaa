import streamlit as st
import pandas as pd
import numpy as np
import os
import folium
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from shapely.geometry import Point, Polygon
from folium.plugins import Fullscreen
import time
import base64
from PIL import Image


def streamlit_settings(title, icon):
    st.set_page_config(page_title=title, page_icon=icon, layout="wide")
    with open("src/styles/main.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    st.markdown(
        """<style>[data-testid="collapsedControl"] svg {height: 3rem;width: 3rem;}</style>""",
        unsafe_allow_html=True,
    )


streamlit_settings(title="Energy Plan Zero, Kringsjå", icon="h")
c1, c2 = st.columns([1.5, 1])
with c1:
    st.title("Energiplan Kringsjå")
with c2:
    st.image('src/img/sio-logo.png', use_column_width = "auto")

st.header("Innledning")

st.header("Dagens energi- og effektsituasjon")

st.header("Tiltak")

st.subheader("Utnyttelse av lokalt produsert elektrisitet")

st.subheader("Fremtidig energibruk")

st.subheader("Fjernvarme")

st.subheader("Grunnvarme")

st.subheader("Grunnvarme med sesonglagring")

st.subheader("Gråvannsgjenvinning")

st.subheader("Solvarme")

st.subheader("Solceller")

st.subheader("Lagring av strøm i batterier")

st.subheader("Reduksjon av effekttopper med varmelagring, evt. større varmepumpe")
