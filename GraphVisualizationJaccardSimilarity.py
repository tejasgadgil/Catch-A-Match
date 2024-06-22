import pandas as pd
from itertools import combinations
from sklearn.metrics import jaccard_score
import networkx as nx
import matplotlib.pyplot as plt

# Load the Excel sheet
file_path = '/content/ModifiedAnswers.xlsx'  # Update with your actual file path
df = pd.read_excel(file_path)

# Extract email ids and answers columns
email_column = df.columns[0]
answers_columns = df.columns[1:]

# Create a dictionary to store email ids and their corresponding answers
data = {email: list(df.loc[df[email_column] == email, answers_columns].values.flatten()) for email in df[email_column]}

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(data.keys())

# Find the most similar pairs based on Jaccard similarity
max_similarity = 0
most_similar_pair = ()

for pair in combinations(data.keys(), 2):
    similarity = jaccard_score(data[pair[0]], data[pair[1]], average='weighted')  # Specify the 'average' parameter

    # Add an edge if the similarity is above a certain threshold (adjust as needed)
    if similarity > 0.5:
        G.add_edge(pair[0], pair[1], weight=similarity)

# Draw the graph
pos = nx.spring_layout(G)  # You can try other layout algorithms as well
nx.draw(G, pos, with_labels=True, font_size=8, node_size=800, font_color="black", font_weight="bold")

# Add edge labels with similarity scores
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Display the graph
plt.show()
