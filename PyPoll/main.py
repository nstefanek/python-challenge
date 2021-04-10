# import dependencies
import os
import csv

# variables
total_votes = 0
khan = 0
correy = 0
li = 0
otooley = 0

# load csv file
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    reader = csv.reader(csvfile)
    next(reader, None) # skip header

# iterate through rows
    for row in reader:
    
        # count voter ids and add to variable
        total_votes +=1
        
        #count times candidates names are found and add to variable
        if row[2] == "Khan":
            kan +=1
        elif row[2] == "Correy":
            correy +=1
        elif row[2] == "Li":
            li = +=1
        elif row[2] == "O'Tooley":
            otooley +=1
            
# make a dictionary from lists created
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan, correy, li, otooley]

# zip together and return winner
dict_candidates_votes = dict(zip(candidates, votes))
winner = max(dict_candidates_votes, winner=dict_candidates_votes.get)

# find percentages of votes
khan_percent = (khan/total_votes) *100
correy_percent = (correy/total_votes) *100
li_percent = (li/total_votes) *100
otooley_percent = (otooley/total_votes) *100

# print results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan})")
print(f"Correy: {correy_percent:.3f}% ({correy})")
print(f"Li: {li_percent:.3f}% ({li})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley})")
print(f"----------------------------")
print(f"Winner: {winner}")

# create a text file with results
output_file = 'Analysis/financial_analysis.txt'
with open(output_file,"w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(f"Election Results")
    csvwriter.writerow(f"----------------------------")
    csvwriter.writerow(f"Total Votes: {total_votes}")
    csvwriter.writerow(f"Khan: {khan_percent:.3f}% ({khan})")
    csvwriter.writerow(f"Correy: {correy_percent:.3f}% ({correy})")
    csvwriter.writerow(f"Li: {li_percent:.3f}% ({li})")
    csvwriter.writerow((f"O'Tooley: {otooley_percent:.3f}% ({otooley})")
    csvwriter.writerow(f"----------------------------")
    csvwriter.writerow(f"Winner: {winner}")

