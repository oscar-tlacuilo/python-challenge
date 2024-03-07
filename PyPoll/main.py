import csv

# Define the path to the CSV file (relative path)
csv_file_path = "election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}  # Dictionary to store candidate names and their vote counts

# Read the CSV file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(csvreader)

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Extract candidate name
        candidate_name = row[2]

        # Count total votes
        total_votes += 1

        # Update candidate vote count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Initialize variables for winner calculation
winner = ""
max_votes = 0

# Calculate and print results
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")

# Create and write results to a text file
with open("election_results.txt", 'w') as result_file:
    result_file.write("Election Results\n")
    result_file.write("----------------------------\n")
    result_file.write(f"Total Votes: {total_votes}\n")
    result_file.write("----------------------------\n")

    # Iterate through candidates
    for candidate, votes in candidates.items():
        # Calculate percentage of votes
        percentage = (votes / total_votes) * 100

        # Print candidate results
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        result_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        # Check for the winner
        if votes > max_votes:
            max_votes = votes
            winner = candidate

    result_file.write("----------------------------\n")
    result_file.write(f"Winner: {winner}\n")
    result_file.write("----------------------------\n")

# Winner results
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")
