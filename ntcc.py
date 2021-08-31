import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

@st.cache
def load_data():
    return pd.read_csv('data/GlobalTemperatures.csv', parse_dates=['dt'])

df = load_data()
yrwise = df.copy()
yrwise['date'] = pd.to_datetime(yrwise.dt)
yrwise['month'] = yrwise.date.dt.month_name() + yrwise.date.dt.year.agg(lambda x:' '+str(x))
yrwise['year'] = yrwise.date.dt.year
yrwise['century'] = yrwise.year.agg(lambda x:str((x//100)+1)+'th')

def home(title):
    st.title("Introduction")
    st.write('In our ever-changing world, mankind’s influence towards mother nature has been a grave issue, with the rise in global warming and other factors affecting our globe, human activities including industrial production, burning fossil fuel, mining, cattle rearing or deforestation have been gradually increasing. There is a dire need for harmony among humans and the environment to preserve our planet’s natural order. The climate change is highly complex phenomenon and we can only understand it as much as our computational resources allow us to. Different elements such as temperature, wind, atmospheric pressure, humidity, rain, etc. are observed over a period of time to describe how climate change is in effect.')
    st.write('Variant needs of humans have always propelled them to exploit the nature and natural resources without realizing the ever lasting effect it has caused to the planet. The primary purpose of this project is to visualize the inter dependence between the factors chosen to analyze the climate change. Enormous amounts of studies have been published in the recent years by both organizations and individuals on how climate change has affected our planet. This project builds upon various studies(which have been properly cited) that have been produced to study the climate change on our planet. The challenges and problems encountered during the project will be clearly discussed at the end of the report. We will also discuss some of the relevant techniques that could not be incorporated into the final visualizations.')
    st.write('The temperature change plays a very crucial role in the climate change profile of the planet. It determines the entire heat profile of the planet. Given the enormous size of Earth’s ocean and their extremely high heat capacity, it takes a tremendous amount of heat energy to raise the surface temperature of the Earth. According to the studies conducted by the National Oceanic and Atmospheric Administration(NOAA), the surface temperature of Earth rose by 2 degrees since the pre-industrial era . This amount may seem really small at first sight but at the scale of our planet, it is a significant number. Record high land temperatures were recorder in several parts of the world in the recent years. These alarmingly high  temperature anomalies trigger a chain of reactions that drive various other factors affecting the climate change like melting of polar ice caps, rise in the global sea level, etc. Therefore analyzing temperature change is not only crucial, but also the  need of the hour.')
    st.write('The Arctic ice cover has been melting at an alarmingly fast rate throughout the recent decades. The Arctic Ice reaches its annual minimum value in the month of September. This period is known as the Arctic Ice minimum. In the year 2020, Arctic ice minimum has hit its second lowest value in its entire history. Researchers have produced various simulations to study how the Arctic ice cover has been depleted over the recent years. The visualization of the arctic sea cover helps us in understanding the patterns in climate change over the years better.')
    st.image('impact.jpg',caption = "Social and Economic Impact of Climate Change",)
    st.write('Above image shows the impacts of the climate change. It is clear by the image how the world would suffer in future because of the climate change.')
    st.write('While the temperature change in itself is a major contributor towards climate change, as mentioned earlier, it also  triggers the increase in the sea level globally. The major contributor in the annual sea level increase is the global warming. The decline in liquid water on land is also considered as the minor contributor towards the sea level change. This hap- pens when the water on the land moves to the oceans through groundwater pumping . According to the study conducted by NOAA , the mean level of water in the oceans globally has increased by 0.14 inches (3.6 millimeters) per year be- tween the years 2006 and 2015. What’s concerning is that this amount is roughly 2.5 times the average rate of increase per year throughout the 20th century. Future projection models show that by the end of the century, the average sea level globally will rise at least 0.3 meters above 2000 levels and that too provided the emissions from greenhouse gases remain in the low part of the spectrum in coming decades.')

def page1(title):
    st.title(title)
    if st.sidebar.checkbox("show raw data?"):
        x = st.sidebar.slider('Choose rows to display..', min_value=0,max_value=df.shape[0],value=10)
        st.write(df.head(x))
    st.header("Summary of Dataset")
    st.write(df.describe())
    st.markdown("<hr>", unsafe_allow_html=True)
    cols = st.beta_columns(2)
    cols[0].subheader("Rows of Dataset")
    cols[0].write(df.shape[0])
    cols[1].subheader("Columns of Dataset")
    cols[1].write(df.shape[1])
    st.markdown("<hr>", unsafe_allow_html=True)
    for i in df.columns:
        st.subheader(i)
        divs = st.beta_columns(2)
        divs[0].write(f"Data Type: {type(df[i].iloc[0])}")
        divs[1].write(f"Null Values: {sum(df[i].isna())}")
        st.markdown("<hr>", unsafe_allow_html=True)

def page2(title):
    data = yrwise.copy()
    data = data.groupby('year', as_index=False).agg({
    'LandAverageTemperature': np.mean,
    'LandMaxTemperature':max,
    'LandMinTemperature':min,
    'LandAndOceanAverageTemperature':np.mean}).reset_index()
    st.title(title)
    st.header("Average Temperature of Land throughout the years")
    st.plotly_chart(px.line(data, 'year', 'LandAverageTemperature'))
    data = data.dropna()
    st.header("Maximum Temperature of Land throughout the years")
    st.plotly_chart(px.line(data, 'year', 'LandMaxTemperature'))
    st.header("Minimum Temperature of Land throughout the years")
    st.plotly_chart(px.line(data, 'year', 'LandMinTemperature'))
    st.header("Average Temperature of Land and Ocean throughout the years")
    st.plotly_chart(px.line(data, 'year', 'LandAndOceanAverageTemperature'))

def page3(title):
    data = yrwise.copy()
    data = data.groupby('century', as_index=False).agg({
    'LandAverageTemperature': np.mean,
    'LandMaxTemperature':max,
    'LandMinTemperature':min,
    'LandAndOceanAverageTemperature':np.mean}).reset_index()
    st.title(title)
    st.header("Average Temperature of Land throughout the Centuries")
    st.plotly_chart(px.bar(data, 'century', 'LandAverageTemperature'))
    data = data.dropna()
    st.header("Maximum Temperature of Land throughout the Centuries")
    st.plotly_chart(px.bar(data, 'century', 'LandMaxTemperature'))
    st.header("Minimum Temperature of Land throughout the Centuries")
    st.plotly_chart(px.bar(data, 'century', 'LandMinTemperature'))
    st.header("Average Temperature of Land and Ocean throughout the Centuries")
    st.plotly_chart(px.bar(data, 'century', 'LandAndOceanAverageTemperature'))

def page4(title):
    st.title(title)
    data = yrwise.copy()
    data = data.dropna()
    st.subheader("Hottest Day in Recorded Data")
    st.write(data[data.LandMaxTemperature == max(data.LandMaxTemperature)].date.iloc[0])
    st.subheader("Coldest Day in Recorded Data")
    st.write(data[data.LandMinTemperature == min(data.LandMinTemperature)].date.iloc[0])
    month_data = data.groupby('month', as_index=False).agg({'LandMaxTemperature':max,'LandMinTemperature':min})
    st.subheader("Hottest Month in Recorded Data")
    st.write(month_data[month_data.LandMaxTemperature == max(month_data.LandMaxTemperature)].month.iloc[0])
    st.subheader("Coldest Month in Recorded Data")
    st.write(month_data[month_data.LandMinTemperature == min(month_data.LandMinTemperature)].month.iloc[0])
    year_data = data.groupby('year', as_index=False).agg({'LandMaxTemperature':max,'LandMinTemperature':min})
    st.subheader("Hottest Year in Recorded Data")
    st.write(year_data[year_data.LandMaxTemperature == max(year_data.LandMaxTemperature)].year.iloc[0])
    st.subheader("Coldest Year in Recorded Data")
    st.write(year_data[year_data.LandMinTemperature == min(year_data.LandMinTemperature)].year.iloc[0])
    st.subheader("Hottest Century in Recorded Data")
    century_data = data.groupby('century', as_index=False).agg({'LandMaxTemperature':max,'LandMinTemperature':min})
    st.write(century_data[century_data.LandMaxTemperature == max(century_data.LandMaxTemperature)].century.iloc[0])
    st.subheader("Coldest Century in Recorded Data")
    st.write(century_data[century_data.LandMinTemperature == min(century_data.LandMinTemperature)].century.iloc[0])

pages = {
    "Introduction": home,
    "Information About Data": page1,
    "Climate Changes by Years": page2,
    "Climate Changes by Centuries": page3,
    "General Observations": page4
    }

page = st.sidebar.selectbox('Choose a page...',list(pages.keys()))
pages[page](page)