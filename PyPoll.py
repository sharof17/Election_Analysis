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


     
# Inirialize a total vote counter
total_votes = 0

# Candidate options
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

winning_count = 0

winning_percentage = 0

winning_candidate = ""

# Open the election results and read the file.
with open(file_to_load) as election_data:

     

    # To do: read and analyze the data here.
     file_reader = csv.reader(election_data)

     # Read and print the header row.
     headers = next(file_reader)
     
     # Print each row in the CSV file.
     for row in file_reader:
          
          # Get candidates' names from each row
          candidate_name = row[2]

          if candidate_name not in candidate_options:

               # Add the candidate name to the candidate list.
               candidate_options.append(candidate_name)
               
               candidate_votes[candidate_name] = 0
               
          
          candidate_votes[candidate_name] += 1

          # Add to the total vote count.
          total_votes += 1

     for candidate_name in candidate_votes:
          votes = candidate_votes[candidate_name]
          vote_percentage = float(votes) / float(total_votes) * 100
          print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

          if (votes > winning_count) and (vote_percentage > winning_percentage):
               winning_count = votes
               winning_percentage = vote_percentage
               winning_candidate = candidate_name
          
winning_candidate_summary = (
          f"-------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"-------------------------\n")
print(winning_candidate_summary)


# # Print the total votes
# print(candidate_votes)
     




# # Using the open() statement ot open the file as a text file
# outfile = open(file_to_save, "w")

# with outfile as txt_file:
# # Write some data to the file.
#      txt_file.write("Counties in the Election\n__________________________\n")
#      txt_file.write("Arapahoe\nDenver\nJefferson")


