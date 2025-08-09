import sys

current_title = None
total_rating = 0
count = 0

for line in sys.stdin:
    try:
        title, rating = line.strip().split("\t")
        rating = float(rating)
    except:
        continue

    if current_title == title:
        total_rating += rating
        count += 1
    else:
        if current_title and count > 0:
            avg = total_rating / count
            print(f"{current_title}\t{avg:.2f}")
        current_title = title
        total_rating = rating
        count = 1

# Last record
if current_title and count > 0:
    avg = total_rating / count
    print(f"{current_title}\t{avg:.2f}")
