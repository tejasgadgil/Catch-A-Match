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

#calculate cosine similarity
similarity_matrix = cosine_similarity(text_matrix, text_matrix)

#create df to store the similarity scores
similarity_df = pd.DataFrame(similarity_matrix, columns=df['Email Address'], index=df['Email Address'])

#find most similar pairs while ensuring each person is matched only once
matched_emails = set()
matched_pairs = []
for email in df['Email Address']:
    #sort similarity scores in descending order and find the most similar person not already matched
    similar_person = similarity_df[email].sort_values(ascending=False)
    for match_email in similar_person.index:
        if match_email != email and match_email not in matched_emails and email not in matched_emails:
            matched_pairs.append((email, match_email))
            matched_emails.add(email)
            matched_emails.add(match_email)
            break

#display the matched pairs
for pair in matched_pairs:
    print(f"{pair[0]} is matched with {pair[1]}")
