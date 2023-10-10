import streamlit as st
import pydeck as pdk
import requests as rq
import json
import jwt
import pandas as pd

from utils.st_utils import footer



st.set_page_config(layout="wide", page_title="You do", page_icon="📜")

st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: white;}
        </style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Tasks</p>', unsafe_allow_html=True)




if __name__ == "__main__":
    footer()