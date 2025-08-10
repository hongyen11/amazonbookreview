# Python + SQLite Version
import pandas as pd
import sqlite3

# Load only needed column
df = pd.read_excel("cleaned_amazonbook.csv.xlsx", usecols=['Title'])

# Make sure Title is a string
df['Title'] = df['Title'].astype(str)

# Create SQLite in-memory database
conn = sqlite3.connect(":memory:")
df.to_sql("book_reviews", conn, index=False, if_exists="replace")

# SQL query for top 10 books by review count
query_review_count = """
SELECT Title, COUNT(*) AS review_count
FROM book_reviews
GROUP BY Title
ORDER BY review_count DESC
LIMIT 10;
"""

# Run and print results
print("=== Top 10 Books by Review Count (SQL) ===")
review_count_sql = pd.read_sql(query_review_count, conn)
for _, row in review_count_sql.iterrows():
    print(f"{row['Title']} {row['review_count']}")