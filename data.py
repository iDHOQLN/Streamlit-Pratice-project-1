import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.sidebar.title("Navigation")

df = pd.read_csv("F:/DataSet/iris.csv")
name = st.sidebar.text_input("Enter Your Name")
the_section = st.sidebar.selectbox("Select The Section", ["Homepage","Dataset","Statistical Analysis", "Data Visualization"])

if the_section == "Homepage":
    st.header("Data Analysis on iris dataset")
    st.write(f"Hello {name}")
    st.subheader("Select Section")

if the_section == "Dataset":
    st.write(df.head())

if the_section == "Statistical Analysis":
    st.subheader("Statistical Analysis")
    st.write(df.describe())

if the_section == "Data Visualization":
    visualization = st.subheader("Data Visualization")

    st.write("Swarmplot - Sepal Length")
    fig1, ax1 = plt.subplots()
    sns.swarmplot(data=df, x='species', y='sepal_length', ax=ax1)
    st.pyplot(fig1)

    st.write("Swarmplot - Sepal Width")
    fig2, ax2 = plt.subplots()
    sns.swarmplot(data=df, x='species', y='sepal_width', ax=ax2)
    st.pyplot(fig2)

    st.write("Swarmplot - Petal Length")
    fig3, ax3 = plt.subplots()
    sns.swarmplot(data=df, x='species', y='petal_length', ax=ax3)
    st.pyplot(fig3)

    st.write("Swarmplot - Petal Width")
    fig4, ax4 = plt.subplots()
    sns.swarmplot(data=df, x='species', y='petal_width', ax=ax4)
    st.pyplot(fig4)

    st.write("Countplot - Species")
    fig5, ax5 = plt.subplots()
    sns.countplot(data=df, x='species')
    st.pyplot(fig5)


