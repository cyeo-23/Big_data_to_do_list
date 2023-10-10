import streamlit as st
import pydeck as pdk
import requests as rq

from utils.st_utils import footer

st.set_page_config(layout="wide", page_title="You do", page_icon="📜")

st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: white;}
        </style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Accueil</p>', unsafe_allow_html=True)

st.sidebar.success("Select an option above.")

kpi2, kpi4 = st.columns(2)

kpi4.markdown(
        """<style>align-items: center; display: flex; flex-direction: column;</style>""", unsafe_allow_html=True)
kpi2.markdown(
        """<style>align-items: center; display: flex; flex-direction: column;</style>""", unsafe_allow_html=True)

kpi4.metric(
        label="Metric 2",
        value=5,
    )

kpi2.metric(
        label="Metric 1",
        value=456,
    )

if __name__ == "__main__":
    footer()