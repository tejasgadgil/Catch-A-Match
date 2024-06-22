import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#load excel sheet into a pd df
file_path = '/content/ModifiedAnswers.xlsx'
df = pd.read_excel(file_path)

#select columns containing text data (ignore email column)
text_columns = df.columns[1:]

#combine all text columns into a single column for each student
df['combined_answers'] = df[text_columns].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)

#CountVectorizer - text data into a matrix of token counts
vectorizer = CountVectorizer()
text_matrix = vectorizer.fit_transform(df['combined_answers'])

#calculate cosine similarity between each pair
similarity_matrix = cosine_similarity(text_matrix, text_matrix)

#create df to store the similarity scores
similarity_df = pd.DataFrame(similarity_matrix, columns=df['Email Address'], index=df['Email Address'])

#find the most similar pairs
most_similar_pairs = []
for email in df['Email Address']:
    similar_classmates = similarity_df[email].sort_values(ascending=False)[1:3]  #top 2 most similar classmates
    most_similar_pairs.append((email, similar_classmates.index[0], similar_classmates.index[1]))

#display the most similar pairs
for pair in most_similar_pairs:
    print(f"{pair[0]} is most similar to {pair[1]} and {pair[2]}")

