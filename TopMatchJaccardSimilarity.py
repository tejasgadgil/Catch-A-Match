import pandas as pd
from itertools import combinations
from sklearn.metrics import jaccard_score

# Load the Excel sheet
file_path = '/content/ModifiedAnswers.xlsx'  # Update with your actual file path
df = pd.read_excel(file_path)

# Extract email ids and answers columns
email_column = df.columns[0]
answers_columns = df.columns[1:]

# Create a dictionary to store email ids and their corresponding answers
data = {email: list(df.loc[df[email_column] == email, answers_columns].values.flatten()) for email in df[email_column]}

# Find the most similar pairs based on Jaccard similarity
max_similarity = 0
most_similar_pair = ()

for pair in combinations(data.keys(), 2):
    similarity = jaccard_score(data[pair[0]], data[pair[1]], average='weighted')  # Specify the 'average' parameter

    if similarity > max_similarity:
        max_similarity = similarity
        most_similar_pair = pair

# Print the most similar pair and their similarity score
print(f"The most similar pair is: {most_similar_pair} with a similarity score of {max_similarity}")


