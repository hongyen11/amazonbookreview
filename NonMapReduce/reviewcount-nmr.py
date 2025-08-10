# Python (Pandas)
import pandas as pd

# Load dataset
df = pd.read_excel("cleaned_amazonbook.csv.xlsx", usecols=['Title'])

# Make sure Title is a string to avoid type errors
df['Title'] = df['Title'].astype(str)

# Count reviews per book
review_count = df.groupby('Title', as_index=False).size()

# Rename columns for clarity
review_count.columns = ['Title', 'review_count']

# Sort by count (descending) and get top 10
top10_review_count = review_count.sort_values(by='review_count', ascending=False).head(10)

print("=== Top 10 Books by Review Count ===")
for _, row in top10_review_count.iterrows():
    print(f"{row['Title']} {row['review_count']}"