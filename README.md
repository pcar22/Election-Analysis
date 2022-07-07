# Election-Analysis

## Project Overview
Seth , a Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate won.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote. 
6. The voter turnout for each county.
7. The percentage of votes from each county out of the total count.
8. The county with the highest turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.12, Visual Studio Code, 1.68.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
-   The voter turnout for each county, percentage of votes from county out of the total count, and the county with the highest turnout are shown in the image below. -   This was accomplished using a for loop and conditional statements to print the results from the election_results.csv file provided. A text file is saved in the     analysis folder as election_analysis.txt.

![county_votes](https://github.com/pcar22/Election-Analysis/blob/main/Resources/county_votes.png)

## Challenge Overview
A script was written using Python, this script is written to pull information from the election_results.csv file provided. In this script we can extract the information needed to do get the candidate, county and number of votes. Calculations are done to total votes and percentages. 
## Challenge Summary
The PyPoll.py script is a great tool to use to reveal critical data. This is a great tool to use on other election data. With some modifications this script can extract other information to produce different reports.   
