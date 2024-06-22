import pandas as pd
from itertools import combinations
from sklearn.metrics import jaccard_score
from prettytable import PrettyTable

# Load the Excel sheet
file_path = '/content/ModifiedAnswers.xlsx'  # Update with your actual file path
df = pd.read_excel(file_path)

# Extract email ids and answers columns
email_column = df.columns[0]
answers_columns = df.columns[1:]

# Create a dictionary to store email ids and their corresponding answers
data = {email: list(df.loc[df[email_column] == email, answers_columns].values.flatten()) for email in df[email_column]}

# Pair each classmate with their closest match
closest_matches = []

for email, other_email in combinations(data.keys(), 2):
    similarity = jaccard_score(data[email], data[other_email], average='weighted')

    closest_matches.append((email, other_email, similarity))

# Sort the pairs based on similarity scores in descending order
closest_matches.sort(key=lambda x: x[2], reverse=True)

# Create a PrettyTable and set column names
table = PrettyTable()
table.field_names = ["Classmate 1", "Classmate 2", "Similarity Score"]

# Add rows to the table
for email, other_email, similarity in closest_matches:
    table.add_row([email, other_email, similarity])

# Print the table
print(table)
