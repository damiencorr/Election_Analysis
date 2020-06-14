

# Challenge:
# 1. Determine the number of votes that were cast from each county and 
# the percentage of votes each county contributed to the election
# 2. Determine which county had the largest turnout
# 3. Save the results to  election_results.txt
# 4. Test by printing your results to the output terminal

# Instructions
# 1. Make a copy of the PyPoll.py file that you used throughout this module and rename it PyPoll_Challenge.py.
# 2. Create a list for the counties.
# 3. Create a dictionary where the county is the key and the votes cast for each county in the election are the values.
# 4. Create an empty string that will hold the county name that had the largest turnout.
# 5. Declare a variable that represents the number of votes that a county received. 
#   Hint: Inside a for loop, add an if statement to check if the county name has already been recorded. 
#       If not, add it to the list of county names.
# 6. Inside the with open() function where you are outputting the file, do the following:
#       Create three if statements to print out the voter turnout results similar to the results shown above.
#       Add the results to the output file.
#       Print the results to the command line.

""" 
EXPECTED OUTPUT

Election Results
-------------------------
Total Votes: 369,711
-------------------------

County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

-------------------------
Largest County Turnout: Denver
-------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------

 """


# Deliver the following information via this script: 
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote
# 6. The number of votes that were cast from each county
# 7. The percentage of votes each county contributed to the election
# 8. The county with the largest turnout

# Overall approach -
# Open the data file.
# Capture the names of all the candidates.
# Capture the names of all the counties.
# Add a vote counter for each candidate.
# Add a vote counter for each county.
# Get the total votes for each candidate.
# Get the total votes for each county.
# Get the total votes cast for the election.
# Calculate %age of total votes for each candidate
# Calculate %age of total votes contributed by each county
# Identify the winner candidate
# Identify the county with largest turnout
# 
# Output election results as per requirements


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
# Declare the empty Candidate dictionary.
candidate_votes = {}

# County Options
county_options = []
# Declare the empty County dictionary.
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Highest Turnout County tracker
highest_turnout_county = ""
highest_count_county = 0
highest_percentage_county = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    # print(headers)    

    # Read each row in the CSV file.
    for row in file_reader:
        # Add the total vote count.
        total_votes +=1

        # Identify the candidate name from each row.
        candidate_name = row[2]

        # Identify the County name in each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing county...
        if county_name not in county_options:
            # Add it to the list of Counties.
            county_options.append(county_name)

            # Begin tracking that county's vote count. 
            county_votes[county_name] = 0
            
        # Add a vote to that county's count.
        county_votes[county_name] += 1



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    county_summary1 = ("\nCounty Votes:\n")
    print(county_summary1)
    txt_file.write(county_summary1)
    for county in county_votes:
        votes = county_votes[county]
        # print(f"{county} = {votes:,}")
        vote_percentage = int(votes) / int(total_votes) * 100
        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)
        # Determine highest vote count and county
        # Determine if this votes is greater than the winning count.
        if (votes > highest_count_county) and (vote_percentage > highest_percentage_county):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            highest_count_county = votes
            highest_percentage_county = vote_percentage
            # And, set the highest turnout county equal to the county's name.
            highest_turnout_county = county

    county_summary2 = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {highest_turnout_county}"
        f"\n-------------------------\n"
    )
    txt_file.write(county_summary2)
    print(county_summary2)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # 4. Format the candidate name and percentage of votes.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Write each candidate, their voter count, and percentage to the terminal and file.
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

    #  Write the winning candidate, vote count and percentage to
    #   file.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # Save the winning candidate's name to the text file.
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

