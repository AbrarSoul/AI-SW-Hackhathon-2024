import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load the event data from Excel
file_path = '2_tapahtumat_agrihubi.xlsx'  # Adjust the file path as needed
event_data = pd.read_excel(file_path)

# Ensure required columns exist
required_columns = ['Tiivistelmä', 'Sisältö', 'Avainsanat']
for column in required_columns:
    if column not in event_data.columns:
        print(f"Column {column} is missing.")
        exit()

# Combine text columns for analysis
event_data['combined_text'] = (
    event_data['Tiivistelmä'].fillna('') + ' ' +
    event_data['Sisältö'].fillna('') + ' ' +
    event_data['Avainsanat'].fillna('')
)

# Tokenize and clean text
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('finnish'))  # Adjust for the dataset language

all_words = []
for text in event_data['combined_text']:
    tokens = word_tokenize(str(text).lower())
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    all_words.extend(filtered_tokens)

# Analyze keyword frequencies
word_freq = Counter(all_words)
top_keywords = word_freq.most_common(20)

# Display top keywords
print("Top Keywords and Their Frequencies:")
for keyword, freq in top_keywords:
    print(f"{keyword}: {freq}")

# Visualization
keywords, frequencies = zip(*top_keywords)
plt.figure(figsize=(10, 6))
plt.barh(keywords, frequencies)
plt.xlabel('Frequency')
plt.ylabel('Keywords')
plt.title('Top Keywords in Event Data')
plt.gca().invert_yaxis()
plt.show()