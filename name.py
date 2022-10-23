import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import hiplot as hip
import altair as alt
st.set_page_config(layout="wide")

st.markdown(""" <style> .font_title {
font-size:50px ; font-family: 'times'; color: black;text-align: center;} 
</style> """, unsafe_allow_html=True)
st.markdown(""" <style> .font_header {
font-size:50px ; font-family: 'times'; color: black;text-align: left;} 
</style> """, unsafe_allow_html=True)
st.markdown(""" <style> .font_subheader {
font-size:35px ; font-family: 'times'; color: black;text-align: left;} 
</style> """, unsafe_allow_html=True)
st.markdown(""" <style> .font_text {
font-size:20px ; font-family: 'times'; color: black;text-align: left;} 
</style> """, unsafe_allow_html=True)

st.markdown('<p class="font_title">Indoor Plant Growth</p>', unsafe_allow_html=True)

st.image("https://www.springwise.com/wp-content/uploads/2022/03/innovationsustainabilitycaptured-CO2-used-in-greenhouses.png")

#st.markdown(r'Numerous factors regulate plant growth and cultivation yield including temperature, CO$_2$ concentration, nutrients, and the intensity and quality of light.', unsafe_allow_html=True)
st.markdown(r'<p class="font_text">Numerous factors regulate plant growth and cultivation yield including temperature, carbon dioxide concentration, relative humidity, and the intensity and quality of light.: </p>', unsafe_allow_html=True)
#st.markdown(r'For better comparison incoming spectra are divided into 100 nm wavebands : Blue (B) $(400-500)$, Green (B) $(500-600)$, Red (R) $(600-700)$, Far-Red (FR) $(700-800)$ nm', unsafe_allow_html=True)
st.markdown('<p class="font_text">For better comparison incoming spectra are divided into 100 nm wavebands : Blue (B) 400 to 500 nm, Green (B) 500 to 600 nm, Red (R) 600 to 700 nm, Far-Red (FR) 700 to 800 nm: </p>', unsafe_allow_html=True)

st.markdown('<p class="font_header">Data: </p>', unsafe_allow_html=True)

st.markdown('<p class="font_subheader">Light Treatment: </p>', unsafe_allow_html=True)

st.markdown('<p class="font_subheader">Plant Data: </p>', unsafe_allow_html=True)

st.markdown('<p class="font_header">References: </p>', unsafe_allow_html=True)
st.markdown('Data used for plant growth visualization are obtained from the following refrences:', unsafe_allow_html=False)
st.markdown('1) Meng, Q., Boldt, J., and Runkle, E. S. (2020). Blue radiation interacts with green radiation to influence growth and predominantly controls quality attributes of lettuce. Journal of the American Society for Horticultural Science 145, 75–87280.', unsafe_allow_html=False)
st.markdown('2) Meng, Q., Kelly, N., and Runkle, E. S. (2019). Substituting green or far-red radiation for blue radiation induces shade avoidance and promotes growth in lettuce and kale. Environmental and experimental botany 162, 383–391283.', unsafe_allow_html=False)
st.markdown('3) Meng, Q. and Runkle, E. S. (2019). Far-red radiation interacts with relative and absolute blue and red photon flux densities to regulate growth, morphology, and pigmentation of lettuce and basil seedlings. Scientia Horticulturae 255, 269–280.', unsafe_allow_html=False)
st.markdown('4) Controlled Environment Agriculture Open Data - Lettuce: https://ceaod.github.io/download/#url=GH_Lettuce/LumiGrow.', unsafe_allow_html=True)