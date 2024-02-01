import streamlit as st
import pandas as pd


# Page set up
st.set_page_config(layout='wide')
st.header("Street Cleaning Schedule")

# Connect to the Google Sheet
schedule_sheet_id = "15EwPbF3c6OgMi62OXyZrEjYLymwj2e3vYmaGK6ldElg"
schedule_sheet_name = "schedule"
address_sheet_id = "18Zp37WJtFYBnQNz9DqGZ59vz9OVQtft17rDhJPWIdHY"
address_sheet_name = "address"
schedule_url = f"https://docs.google.com/spreadsheets/d/{schedule_sheet_id}/gviz/tq?tqx=out:csv&sheet={schedule_sheet_name}"
address_url = f"https://docs.google.com/spreadsheets/d/{address_sheet_id}/gviz/tq?tqx=out:csv&sheet={address_sheet_name}"

schedule = pd.read_csv(schedule_url, dtype=str).fillna("")
schedule = schedule[['CNN','Corridor','Limits','CNNRightLeft','BlockSide','FullName','WeekDay','FromHour','ToHour','BlockSweepID']]
address = pd.read_csv(address_url, dtype=str).fillna("")
address = address[['Address', 'Address Number','Street Name',
                   'Street Type','ZIP Code', 'CNN']]
# Show the dataframe
df = pd.merge(address, schedule, on='CNN', how='inner')
st.write(df)


# get the keywords to filter the dataframe
text_search = st.text_input("Enter your address", value="")
street = df['Address'].str.lower().str.contains(text_search.lower())
df_search = df[street]
print(df_search)
result = f"""Next street cleaning is 
on {df_search['WeekDay'][0]} from {df_search['FromHour'][0]} AM to {df_search['ToHour'][0]} AM."""
# Show the results
if text_search:
    st.write(result)

