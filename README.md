# Catch a Match: Student Quiz Matching Tool

Welcome to "Catch a Match," where we turn quiz responses into unexpected connections! This tool analyzes quiz answers from MKSSS's Cummins College of Engineering For Women to pair participants based on answer similarities. Developed for Gandhaar, our college festival, in collaboration with the Wings Magazine Club.

## Project Description

Ever wondered who thinks like you? This project dives into student responses, using clever algorithms to uncover similarities between classmates' answers. Whether it's uncovering quiz twins or surprising matches, expect insights and connections that spark curiosity.

## Key Features

- **Cosine Similarity Analysis:** Crunches text data using CountVectorizer and cosine similarity to find kindred spirits in the quiz realm.
- **Jaccard Similarity Analysis:** Plays matchmaker by comparing answer sets with the Jaccard index—perfect for discovering unexpected quiz alliances.
- **Visualize Connections:** Opt for a fun network graph visualization (using NetworkX and Matplotlib) to see how classmates connect through their quiz answers.
- **Get Results:** Discover the quirkiest quiz duos with outputs that range from friendly console prints to structured tables (thanks to PrettyTable).

## Usage

1. **Setup:** 
   - Clone the repository and prep your quiz data:
     ```bash
     git clone https://github.com/tejasgadgil/Catch-A-Match.git
     cd Catch-A-Match
     ```
   - Install the magic: 
     ```bash
     pip install pandas scikit-learn networkx matplotlib prettytable
     ```

2. **Data Dive:** 
   - Drop your Excel file (`QuizAnswers.xlsx`) into the project folder.

3. **Run the Show:**
   - Take your pick:
     - **Cosine Similarity Analysis:**
       ```bash
       python CosineSimilarityMatch.py
       python CosineSimilarityTwoMatches.py
       ```
     - **Jaccard Similarity with Visual Pizzazz:**
       ```bash
       python TopMatchJaccardSimilarity.py
       python GraphVisualizationJaccardSimilarity.py
       python MatchesWithSimilarityScoresJaccardSimilarity.py
       ```

4. **Catch the Matches:**
   - See who clicks! Dive into results to find surprising quiz matches and explore how classmates' quiz brains sync up.

## Let's Make a Match!

Join us in uncovering quiz camaraderie and surprising connections at Gandhaar. Feel free to fork, contribute, and share your insights as we make "Catch a Match" a quiz adventure to remember!
