import csv
import random

# Define the header and rules
header = "Target[D],AL,CCT,ACD,LT,K1,K2,WTW"
ranges = [
    ("Target[D]", -2.5, 1.00),
    ("AL", 19, 35),
    ("CCT", 260, 760),
    ("ACD", 1.25, 5.25),
    ("LT", 2.6, 7.4),
    ("K1", 37, 52),
    ("K2", 37, 52),
    ("WTW", 8.8, 14.50),
]


# Create a CSV file and write the header
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header.split(","))

    # Generate 100 lines following the rules
    for _ in range(100):
        line = []
        for key, min, max in ranges:
            if (key == "K1" or key == "K2"):
                k1 = random.uniform(min, max)
                value = str(float(k1))

                k2 = random.uniform(k1, max)
                value = value + str(float(k2))
                line.append(value)
                continue

            value = str(float(random.uniform(min, max)))

            line.append(value)
        writer.writerow(line)
