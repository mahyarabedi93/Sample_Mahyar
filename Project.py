import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import hiplot as hip
import altair as alt
import plotly.express as px

####################################################################################################################################################################
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")

####################################################################################################################################################################

st.markdown(""" <style> .font_title {
font-size:50px ; font-family: 'times'; color: black;text-align: center;} 
</style> """, unsafe_allow_html=True)

st.markdown(""" <style> .font_header {
font-size:50px ; font-family: 'times'; color: black;text-align: left;} 
</style> """, unsafe_allow_html=True)

st.markdown(""" <style> .font_subheader {
font-size:35px ; font-family: 'times'; color: black;text-align: left;} 
</style> """, unsafe_allow_html=True)

st.markdown(""" <style> .font_subsubheader {
font-size:28px ; font-family: 'times'; color: black;text-align: left;} 
</style> """, unsafe_allow_html=True)

st.markdown(""" <style> .font_text {
font-size:20px ; font-family: 'times'; color: black;text-align: left;} 
</style> """, unsafe_allow_html=True)

st.markdown(""" <style> .font_subtext {
font-size:18px ; font-family: 'times'; color: black;text-align: center;} 
</style> """, unsafe_allow_html=True)

####################################################################################################################################################################

st.markdown('<p class="font_title">Indoor Plant Growth</p>', unsafe_allow_html=True)

####################################################################################################################################################################

st.image("https://www.springwise.com/wp-content/uploads/2022/03/innovationsustainabilitycaptured-CO2-used-in-greenhouses.png")

####################################################################################################################################################################

st.markdown('<p class="font_text">Numerous factors regulate plant growth and cultivation yield including temperature, carbon dioxide concentration, relative humidity, and the intensity and quality of light. </p>', unsafe_allow_html=True)
st.markdown('<p class="font_text">The goal for this part of the project is to investigate the available data for indoor lettuce cultivar for a possible trend between the investigated features and the cultivation yield. </p>', unsafe_allow_html=True)
st.markdown('<p class="font_text">For better comparison incoming spectra are divided into 100 nm wavebands : Blue (B) 400 to 500 nm, Green (B) 500 to 600 nm, Red (R) 600 to 700 nm, Far-Red (FR) 700 to 800 nm. </p>', unsafe_allow_html=True)

####################################################################################################################################################################

st.markdown('<p class="font_header">Data: </p>', unsafe_allow_html=True)

####################################################################################################################################################################

st.markdown('<p class="font_subheader">Light Treatment: </p>', unsafe_allow_html=True)

Light_Treatments = pd.read_csv("Light Data All.csv")

st.table(Light_Treatments.describe())
st.markdown('<p class="font_subtext">Table 1: Statistical properties of various light treatment.</p>', unsafe_allow_html=True)

####################################################################################################################################################################

st.sidebar.markdown('<p class="font_text">Fig. 1: Spectral Visualization:</p>', unsafe_allow_html=True)

Light_Treatment_Name = st.sidebar.selectbox(
    "Fig. 1: Light Treatment:",
    ['B30R150' , 'B30R150FR30' , 'R180FR30' , 'B90R90' , 'B90R90FR30' , 'B180FR30' , 'B90R90FR75' , 'B180R180' , 'B180R180FR30' , 'B180R180FR75' , 'B60R120' , 'B40G20R120' , 'B20G40R120' , 'G60R120' , 'B40R120FR20' , 'B20R120FR40' , 'R120FR60' , 'B20G20R120FR20' , 'R180' , 'B20R160' , 'B20G60R100' , 'B60G60R60' , 'B100R80' , 'B100G60R20' , 'EQW180' , 'EQW100B10R70' , 'EQW100B50R30' , 'WW180' , 'Greenhouse'])
    
if Light_Treatment_Name != "Greenhouse":
    Figure=plt.figure(figsize=(12,4))
    plt.subplot(1,2,1)
    plt.plot(Light_Treatments['Wavelength'] , Light_Treatments[Light_Treatment_Name], linewidth=1,color='black')
    plt.title(Light_Treatment_Name)
    plt.fill_between(Light_Treatments['Wavelength'].loc[(Light_Treatments['Wavelength']>=400) & (Light_Treatments['Wavelength']<=500) ], Light_Treatments[Light_Treatment_Name].loc[(Light_Treatments['Wavelength']>=400) & (Light_Treatments['Wavelength']<=500) ], color='blue')
    plt.fill_between(Light_Treatments['Wavelength'].loc[(Light_Treatments['Wavelength']>=500) & (Light_Treatments['Wavelength']<=600) ], Light_Treatments[Light_Treatment_Name].loc[(Light_Treatments['Wavelength']>=500) & (Light_Treatments['Wavelength']<=600) ], color='green')
    plt.fill_between(Light_Treatments['Wavelength'].loc[(Light_Treatments['Wavelength']>=600) & (Light_Treatments['Wavelength']<=700) ], Light_Treatments[Light_Treatment_Name].loc[(Light_Treatments['Wavelength']>=600) & (Light_Treatments['Wavelength']<=700) ], color='red')
    plt.fill_between(Light_Treatments['Wavelength'].loc[(Light_Treatments['Wavelength']>=700) & (Light_Treatments['Wavelength']<=800) ], Light_Treatments[Light_Treatment_Name].loc[(Light_Treatments['Wavelength']>=700) & (Light_Treatments['Wavelength']<=800) ], color='darkred')
    plt.axvline(x = 400, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 500, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 600, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 700, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 800, linewidth=1,linestyle='--',color='black')
    plt.xticks(ticks=[400,500,600,700,800])
    plt.xlim(300,900)
    plt.grid(which='both',axis='both',color='grey', linestyle='--', linewidth=.3)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Photon Flux Density')
    plt.subplot(1,2,2)
    plt.plot(Light_Treatments['Wavelength'] , Light_Treatments['Energy '+Light_Treatment_Name], linewidth=1,color='black')
    plt.title(Light_Treatment_Name)
    plt.fill_between(Light_Treatments['Wavelength'].loc[(Light_Treatments['Wavelength']>=400) & (Light_Treatments['Wavelength']<=500) ], Light_Treatments['Energy '+Light_Treatment_Name].loc[(Light_Treatments['Wavelength']>=400) & (Light_Treatments['Wavelength']<=500) ], color='blue')
    plt.fill_between(Light_Treatments['Wavelength'].loc[(Light_Treatments['Wavelength']>=500) & (Light_Treatments['Wavelength']<=600) ], Light_Treatments['Energy '+Light_Treatment_Name].loc[(Light_Treatments['Wavelength']>=500) & (Light_Treatments['Wavelength']<=600) ], color='green')
    plt.fill_between(Light_Treatments['Wavelength'].loc[(Light_Treatments['Wavelength']>=600) & (Light_Treatments['Wavelength']<=700) ], Light_Treatments['Energy '+Light_Treatment_Name].loc[(Light_Treatments['Wavelength']>=600) & (Light_Treatments['Wavelength']<=700) ], color='red')
    plt.fill_between(Light_Treatments['Wavelength'].loc[(Light_Treatments['Wavelength']>=700) & (Light_Treatments['Wavelength']<=800) ], Light_Treatments['Energy '+Light_Treatment_Name].loc[(Light_Treatments['Wavelength']>=700) & (Light_Treatments['Wavelength']<=800) ], color='darkred')
    plt.axvline(x = 400, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 500, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 600, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 700, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 800, linewidth=1,linestyle='--',color='black')
    plt.xticks(ticks=[400,500,600,700,800])
    plt.xlim(300,900)
    plt.grid(which='both',axis='both',color='grey', linestyle='--', linewidth=.3)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Spectral Energy')
else:
    Figure=plt.figure(figsize=(12,2))
    plt.subplot(1,2,1)
    plt.plot(Light_Treatments['Greenhouse Wavelength'] , Light_Treatments[Light_Treatment_Name], linewidth=1,color='black')
    plt.title(Light_Treatment_Name)
    plt.fill_between(Light_Treatments['Greenhouse Wavelength'].loc[(Light_Treatments['Greenhouse Wavelength']>=400) & (Light_Treatments['Greenhouse Wavelength']<=500) ], Light_Treatments[Light_Treatment_Name].loc[(Light_Treatments['Greenhouse Wavelength']>=400) & (Light_Treatments['Greenhouse Wavelength']<=500) ], color='blue')
    plt.fill_between(Light_Treatments['Greenhouse Wavelength'].loc[(Light_Treatments['Greenhouse Wavelength']>=500) & (Light_Treatments['Greenhouse Wavelength']<=600) ], Light_Treatments[Light_Treatment_Name].loc[(Light_Treatments['Greenhouse Wavelength']>=500) & (Light_Treatments['Greenhouse Wavelength']<=600) ], color='green')
    plt.fill_between(Light_Treatments['Greenhouse Wavelength'].loc[(Light_Treatments['Greenhouse Wavelength']>=600) & (Light_Treatments['Greenhouse Wavelength']<=700) ], Light_Treatments[Light_Treatment_Name].loc[(Light_Treatments['Greenhouse Wavelength']>=600) & (Light_Treatments['Greenhouse Wavelength']<=700) ], color='red')
    plt.fill_between(Light_Treatments['Greenhouse Wavelength'].loc[(Light_Treatments['Greenhouse Wavelength']>=700) & (Light_Treatments['Greenhouse Wavelength']<=800) ], Light_Treatments[Light_Treatment_Name].loc[(Light_Treatments['Greenhouse Wavelength']>=700) & (Light_Treatments['Greenhouse Wavelength']<=800) ], color='darkred')
    plt.axvline(x = 400, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 500, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 600, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 700, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 800, linewidth=1,linestyle='--',color='black')
    plt.xticks(ticks=[400,500,600,700,800])
    plt.xlim(300,900)
    plt.grid(which='both',axis='both',color='grey', linestyle='--', linewidth=.3)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Photon Flux Density')
    plt.subplot(1,2,2)
    plt.plot(Light_Treatments['Greenhouse Wavelength'] , Light_Treatments['Energy '+Light_Treatment_Name], linewidth=1,color='black')
    plt.title(Light_Treatment_Name)
    plt.fill_between(Light_Treatments['Greenhouse Wavelength'].loc[(Light_Treatments['Greenhouse Wavelength']>=400) & (Light_Treatments['Greenhouse Wavelength']<=500) ], Light_Treatments['Energy '+Light_Treatment_Name].loc[(Light_Treatments['Greenhouse Wavelength']>=400) & (Light_Treatments['Greenhouse Wavelength']<=500) ], color='blue')
    plt.fill_between(Light_Treatments['Greenhouse Wavelength'].loc[(Light_Treatments['Greenhouse Wavelength']>=500) & (Light_Treatments['Greenhouse Wavelength']<=600) ], Light_Treatments['Energy '+Light_Treatment_Name].loc[(Light_Treatments['Greenhouse Wavelength']>=500) & (Light_Treatments['Greenhouse Wavelength']<=600) ], color='green')
    plt.fill_between(Light_Treatments['Greenhouse Wavelength'].loc[(Light_Treatments['Greenhouse Wavelength']>=600) & (Light_Treatments['Greenhouse Wavelength']<=700) ], Light_Treatments['Energy '+Light_Treatment_Name].loc[(Light_Treatments['Greenhouse Wavelength']>=600) & (Light_Treatments['Greenhouse Wavelength']<=700) ], color='red')
    plt.fill_between(Light_Treatments['Greenhouse Wavelength'].loc[(Light_Treatments['Greenhouse Wavelength']>=700) & (Light_Treatments['Greenhouse Wavelength']<=800) ], Light_Treatments['Energy '+Light_Treatment_Name].loc[(Light_Treatments['Greenhouse Wavelength']>=700) & (Light_Treatments['Greenhouse Wavelength']<=800) ], color='darkred')
    plt.axvline(x = 400, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 500, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 600, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 700, linewidth=1,linestyle='--',color='black')
    plt.axvline(x = 800, linewidth=1,linestyle='--',color='black')
    plt.xticks(ticks=[400,500,600,700,800])
    plt.xlim(300,900)
    plt.grid(which='both',axis='both',color='grey', linestyle='--', linewidth=.3)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Spectral Energy')
st.pyplot(Figure)
st.markdown('<p class="font_subtext">Fig. 1: Photon and energy distribution for various investigated light treatment.</p>', unsafe_allow_html=True)

####################################################################################################################################################################

st.markdown('<p class="font_subheader">Plant Data: </p>', unsafe_allow_html=True)

Plant_Data=pd.read_csv("Project Data.csv")

st.table(Plant_Data.describe())

st.markdown('<p class="font_subtext">Table 2: Statistical properties of lettuce cultivated under different light treatment and environmental conidtions.</p>', unsafe_allow_html=True)

####################################################################################################################################################################

col3,col4=st.columns(2,gap='small')

source = pd.DataFrame({"category": ['Rouxai','Rex','Cherokee'], "value": [Plant_Data.loc[Plant_Data["Species"]=="Rouxai"].shape[0],
                                                Plant_Data.loc[Plant_Data["Species"]=="Rex"].shape[0],
                                                Plant_Data.loc[Plant_Data["Species"]=="Cherokee"].shape[0]]})

d=alt.Chart(source).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="category", type="nominal",
                    scale=alt.Scale(scheme='rainbow'))
)

col3.altair_chart(d, use_container_width=True)

Cat=[]
for i in Light_Treatments.columns:
    if ('(' not in i) & ("Energy" not in i) & ("Wave" not in i):
        Cat=np.append(Cat,i)
        
value=[];
for i in Cat:
    value=np.append(value,Plant_Data.loc[Plant_Data["Treatment"]==i].shape[0])
source1 = pd.DataFrame({"category": Cat, "value": value})

g=alt.Chart(source1).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="category", type="nominal",
                    scale=alt.Scale(scheme='rainbow'))
)

col4.altair_chart(g, use_container_width=True)

st.markdown('<p class="font_subtext">Fig. 2: Categorical distribution of experimental observations.</p>', unsafe_allow_html=True)

####################################################################################################################################################################

st.sidebar.markdown('<p class="font_text">Fig. 3: Matrix plot configuration:</p>', unsafe_allow_html=True)
col1,col2=st.columns(2,gap='small')
pairplot_options_x = col1.multiselect(
    'Select features for x-axis of matrixplot:',
    ['Energy', 'Energy (400-500)','Energy (500-600)', 'Energy (600-700)', 'Energy (700-800)', 'PFD','PFD (400-500)', 'PFD (500-600)', 'PFD (600-700)', 'PFD (700-800)',
    'CO2 ave', 'CO2 std', 'T ave', 'T std', 'RH ave', 'RH std','Photoperiod (h)', 'Day', 'Fresh Mass (g)', 'Dry Mass (g)'])

pairplot_options_y = col2.multiselect(
    'Select features for y-axis of matrixplot:',
    ['Energy', 'Energy (400-500)','Energy (500-600)', 'Energy (600-700)', 'Energy (700-800)', 'PFD','PFD (400-500)', 'PFD (500-600)', 'PFD (600-700)', 'PFD (700-800)',
    'CO2 ave', 'CO2 std', 'T ave', 'T std', 'RH ave', 'RH std','Photoperiod (h)', 'Day', 'Fresh Mass (g)', 'Dry Mass (g)'])
    
pairplot_hue = st.sidebar.select_slider(
    'Select hue for matrixplot:',
    options=['Species', 'Treatment'])


fig1=sns.pairplot(data=Plant_Data,x_vars=pairplot_options_x,y_vars=pairplot_options_y, kind='scatter',hue=pairplot_hue,palette='hsv')

c=alt.Chart(Plant_Data).mark_circle().encode(
    alt.X(alt.repeat("column"), type='quantitative'),
    alt.Y(alt.repeat("row"), type='quantitative'),
    color=pairplot_hue
).properties(
    width=280,
    height=280
).repeat(
    row=pairplot_options_y,
    column=pairplot_options_x
).interactive()

st.altair_chart(c, use_container_width=True)
st.markdown('<p class="font_subtext">Fig. 3: Matrix plot for lettuce growth dataset.</p>', unsafe_allow_html=True)

####################################################################################################################################################################

st.markdown('<p class="font_text">Dry Mass Heatmap based on Red and Blue Wavebands:</p>', unsafe_allow_html=True)
#st.markdown('<p class="font_subsubheader"> Correlation between  </p>', unsafe_allow_html=True)
col5,col6=st.columns(2,gap='small')
heatmap = alt.Chart(Plant_Data).mark_rect().encode(
    alt.X('Energy (600-700):Q', bin=True),
    alt.Y('Dry Mass (g):Q', bin=True),
    alt.Color('count()', scale=alt.Scale(scheme='greenblue'))
).properties(
    height=300,
    width=600
)

points = alt.Chart(Plant_Data).mark_circle(
    color='black',
    size=5,
).encode(
    x='Energy (600-700):Q',
    y='Dry Mass (g):Q',
).properties(
    height=300,
    width=600
)
G=heatmap+points
col5.altair_chart(G, use_container_width=True)

heatmap = alt.Chart(Plant_Data).mark_rect().encode(
    alt.X('Energy (400-500):Q', bin=True),
    alt.Y('Dry Mass (g):Q', bin=True),
    alt.Color('count()', scale=alt.Scale(scheme='greenblue'))
).properties(
    height=300,
    width=600
)

points = alt.Chart(Plant_Data).mark_circle(
    color='black',
    size=5,
).encode(
    x='Energy (400-500):Q',
    y='Dry Mass (g):Q',
).properties(
    height=300,
    width=600
)
H=heatmap+points
col6.altair_chart(H, use_container_width=True)
st.markdown('<p class="font_subtext">Fig. 4: Impact of Red (600-700) and Blue (400-500) Wavebands on lettuce plant growth.</p>', unsafe_allow_html=True)

####################################################################################################################################################################
# st.sidebar.markdown('<p class="font_text">Fig. 5: 2D Scatter Plot:</p>', unsafe_allow_html=True)
# Scatter_X =st.sidebar.selectbox(
#     "Fig. 5: x-axis feature for scatter plot:",
#     ['Energy', 'Energy (400-500)','Energy (500-600)', 'Energy (600-700)', 'Energy (700-800)', 'PFD','PFD (400-500)', 'PFD (500-600)', 'PFD (600-700)', 'PFD (700-800)','CO2 ave', 'CO2 std', 'T ave', 'T std', 'RH ave', 'RH std','Photoperiod (h)', 'Day'])

# Scatter_Y =st.sidebar.selectbox(
#     "Fig. 5: y-axis feature for scatter plot:",
#     ['Energy', 'Energy (400-500)','Energy (500-600)', 'Energy (600-700)', 'Energy (700-800)', 'PFD','PFD (400-500)', 'PFD (500-600)', 'PFD (600-700)', 'PFD (700-800)','CO2 ave', 'CO2 std', 'T ave', 'T std', 'RH ave', 'RH std','Photoperiod (h)', 'Day','Dry Mass (g)','Fresh Mass (g)'])

# fig = px.scatter(Plant_Data, x=Scatter_X, y=Scatter_Y,size="Day", color="Treatment",hover_name="Species", log_x=False, size_max=15)
# fig.show()

# st.plotly_chart(fig, use_container_width=True)
# st.markdown('<p class="font_subtext">Fig. 5: 2D scatter plot for two given features.</p>', unsafe_allow_html=True)

####################################################################################################################################################################
#col7,col8=st.columns(2,gap='small')
st.sidebar.markdown('<p class="font_text">Fig. 5: 3D Scatter Plot:</p>', unsafe_allow_html=True)
Scatter_3D_X =st.sidebar.selectbox(
    "Fig. 5: x-axis feature for 3D scatter plot:",
    ['Energy', 'Energy (400-500)','Energy (500-600)', 'Energy (600-700)', 'Energy (700-800)', 'PFD','PFD (400-500)', 'PFD (500-600)', 'PFD (600-700)', 'PFD (700-800)','CO2 ave', 'CO2 std', 'T ave', 'T std', 'RH ave', 'RH std','Photoperiod (h)', 'Day'])

Scatter_3D_Y =st.sidebar.selectbox(
    "Fig. 5: y-axis feature for 3D scatter plot:",
    ['Energy', 'Energy (400-500)','Energy (500-600)', 'Energy (600-700)', 'Energy (700-800)', 'PFD','PFD (400-500)', 'PFD (500-600)', 'PFD (600-700)', 'PFD (700-800)','CO2 ave', 'CO2 std', 'T ave', 'T std', 'RH ave', 'RH std','Photoperiod (h)', 'Day'])

Scatter_3D_Z =st.sidebar.selectbox(
    "Fig. 5: Z-axis feature for 3D scatter plot:",
    ['Dry Mass (g)', 'Fresh Mass (g)'])

fig=px.scatter_3d(Plant_Data, x=Scatter_3D_X, y=Scatter_3D_Y, z=Scatter_3D_Z,opacity = 0.7,height=600,
    width=1200,color='Treatment')
st.plotly_chart(fig)

####################################################################################################################################################################

st.markdown('<p class="font_header">References: </p>', unsafe_allow_html=True)
st.markdown('Data used for plant growth visualization are obtained from the following refrences:', unsafe_allow_html=False)
st.markdown('1) Meng, Q., Boldt, J., and Runkle, E. S. (2020). Blue radiation interacts with green radiation to influence growth and predominantly controls quality attributes of lettuce. Journal of the American Society for Horticultural Science 145, 75–87280.', unsafe_allow_html=False)
st.markdown('2) Meng, Q., Kelly, N., and Runkle, E. S. (2019). Substituting green or far-red radiation for blue radiation induces shade avoidance and promotes growth in lettuce and kale. Environmental and experimental botany 162, 383–391283.', unsafe_allow_html=False)
st.markdown('3) Meng, Q. and Runkle, E. S. (2019). Far-red radiation interacts with relative and absolute blue and red photon flux densities to regulate growth, morphology, and pigmentation of lettuce and basil seedlings. Scientia Horticulturae 255, 269–280.', unsafe_allow_html=False)
st.markdown('4) Controlled Environment Agriculture Open Data - Lettuce: https://ceaod.github.io/download/#url=GH_Lettuce/LumiGrow.', unsafe_allow_html=True)
