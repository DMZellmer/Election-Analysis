# Election-Analysis

##Project Overview
A Colorado Board of Elections employee has given you the follwing tasks to complete the election audit of a recent local confressional election.

1. Calculate the total number of votes cast. 
2. Get a a complete list of the candidates who received votes. 
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

##Resouces
--Data Source: election_results.csv
--Software: Python 3.9.1, Visual Studio Code 1.58.2

##Summary
The analysis of the election show that: 
 -There were 369,711 votes cast in this election.
 -The candidates were: 
      Charles Casper Stockham
      Diana DeGette
      Raymon Anthony Doane
      
##Results
Charles Casper Stockham received 23.0% of the total vote with 85,213 votes.
Diana DeGette received 73.8% of the total votal with 272,892 votes for a landslide victory in this election.
Raymon Anthony Doane came in third with 3.1% total vote or 11,606 votes.

##Challenge Overview
The election commission has requested additional data to complete the audit:
1. The voter turnout for each county
Jefferson: 38,855 (10.5%)
Denver: 306,055 (82.8%)
Arapahoe: 24,801 (6.7%)

Denver county had the highest voter turnout (306,055 votes) (82.8% of total votes)

![Screenshot (13)](https://user-images.githubusercontent.com/86337475/126909509-07a32c8b-8938-4634-907d-b8ab8d2239f8.png)

Above you can see two separate python scripts with very similar conditional for loops. The code on the left pulls the votes for each county, counts the votes and determines the county with the highest voter turnout, as well as the percentage of total votes from all three counties. The code on the right counts the votes for each candidate and determines the winner by votes and reports total votes for each candidate as well as the percentage of the total votes.  This type of code could be used for future election audits as well as providing a more in-depth analysis on election results such as which candidate had the highest votes in which county, for example. This type of data could be useful to the candidates going forword to identify areas where they need to focus their efforts more, or where their voter strongholds are.
