# #The data we need to retrieve.
# # Total number of votes cast
# # A complete list of candidates who received votes
# # Total number of votes each candidate received
# # Percentage of votes each candidate won
# # The winner of the election based on popular vote

# # Assign a variable for the file load and the path.
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)


# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

#Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()






# Using the 'with statement' open the file as a text file.
# with open(file_to_save, "w") as txt_file:
#     # Write some data to the file.
#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Arapahoe\nDenver\nJefferson")

#ELECTION RESULTS#

#add our dependencies.
import csv
import os

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")

#1.  Intialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare an empty dictionary.
candidate_votes = {}  #{"candidate_1": votes, "candidate_2": votes, etc}

# Whinning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file.
    for row in file_reader:
        #2.  Add to the total vote count.
        total_votes +=1

        # Print the cadidate name from each row    
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0  #creates each candidate as a key

 # Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"--------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    # Determine the % of votes for each candidate by looping through the counts.
    #1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #3. Calculate the % of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # TO DO: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        # Determine the winning vote counte and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            #vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            #And, set the winning_cadidate equal to the candidate's name.
            winning_candidate = candidate_name

    #To do: print out the winning candidate, vote count and percentage to 
    # terminal.     
    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


    
