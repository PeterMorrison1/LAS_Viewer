import streamlit as st

def summary_2_col(data, df, c1, c2):
    with c1:
        st.subheader("File Info")
        for section in data.sections:
            st.text(section)
            st.text(data.sections[section])


    # df['depth'] = df.index
    with c2:
        st.subheader("Raw data")
        st.write(df)

        st.text("Raw Data Summary")
        st.write(df.describe())