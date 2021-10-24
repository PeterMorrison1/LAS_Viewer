import streamlit as st
import plotly.express as px


def build_a_chart(df):
    st.header("Build your simple chart")
    # chart_types = ["scatter", "bar", "line", "area", "pie", "histogram", "violin", "heatmap"]
    chart_types = ["line", "histogram"]
    chart_type = st.selectbox("Choose your chart type", chart_types)

    st.write("Note that at least one x or y *must* have only one variable selected*")
    chart_c1, chart_c2 = st.columns(2)
    with chart_c1:
        x = st.multiselect("Choose your X-Axis", df.columns)
        x_multi = st.checkbox("Multiple x Variables Selected?")
        if not x_multi and x:
            x = x[0]
            
    with chart_c2:
        y = st.multiselect("Choose your Y-Axis", df.columns)
        y_multi = st.checkbox("Multiple y Variables Selected?")
        if not y_multi and y:
            y = y[0]
            


    if x_multi and y_multi:
        st.error("At least one axis must be a single value only.")

    if x and y:
        title = f"User Plot: {x} as x and {y} as y"
        if chart_type == 'line':
            fig = px.line(df, x=x, y=y, title=title)
            
        elif chart_type == 'histogram':
            fig = px.histogram(df, x=x, y=y, title=title)
        
        st.plotly_chart(fig, use_container_width=True)