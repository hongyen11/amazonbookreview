import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    try:
        title = row[0].strip()
        if title:
            print(f"{title}\t1")
    except:
        continue
