# Open the data file.
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.


import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
     file_reader = csv.reader(election_data)

     # Read and print the header row.
     headers = next(file_reader)
     print(headers)
     
     # Print each row in the CSV file.
     for row in file_reader:
       print(row)

     




# # Using the open() statement ot open the file as a text file
# outfile = open(file_to_save, "w")

# with outfile as txt_file:
# # Write some data to the file.
#      txt_file.write("Counties in the Election\n__________________________\n")
#      txt_file.write("Arapahoe\nDenver\nJefferson")


