import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import hiplot as hip
import altair as alt
import plotly.figure_factory as ff
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
col1,col2=st.columns(2,gap='small')
light_stat = col1.checkbox('Show statistical properties of Light Treatments')
if light_stat==True:
    st.table(Light_Treatments.describe())
    st.markdown('<p class="font_subtext">Table 1: Statistical properties of various light treatment.</p>', unsafe_allow_html=True)

light_show = col2.checkbox('Show Light Treatments Data')
if light_show==True:
    st.table(Light_Treatments)
    st.markdown('<p class="font_subtext">Table 2: Light treatment information including energy, photon density, and wavelength.</p>', unsafe_allow_html=True)

####################################################################################################################################################################

st.sidebar.markdown('<p class="font_text">Fig. 1: Spectral Visualization:</p>', unsafe_allow_html=True)

Light_Treatment_Name = st.sidebar.selectbox(
    "Fig. 1: Light Treatment:",
    ['B30R150' , 'B30R150FR30' , 'R180FR30' , 'B90R90' , 'B90R90FR30' , 'B180FR30' , 'B90R90FR75' , 'B180R180' , 'B180R180FR30' , 'B180R180FR75' , 'B60R120' , 'B40G20R120' , 'B20G40R120' , 'G60R120' , 'B40R120FR20' , 'B20R120FR40' , 'R120FR60' , 'B20G20R120FR20' , 'R180' , 'B20R160' , 'B20G60R100' , 'B60G60R60' , 'B100R80' , 'B100G60R20' , 'EQW180' , 'EQW100B10R70' , 'EQW100B50R30' , 'WW180' , 'Greenhouse'])

col1,col3,col2=st.columns([5,1,5],gap='small')
x_min = col1.number_input('Insert a minimum value for x-axis')
x_max = col2.number_input('Insert a maximum value for x-axis')
    
if Light_Treatment_Name != "Greenhouse":
    Figure=plt.figure(figsize=(12,2))
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
    plt.xlim(x_min,x_max)
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
    # plt.xticks(ticks=[400,500,600,700,800])
    plt.xlim(x_min,x_max)
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
    # plt.xticks(ticks=[400,500,600,700,800])
    plt.xlim(x_min,x_max)
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
    # plt.xticks(ticks=[400,500,600,700,800])
    plt.xlim(x_min,x_max)
    plt.grid(which='both',axis='both',color='grey', linestyle='--', linewidth=.3)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Spectral Energy')
st.pyplot(Figure)
st.markdown('<p class="font_subtext">Fig. 1: Photon and energy distribution for various investigated light treatment.</p>', unsafe_allow_html=True)

####################################################################################################################################################################

st.markdown('<p class="font_subheader">Plant Data: </p>', unsafe_allow_html=True)

Plant_Data=pd.read_csv("Project Data.csv")

col1,col2,col3=st.columns(3,gap='small')
lettuce_stat = col1.checkbox('Show statistical properties of Lettuce dataset')

if lettuce_stat==True:
    st.table(Plant_Data.describe())
    st.markdown('<p class="font_subtext">Table 3: Statistical properties of lettuce cultivated under different light treatment and environmental conidtions.</p>', unsafe_allow_html=True)

lettuce_show = col2.checkbox('Show Lettuce dataset')

if lettuce_show==True:
    st.table(Plant_Data)
    st.markdown('<p class="font_subtext">Table 4: Experimental observations for lettuce cultivated under different light treatments and various environmental conidtions.</p>', unsafe_allow_html=True)


lettuce_hip = col3.checkbox('Show Lettuce hiplot')

if lettuce_hip==True:
    xp = hip.Experiment.from_dataframe(Plant_Data)
    ret_val = xp.to_streamlit(ret="selected_uids", key="hip").display()
    st.markdown('<p class="font_subtext">Fig. 2: Hiplot for lettuce data.</p>', unsafe_allow_html=True)


####################################################################################################################################################################

col3,col4=st.columns(2,gap='small')

source = pd.DataFrame({"category": ['Rouxai','Rex','Cherokee'], "value": [Plant_Data.loc[Plant_Data["Species"]=="Rouxai"].shape[0],
                                                Plant_Data.loc[Plant_Data["Species"]=="Rex"].shape[0],
                                                Plant_Data.loc[Plant_Data["Species"]=="Cherokee"].shape[0]]})

d=alt.Chart(source).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="category", type="nominal",scale=alt.Scale(scheme='rainbow')),
    tooltip=("category","value")
).interactive()

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
    color=alt.Color(field="category", type="nominal",scale=alt.Scale(scheme='rainbow')),
    tooltip=("category","value")
).interactive()

col4.altair_chart(g, use_container_width=True)

st.markdown('<p class="font_subtext">Fig. 3: Categorical distribution of experimental observations.</p>', unsafe_allow_html=True)

####################################################################################################################################################################

st.sidebar.markdown('<p class="font_text">Fig. 4: Matrix plot configuration:</p>', unsafe_allow_html=True)
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
    color=pairplot_hue,
    tooltip=['Dry Mass (g)', 'Photoperiod (h)', 'RH ave', 'CO2 ave']
).properties(
    width=280,
    height=280
).repeat(
    row=pairplot_options_y,
    column=pairplot_options_x
).interactive()

st.altair_chart(c, use_container_width=True)
st.markdown('<p class="font_subtext">Fig. 4: Matrix plot for lettuce growth dataset.</p>', unsafe_allow_html=True)

####################################################################################################################################################################

# st.markdown('<p class="font_text">Dry Mass Heatmap based on Red and Blue Wavebands:</p>', unsafe_allow_html=True)
#st.markdown('<p class="font_subsubheader"> Correlation between  </p>', unsafe_allow_html=True)
tab1, tab2 = st.tabs(["Heatmap", "Jointplot"])
with tab1:
    option1 = st.selectbox(
        'Studied feature 1:',
        ('Energy', 'Energy (400-500)','Energy (500-600)', 'Energy (600-700)', 'Energy (700-800)', 'PFD','PFD (400-500)', 'PFD (500-600)', 'PFD (600-700)', 'PFD (700-800)',
        'CO2 ave', 'CO2 std', 'T ave', 'T std', 'RH ave', 'RH std','Photoperiod (h)', 'Day'))
    option3 = st.selectbox(
        'Studied feature 2:',
        ('Energy', 'Energy (400-500)','Energy (500-600)', 'Energy (600-700)', 'Energy (700-800)', 'PFD','PFD (400-500)', 'PFD (500-600)', 'PFD (600-700)', 'PFD (700-800)',
        'CO2 ave', 'CO2 std', 'T ave', 'T std', 'RH ave', 'RH std','Photoperiod (h)', 'Day'))
    option2 = st.selectbox('Dry Mass or Fresh Mass',('Dry Mass (g)', 'Fresh Mass (g)'))
    col1, col2=st.columns(2,gap='small')
    heatmap = alt.Chart(Plant_Data).mark_rect().encode(
        alt.X(option1+':Q', bin=True),
        alt.Y(option2+':Q', bin=True),
        alt.Color('count()', scale=alt.Scale(scheme='greenblue'))
    ).properties(
        height=500,
        width=700
    )
    points = alt.Chart(Plant_Data).mark_circle(
        color='black',
        size=5,
    ).encode(
        x=option1+':Q',
        y=option2+':Q',
    ).properties(
        height=500,
        width=700
    )
    G=heatmap+points
    col1.altair_chart(G, use_container_width=True)
    heatmap = alt.Chart(Plant_Data).mark_rect().encode(
        alt.X(option3+':Q', bin=True),
        alt.Y(option2+':Q', bin=True),
        alt.Color('count()', scale=alt.Scale(scheme='greenblue'))
    ).properties(
        height=500,
        width=700
    )
    points = alt.Chart(Plant_Data).mark_circle(
        color='black',
        size=5,
    ).encode(
        x=option3+':Q',
        y=option2+':Q',
    ).properties(
        height=500,
        width=700
    )
    G=heatmap+points
    col2.altair_chart(G, use_container_width=True)
    st.markdown('<p class="font_subtext">Fig. 5: Heatmap of lettuce mass with respect to a feature.</p>', unsafe_allow_html=True)

with tab2:
    option3 = st.selectbox(
        'Feature 1',
        ('Energy', 'Energy (400-500)','Energy (500-600)', 'Energy (600-700)', 'Energy (700-800)', 'PFD','PFD (400-500)', 'PFD (500-600)', 'PFD (600-700)', 'PFD (700-800)',
        'CO2 ave', 'CO2 std', 'T ave', 'T std', 'RH ave', 'RH std','Photoperiod (h)', 'Day'))

    option4 = st.selectbox(
        'Feature 2',
        ('Energy', 'Energy (400-500)','Energy (500-600)', 'Energy (600-700)', 'Energy (700-800)', 'PFD','PFD (400-500)', 'PFD (500-600)', 'PFD (600-700)', 'PFD (700-800)',
        'CO2 ave', 'CO2 std', 'T ave', 'T std', 'RH ave', 'RH std','Photoperiod (h)', 'Day'))

    option5 = st.selectbox(
        'Color map:',
        ('mako','viridis','rocket','Spectral','coolwarm','cubehelix','dark:salmon_r'))

    option6 = st.slider('Number of contour level:', 0, 200, 20)

    sns.set_theme(style="white")
    fig = sns.JointGrid(data=Plant_Data, x=option3, y=option4, space=0)
    fig.plot_joint(sns.kdeplot,
                 fill=True,
                 thresh=0, levels=option6, cmap=option5)
    fig.plot_marginals(sns.histplot, color="blue", alpha=1, bins=30)
    plt.show()
    st.pyplot(fig)
    st.markdown('<p class="font_subtext">Fig. 5: Jointplot for two of the investigated features.</p>', unsafe_allow_html=True)

####################################################################################################################################################################
#col7,col8=st.columns(2,gap='small')
st.sidebar.markdown('<p class="font_text">Fig. 6: 3D Scatter Plot:</p>', unsafe_allow_html=True)
Scatter_3D_X =st.sidebar.selectbox(
    "Fig.6: x-axis feature for 3D scatter plot:",
    ['Energy', 'Energy (400-500)','Energy (500-600)', 'Energy (600-700)', 'Energy (700-800)', 'PFD','PFD (400-500)', 'PFD (500-600)', 'PFD (600-700)', 'PFD (700-800)','CO2 ave', 'CO2 std', 'T ave', 'T std', 'RH ave', 'RH std','Photoperiod (h)', 'Day'])

Scatter_3D_Y =st.sidebar.selectbox(
    "Fig. 6: y-axis feature for 3D scatter plot:",
    ['Energy', 'Energy (400-500)','Energy (500-600)', 'Energy (600-700)', 'Energy (700-800)', 'PFD','PFD (400-500)', 'PFD (500-600)', 'PFD (600-700)', 'PFD (700-800)','CO2 ave', 'CO2 std', 'T ave', 'T std', 'RH ave', 'RH std','Photoperiod (h)', 'Day'])

Scatter_3D_Z =st.sidebar.selectbox(
    "Fig.6: Z-axis feature for 3D scatter plot:",
    ['Dry Mass (g)', 'Fresh Mass (g)'])
Scatter_3D_hue =st.sidebar.selectbox(
    "Fig. 6: Hue for 3D scatter plot:",
    ['Species', 'Treatment'])

fig=px.scatter_3d(Plant_Data, x=Scatter_3D_X, y=Scatter_3D_Y, z=Scatter_3D_Z,opacity = 0.7,height=600,
    width=1200,color=Scatter_3D_hue)
st.plotly_chart(fig)
st.markdown('<p class="font_subtext">Fig. 6: 3D scatter plot of lettuce mass versus other features.</p>', unsafe_allow_html=True)

####################################################################################################################################################################

st.markdown('<p class="font_header">References: </p>', unsafe_allow_html=True)
st.markdown('Data used for plant growth visualization are obtained from the following refrences:', unsafe_allow_html=False)
st.markdown('1) Meng, Q., Boldt, J., and Runkle, E. S. (2020). Blue radiation interacts with green radiation to influence growth and predominantly controls quality attributes of lettuce. Journal of the American Society for Horticultural Science 145, 75–87280.', unsafe_allow_html=False)
st.markdown('2) Meng, Q., Kelly, N., and Runkle, E. S. (2019). Substituting green or far-red radiation for blue radiation induces shade avoidance and promotes growth in lettuce and kale. Environmental and experimental botany 162, 383–391283.', unsafe_allow_html=False)
st.markdown('3) Meng, Q. and Runkle, E. S. (2019). Far-red radiation interacts with relative and absolute blue and red photon flux densities to regulate growth, morphology, and pigmentation of lettuce and basil seedlings. Scientia Horticulturae 255, 269–280.', unsafe_allow_html=False)
st.markdown('4) Controlled Environment Agriculture Open Data - Lettuce: https://ceaod.github.io/download/#url=GH_Lettuce/LumiGrow.', unsafe_allow_html=True)
