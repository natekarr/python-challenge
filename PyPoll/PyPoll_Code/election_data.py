import os
import csv

election_csv = os.path.join("..", "Resources", "election_data.csv")

names = []
counts = []
greatest_votes = 0
winner = ""

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        if row[2] in names:
            counts[names.index(row[2])] = counts[names.index(row[2])] + 1
        else:    
            names.append(row[2])
            counts.append(1)

with open('../Analysis/election_data_output.txt', 'w') as f:
    print("Election Results")
    f.write("Election Results\n")
    print("------------------------------")
    f.write("------------------------------\n")
    total_votes = sum(counts)
    print(f"Total Votes: {total_votes}")
    f.write(f"Total Votes: {total_votes}\n")
    print("------------------------------")
    f.write("------------------------------\n")
    count = 0
    for name in names:
        percent = round(100 * (counts[count] / total_votes), 3)
        print(f"{name}: {percent}% ({counts[count]})")
        f.write(f"{name}: {percent}% ({counts[count]})\n")
        count += 1
        if percent > greatest_votes:
            winner = name
            greatest_votes = percent
    print("------------------------------")
    f.write("------------------------------\n")
    print(f"Winner: {winner}")
    f.write(f"Winner: {winner}\n")
    print("------------------------------")
    f.write("------------------------------\n")