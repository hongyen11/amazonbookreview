import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    try:
        title = row[0].strip()
        rating = float(row[1].strip())
        if title and 1 <= rating <= 5:
            print(f"{title}\t{rating}")
    except:
        continue
