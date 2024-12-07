import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def load_data():
    """
    Load preprocessed data for Benin, Sierra Leone, and Togo.
    Replace with actual data loading script if necessary.
    """
    benin_data = pd.read_csv("../data/benin_cleaned.csv")
    sierra_leone_data = pd.read_csv("../data/sierraleone_cleaned.csv")
    togo_data = pd.read_csv("../data/togo_cleaned.csv")
    return benin_data, sierra_leone_data, togo_data

def generate_histogram(data, metric, region):
    """
    Generate and display a histogram for a specific metric in the given region's dataset.
    """
    fig, ax = plt.subplots()
    ax.hist(data[metric], bins=30, color='blue', edgecolor='black')
    ax.set_xlabel(metric)
    ax.set_ylabel("Frequency")
    ax.set_title(f"{region}: {metric} Histogram")
    st.pyplot(fig)

def generate_bubble_chart(data, metric, region):
    """
    Generate and display a bubble chart for GHI, Tamb, and a specified metric.
    """
    fig, ax = plt.subplots()
    bubble_sizes = data["RH"] / data["RH"].max() * 100
    sc = ax.scatter(data["GHI"], data["Tamb"], c=data[metric], s=bubble_sizes, alpha=0.5, cmap="viridis")
    ax.set_xlabel("GHI")
    ax.set_ylabel("Tamb")
    plt.colorbar(sc, label=metric)
    st.pyplot(fig)

def get_region_data(region, data_map):
    """
    Get the dataset for the selected region from the data map.
    """
    return data_map[region]
