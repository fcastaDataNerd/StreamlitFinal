import streamlit as st

# Title of the app
st.title("ROS Playoff Scenarios")

st.header("Greeting, gentlemen. Explore your tanking scenarios below (except for FS)")

import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
# Load data and historical scores
scores = pd.read_excel("C:\\Users\\Franco Castagliuolo\\OneDrive - Bentley University\\DataMining\\Fantasy.xlsx", sheet_name="ScoringData")
records = pd.read_excel("C:\\Users\\Franco Castagliuolo\\OneDrive - Bentley University\\DataMining\\Fantasy.xlsx", sheet_name="Records")
schedule = pd.read_excel("C:\\Users\\Franco Castagliuolo\\OneDrive - Bentley University\\DataMining\\Fantasy.xlsx", sheet_name="Schedule")
playoffs = pd.read_excel("C:\\Users\\Franco Castagliuolo\\OneDrive - Bentley University\\DataMining\\Fantasy.xlsx", sheet_name="Playoffs")

st.subheader("Week 12")
