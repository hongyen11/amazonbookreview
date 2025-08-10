# Python + SQLite Version
import pandas as pd
import sqlite3

# Load only needed columns
df = pd.read_excel("cleaned_amazonbook.csv.xlsx", usecols=['Id', 'review/text'])

# Create SQLite in-memory database
conn = sqlite3.connect(":memory:")
df.to_sql("book_reviews", conn, index=False, if_exists="replace")

# SQL query to get word count per review
query_wordcount = """
SELECT Id,
       LENGTH(TRIM("review/text")) - LENGTH(REPLACE(TRIM("review/text"), ' ', '')) + 1 AS word_count
FROM book_reviews
ORDER BY word_count DESC
LIMIT 10;
"""

# Run and print results
print("=== Top 10 Reviews by Word Count (SQL) ===")
print(pd.read_sql(query_wordcount, conn).to_string(index=False))