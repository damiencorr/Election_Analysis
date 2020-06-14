# Election_Analysis

## Project Overview
A Colorado Board of elections employee has given you the following tasks to complete the election audt of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes eah candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.3, Visual Studio Code, 1.45.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast int he election.
- The candidates were
-- Charles Casper Stockham
-- Diana DeGette
-- Raymon Anthony Doane
- The candidate results were:
-- Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
-- Diana DeGette received 73.8% of the vote and 272,892 number of votes.
-- Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
-- Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Challenge Overview

1. Determine the number of votes that were cast from each county and the percentage of votes each county contributed to the election
2. Determine which county had the largest turnout
3. Save the results to election_results.txt
4. Test by printing your results to the output terminal

## Challenge Summary

Deliver the following information via the PyPoll_Challenge.py script: 
1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote
6. The number of votes that were cast from each county
7. The percentage of votes each county contributed to the election
8. The county with the largest turnout

Overall approach -
- Open the resource data file.
- Capture the names of all the candidates.
- Capture the names of all the counties.
- Add a vote counter for each candidate.
- Add a vote counter for each county.
- Get the total votes for each candidate.
- Get the total votes for each county.
- Get the total votes cast for the election.
- Calculate %age of total votes for each candidate
- Calculate %age of total votes contributed by each county
- Identify the winner candidate
- Identify the county with largest turnout
- Output election results as per challenge requirements


Election Results

Total Votes: 369,711


County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

Largest County Turnout: Denver

Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
