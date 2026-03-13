import csv

# Writing CSV
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name"])
    writer.writerow([1, "Alice"])
    writer.writerow([2, "Bob"])

# Reading CSV
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)