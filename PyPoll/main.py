import os
import csv

#creating a path to the csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#initializing relevant variables
total_votes = 0
dash = "-------------------------------"
winner = ""
pct_array = []
skip = 0    #unnecessary variable to reference when I need to skip the header row in the loop

ccs = "Charles Casper Stockham"
ccs_pct = 0
ccs_votes = 0

ddg = "Diana DeGette"
ddg_pct = 0
ddg_votes = 0

rad = "Raymon Anthony Doane"
rad_pct = 0
rad_votes = 0

#reading in the csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #looping through each row (ballot) in the csv
    for ballot in csvreader:

        #total vote tally increases by 1 for every row
        total_votes += 1

        if ballot[2] == "Candidate":
            skip = 0    #unnecessary, but helps skip the header row
     
        #adding 1 vote to CCS's tally if the ballot is for him
        elif ballot[2] == "Charles Casper Stockham":
            ccs_votes += 1
        
        #adding 1 vote to DDG's tally if the ballot is for her
        elif ballot[2] == "Diana DeGette":
            ddg_votes += 1
        
        #adding 1 vote to RAD's tally if the ballot isn't for the other 2 candidates
        else:
            rad_votes += 1

#finding % of ballots in favor of each candidate and appending them to an array
ccs_pct = round((ccs_votes/total_votes)*100, 2)
pct_array.append(ccs_pct)

ddg_pct = round((ddg_votes/total_votes)*100, 2)
pct_array.append(ddg_pct)

rad_pct = round((rad_votes/total_votes)*100, 2)
pct_array.append(rad_pct)


#determening which candidate had the greatest % of votes and declaring them the winner
if max(pct_array) == ccs_pct:
    winner = ccs
elif max(pct_array) == ddg_pct:
    winner = ddg
else:
    winner = rad

#printing outputs to terminal
print("Election Results")
print(dash)
print(f"Total Votes: {total_votes}")
print(dash)
print(f"{ccs}: {ccs_pct}% ({ccs_votes})")
print(f"{ddg}: {ddg_pct}% ({ddg_votes})")
print(f"{rad}: {rad_pct}% ({rad_votes})")
print(dash)
print(f"Winner: {winner}")
print(dash)

#writing outputs to a new text file PyPoll.txt
with open("PyPoll.txt", "w") as pypolltxt:
    pypolltxt.write("Election Results\n")
    pypolltxt.write(dash + "\n")
    pypolltxt.write(f"{ccs}: {ccs_pct}% ({ccs_votes})\n")
    pypolltxt.write(f"{ddg}: {ddg_pct}% ({ddg_votes})\n")
    pypolltxt.write(f"{rad}: {rad_pct}% ({rad_votes})\n")
    pypolltxt.write(dash + "\n")
    pypolltxt.write(f"Winner: {winner}\n")
    pypolltxt.write(dash)