import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
output_file = open("PyPollElectionResults.txt", "w")
candidate_dictionary = {}
dashes = "-------------------------"
vote_summary = ""
total_votes = 0

with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile)
#Cycle through the headings of the csv file. We don't need the heandings here so they are not stored.
    next(csvreader)

    for row in csvreader:
#Checks if the candidate name is not in the candidate dictionary.
        if row[2] not in candidate_dictionary:
#Adds the candidate name and initializes the count of votes to 0. 
            candidate_dictionary[row[2]] = 0
#If the candidate exists is adds to the running number of votes for the candidate.
        candidate_dictionary[row[2]] = candidate_dictionary[row[2]] + 1
        total_votes += 1

#Create the candidate summary list dicitonary and append the percent key and values.    
candidate_summary = [{
    "candidate" : row, 
    "votes" : candidate_dictionary[row],
#Get the percent of votes and set the values into the three decimal percent format.
    "percent": "{:.3%}".format(candidate_dictionary[row]/total_votes)
    } for row in candidate_dictionary]
    
winner = max(candidate_dictionary.items(), key = lambda x : x[1])
 
 #Iterate through the list dictionary and store each result record into a variable for printing and/or writing.
for i in candidate_summary:
        vote_summary = vote_summary + (i["candidate"] + ": " + i["percent"] + " (" + str(i["votes"]) + ")\n")

election_results = ("\nElection Results\n" + dashes + "\nTotal Votes:" + str(total_votes) + "\n" + dashes +
        "\n" + vote_summary + dashes + "\nWinner: " + winner[0]+ "\n" + dashes)
    
print(election_results)
output_file.writelines(election_results)
output_file.close()