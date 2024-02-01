import streamlit as st
import pandas as pd


# Page set up
st.set_page_config(layout='wide')
st.header("Street Cleaning Schedule")

# Connect to the Google Sheet
sheet_id = "15EwPbF3c6OgMi62OXyZrEjYLymwj2e3vYmaGK6ldElg"
sheet_name = "schedule"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url, dtype=str).fillna("")

# Show the dataframe
st.write(df)

# get the keywords to filter the dataframe
text_search = st.text_input("Enter your address", value="")
street = df['Limits'].str.match(text_search)
corridor = df['Corridor'].str.match(text_search)
df_search = df[street | corridor]
result = f"Next street cleaning is on {df_search['WeekDay']}"
st.write(df_search["WeekDay"])
# Show the results
if text_search:
    st.write(result)