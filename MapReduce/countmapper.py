import sys

for line in sys.stdin:
    parts = line.strip().split(",")
    if len(parts) >= 3:
        review_id = parts[2].strip() 
        review_text = parts[-1].strip()  

        word_count = len(review_text.split())
        if word_count > 0:
            print(f"{review_id}\t{word_count}")

