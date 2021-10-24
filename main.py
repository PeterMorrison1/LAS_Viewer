from matplotlib.pyplot import hist
import streamlit as st
import pandas as pd
import numpy as np
import lasio
import summary
import build_a_chart
import plotly.express as px


st.set_page_config(layout="wide", page_title="LAS Viewer")


st.title("LAS Viewer")
st.sidebar.title("LAS Viewer")
st.sidebar.caption("by [PeterMorrison1](github.com/PeterMorrison1)")
st.sidebar.write("This is to test the capabilities of Streamlit and how fast it is to develop a GUI for data science & data engineering.")

st.sidebar.header("Download/Upload")
st.sidebar.download_button("Download LAS File", "test.las")
upload_path = st.sidebar.file_uploader("Upload LAS File")

@st.cache
def load_las_file(path):
    data = lasio.read(path) 
    df = data.df()
    df = df.reset_index()
    return data, df

@st.cache
def load_las_upload(file):
    data = lasio.read(file.read().decode()) 
    df = data.df()
    df = df.reset_index()
    return data, df
    

def load_las_df(df):
    pass


if upload_path:
    data, df = load_las_upload(upload_path)
    st.write(f"Loaded file: {upload_path.name}")
else:
    st.write("Loaded example data")
    data, df = load_las_file("test.las")




st.write(f"Query params: ${st.experimental_get_query_params()}")

with st.expander("Summary"):
    c1, c2 = st.columns(2)
    summary.summary_2_col(data, df, c1, c2)



with st.expander("Build a Custom Chart"):
    build_a_chart.build_a_chart(df)
