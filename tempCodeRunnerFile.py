import pandas as pd
import streamlit as st
data = {
    "Zip Code": ["33050", "33040", "33045", "29401", "29577", "32034", "32951", "32940", "33706", "29928"],
    "City": ["Marathon", "Key West", "Islamorada", "Charleston", "Myrtle Beach", "Fernandina Beach", "Melbourne Beach", "Vero Beach", "St. Petersburg", "Hilton Head Island"],
    "State": ["FL", "FL", "FL", "SC", "SC", "FL", "FL", "FL", "FL", "SC"],
    "Number of Hurricane Landfalls (1950-2020)": [14, 13, 12, 11, 10, 9, 9, 8, 8, 7]
}

df = pd.DataFrame(data)
print(df) 
#creating our streamlit prototype
st.title('Hurricane-Prone Zip Codes')
st.write(df)

#use --streamlit run --help in terminal for help
# Add a filter to the app
#also to run this in a web app use command  streamlit run c:\Users\tenni\HavenMap\HavenMap\tempCodeRunnerFile.py for trinity
#whitnie this would be different for u
st.write('Filter by State:')
state_filter = st.selectbox('Select a state', ['FL', 'SC', 'NC'])
st.write('Filtered data:')
filtered_df = df[df['State'] == state_filter]
st.write(filtered_df)
