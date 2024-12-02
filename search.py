import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load the event data
file_path = '2_tapahtumat_agrihubi.xlsx'
event_data = pd.read_excel(file_path, engine='openpyxl')

# Combine relevant columns for analysis and search functionality
event_data['combined_themes'] = event_data['Aiheet'].fillna('') + ' ' + event_data['Avainsanat'].fillna('')

# CAP goals for analysis
cap_goals = ['sustainability', 'rural development', 'innovation']

# Streamlit App
st.title("CAP Plan Event Analysis Dashboard")

# Section 1: Detailed Analysis of Event Alignment with CAP Goals
st.header("1. Event Alignment with CAP Goals")
cap_analysis = {goal: event_data['combined_themes'].str.contains(goal, case=False, na=False).sum() for goal in cap_goals}
cap_df = pd.DataFrame(list(cap_analysis.items()), columns=['CAP Goal', 'Matching Events'])

st.write("### CAP Plan Alignment Summary")
st.table(cap_df)

# Visualization of CAP alignment
st.write("### CAP Alignment Visualization")
fig, ax = plt.subplots()
ax.bar(cap_analysis.keys(), cap_analysis.values(), color='skyblue')
ax.set_title("Number of Events Matching CAP Goals")
ax.set_xlabel("CAP Goals")
ax.set_ylabel("Number of Events")
st.pyplot(fig)

# Section 2: Event Distribution and Future Needs
st.header("2. Event Distribution and Future Needs")
# Distribution of events by themes
theme_counts = Counter(' '.join(event_data['Aiheet'].fillna('')).lower().split())
theme_df = pd.DataFrame(theme_counts.most_common(10), columns=['Theme', 'Frequency'])

st.write("### Top 10 Themes in Events")
st.bar_chart(theme_df.set_index('Theme'))

# Recommendations for future needs
st.write("### Recommendations for Future Events")
underrepresented_goals = [goal for goal, count in cap_analysis.items() if count < 5]
if underrepresented_goals:
    st.write("The following CAP goals are underrepresented in events:")
    for goal in underrepresented_goals:
        st.write(f"- {goal}")
else:
    st.write("All CAP goals are well-represented in the event data.")

# Section 3: Search Functionality
st.header("3. Search Event Data")
query = st.text_input("Search events by keyword:")
if query:
    query_lower = query.lower()
    filtered_data = event_data[event_data['combined_themes'].str.contains(query_lower, case=False, na=False)]

    if not filtered_data.empty:
        st.write(f"### Results for '{query}':")
        st.dataframe(filtered_data[['Aiheet', 'Avainsanat', 'combined_themes']])
    else:
        st.write(f"No results found for '{query}'.")
