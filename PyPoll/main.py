import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
can_count={}
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        #print (row)
        if row[2] not in can_count:
            can_count[row[2]] = 0
        can_count[row[2]] = can_count[row[2]] + 1
    total_votes= (csvreader.line_num-1)
    can_smry=[{"candidate" : row, "votes" : can_count[row], "percent": "{:.3%}".format(can_count[row]/total_votes)} for row in can_count]
    winner = max(can_count.items(), key= lambda x : x[1])
    print("Total Votes:", total_votes)
    #print(can_smry)
    for i in can_smry:
        print(i["candidate"] + ": " + i["percent"] + " (" + str(i["votes"]) + ")")
    print("Winner:", winner[0])
    
    
    
    