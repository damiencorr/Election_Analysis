# Deliver the following information via this script: 
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote


""" Open the data file.
Write down the names of all the candidates.
Add a vote count for each candidate.
Get the total votes for each candidate.
Get the total votes cast for the election. """





# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)


# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()


# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)



import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)
     


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis-0.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World leek")

# Close the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis-1.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    txt_file.write("Counties in the election\n")    
    txt_file.write("------------------------\n")    
    txt_file.write("Arapahoe\nDenver\nJefferson")