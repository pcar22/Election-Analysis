# from distutils import text_file

# add our dependencies.
import csv
import os

# Assign a variable to laod a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage. Module 3.5.5 Determine the winning candidate. Before with open statement
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]

    # If the candidate does not match any existing candidate add it to the candidate list. 
        if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list. 
            candidate_options.append(candidate_name)
        # Begin tracking the candidates vote count. 
            candidate_votes[candidate_name] = 0
            #Add a vote to that candidate's count. Line up with if statement to increment each "candidates vote
            candidate_votes[candidate_name] += 1
        
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)


    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Print each candidate, their voter count, and percentage to the terminal.
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") # Commented out this line to write the results
            # Determine winning vote count, winning percentage, and candidiate. Module 3.5.5 if statement inside the for loop.
        if (votes > winning_count) and (vote_percentage > winning_percentage): # Determines if the votes are greater than the winning count. 
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
        
    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Print the winning candidates results to the terminal.
    winning_candidate_summary = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary) # Commented line to write to text file.

# Save the winning candidate's results to the text file. 
txt_file.write(winning_candidate_summary)

                                               
