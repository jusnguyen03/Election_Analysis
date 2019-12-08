# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize a total county vote counter.
total_county_votes = 0

# Largest County and Count Tracker
largest_county_winner = ""

# County Options and county votes.
counties = []

# Declare the empty dictionary
county_votes = {}

# Candidate Options and candidate votes.
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file for the Candidate.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
        county_name = row[1]

        # if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # if the county does not match any existing county...
        if county_name not in counties:
            # Add the county name to the county list.
            counties.append(county_name)
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
    
    county_results = (
        f"\nCounty Votes:\n")
    print(county_results, end="")
    txt_file.write(county_results)

    # Determine the percentage of votes for each county by looping through the counts.
    # Iterate through the county list.
    for county in county_votes:
        # Retrieve vote count and percentage.
        co_votes = county_votes[county]
        co_vote_percentage = float(co_votes) / float(total_votes) * 100
        county_total_results = (
            f"{county}: {co_vote_percentage:.1f}% ({co_votes:,})\n")

        # Print each county's voter count and percentage to the terminal.
        print(county_total_results)
        txt_file.write(county_total_results)

    for county, votes in county_votes.items():
        if votes == max(county_votes.values()):
            largest_county_winner = county
            largest_county_summary = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {largest_county_winner}\n"
            f"-------------------------\n")
            # Print (larguest_county_summary)
            print(largest_county_summary, end="")
            # Save the largest county file to text
            txt_file.write(largest_county_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)