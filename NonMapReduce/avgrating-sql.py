import pandas as pd
import sqlite3

# Load and clean before inserting into SQL
df = pd.read_excel("cleaned_amazonbook.csv.xlsx", usecols=['Title', 'review/score'])
df['Title'] = df['Title'].astype(str)
df['review/score'] = pd.to_numeric(df['review/score'], errors='coerce')
df = df.dropna(subset=['review/score'])

# Insert into SQLite
conn = sqlite3.connect(":memory:")
df.to_sql("book_reviews", conn, index=False, if_exists="replace")

# SQL query
query = """
SELECT Title, ROUND(AVG("review/score"), 2) AS avg_rating
FROM book_reviews
GROUP BY Title
ORDER BY avg_rating DESC, Title ASC
LIMIT 10;
"""

avg_rating_sql = pd.read_sql(query, conn)

print("=== Top 10 Books by Average Rating (SQL) ===")
for _, row in avg_rating_sql.iterrows():
    print(f"{row['Title']} {row['avg_rating']:.2f}")