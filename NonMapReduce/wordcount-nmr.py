# Python (Pandas)
import pandas as pd

# Load dataset
df = pd.read_excel("cleaned_amazonbook.csv.xlsx", usecols=['Id', 'review/text'])

# Ensure all reviews are strings, count words, and ensure int type
df['word_count'] = (
    df['review/text']
    .astype(str)
    .apply(lambda x: len(x.split()))
    .astype(int)
)

# Sort and get top 10 reviews by word count
top10_reviews_wordcount = (
    df[['Id', 'word_count']]
    .sort_values(by='word_count', ascending=False)
    .head(10)
)

print("=== Top 10 Reviews by Word Count ===")
print(top10_reviews_wordcount.to_string(index=False))