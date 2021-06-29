import os
import csv

election = {}

total_votes = 0
candidate = ""
votes_percent = 0
winner_name = ""
winner_count = 0

election_csv = os.path.join('Resources', 'election_data.csv')
        
with open (election_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    print("Election Results")
    print("_______________________")

    for row in csvreader:

        candidate = row[2]
        total_votes = total_votes + 1

        if candidate in election:
            election[candidate] = election[candidate] + 1
        else:
            election[candidate] = 1 

print(f"Total Votes: {total_votes}")
print("_______________________")

for key, value in election.items():
    if value > winner_count:
        winner_name = key
        winner_count = value

    votes_percent = value/total_votes * 100

    print (f" {key} : ({round(votes_percent, 2)}%) {str(value)}")
print("_______________________")
print (f"Winner: {winner_name}")
print("_______________________")

file_name = "election.txt"
with open(os.path.join("Analysis",file_name), "w") as txt_file:

    txt_file.write("Election Results\n")
    txt_file.write("_______________________\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("_______________________\n")
    txt_file.write(f" {key} : ({round(votes_percent, 2)}%) {str(value)}\n")
    txt_file.write("_______________________\n")
    txt_file.write(f"Winner: {winner_name}\n")
    txt_file.write ("_______________________\n") 
    

        
        
        
# The total number of votes cast



# A complete list of candidates who received votes


# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote.