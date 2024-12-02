import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from itertools import combinations
import pdfplumber

# Step 1: Extract Insights from CAP Plan
def extract_cap_goals(pdf_path):
    cap_keywords = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if "sustainability" in text.lower():
                cap_keywords.append("sustainability")
            if "rural development" in text.lower():
                cap_keywords.append("rural development")
            if "innovation" in text.lower():
                cap_keywords.append("innovation")
    return list(set(cap_keywords))

# Load CAP goals
cap_file = '2_Suomen_CAP-suunnitelma.pdf'
cap_goals = extract_cap_goals(cap_file)
print("CAP Goals:", cap_goals)

# Step 2: Load Event Data
event_file = '2_tapahtumat_agrihubi.xlsx'
event_data = pd.read_excel(event_file, engine='openpyxl')

# Combine relevant columns for analysis
event_data['combined_themes'] = event_data['Aiheet'].fillna('') + ' ' + event_data['Avainsanat'].fillna('')

# Tokenize and count keyword frequencies
all_keywords = ' '.join(event_data['combined_themes']).lower().split()
theme_counts = Counter(all_keywords)

# Step 3: Refine Keywords for Analysis
keywords_to_analyze = ['maatalous', 'maaseudun', 'ilmasto', 'koulutus', 'tilaisuus', 'ohjelma', 'järjestetään', 'ilmoittaudu']
refined_counts = {key: theme_counts.get(key, 0) for key in keywords_to_analyze}

# Visualize Refined Keyword Analysis
plt.bar(refined_counts.keys(), refined_counts.values())
plt.title("Refined Keyword Analysis")
plt.xlabel("Keywords")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()

# Step 4: Co-occurrence Analysis
event_data['keywords'] = event_data['combined_themes'].apply(lambda x: [word for word in x.lower().split() if word in keywords_to_analyze])

co_occurrence = {}
for keywords in event_data['keywords']:
    for pair in combinations(set(keywords), 2):  # Unique combinations of 2
        co_occurrence[pair] = co_occurrence.get(pair, 0) + 1

# Display Top Co-occurrences
sorted_co_occurrences = sorted(co_occurrence.items(), key=lambda x: x[1], reverse=True)
print("Top Keyword Co-occurrences:", sorted_co_occurrences[:10])

# Visualize Co-occurrences
cooccurrence_df = pd.DataFrame(sorted_co_occurrences[:10], columns=['Keyword Pair', 'Frequency'])
cooccurrence_df.plot.barh(x='Keyword Pair', y='Frequency', legend=False)
plt.title("Top Keyword Co-occurrences")
plt.xlabel("Frequency")
plt.ylabel("Keyword Pairs")
plt.gca().invert_yaxis()
plt.show()

# Step 5: Match Themes to CAP Goals and Recommend Topics
cap_goal_matches = {goal: sum(refined_counts.get(word, 0) for word in keywords_to_analyze if goal in word) for goal in cap_goals}

# Display Recommendations
print("CAP Goal Matches:", cap_goal_matches)

underrepresented_themes = [goal for goal, count in cap_goal_matches.items() if count < 5]
print("Recommended Topics for Future Events:", underrepresented_themes)