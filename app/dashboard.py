import streamlit as st
import utils  # Importing the refactored utility functions

# Load data dynamically
benin_data, sierra_leone_data, togo_data = utils.load_data()

# Data mapping
data_map = {
    "Benin": benin_data,
    "Sierra Leone": sierra_leone_data,
    "Togo": togo_data
}

# Dashboard Title
st.title("Energy Data Dashboard")

# Sidebar for navigation
st.sidebar.header("Navigation")
region = st.sidebar.selectbox("Select Region", ["Benin", "Sierra Leone", "Togo"])
metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI", "Tamb", "TModA", "TModB", "WS"])
visualization = st.sidebar.selectbox("Select Visualization", ["Line Chart", "Histogram", "Bubble Chart"])

# Get the data for the selected region
data = utils.get_region_data(region, data_map)

# Visualizations
if visualization == "Line Chart":
    st.subheader(f"{region}: {metric} Over Time")
    st.line_chart(data[["Timestamp", metric]].set_index("Timestamp"))
elif visualization == "Histogram":
    st.subheader(f"{region}: {metric} Distribution")
    utils.generate_histogram(data, metric, region)
elif visualization == "Bubble Chart":
    st.subheader(f"{region}: GHI vs. Tamb vs. {metric} (Bubble Size = RH)")
    utils.generate_bubble_chart(data, metric, region)

# Add interactivity
st.sidebar.header("Customize View")
show_raw_data = st.sidebar.checkbox("Show Raw Data")

if show_raw_data:
    st.subheader(f"{region}: Raw Data")
    st.dataframe(data)

# Deploy Information
st.sidebar.markdown("---")
st.sidebar.markdown("Developed by [Abenezer Eshetie](https://github.com/EbenGitHub/10-academy-week-0)")
