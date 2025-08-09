import sys

current_title = None
total = 0

for line in sys.stdin:
    try:
        title, count = line.strip().split('\t')
        count = int(count)
    except:
        continue

    if title == current_title:
        total += count
    else:
        if current_title:
            print(f"{current_title}\t{total}")
        current_title = title
        total = count

# Emit last record
if current_title:
    print(f"{current_title}\t{total}")
