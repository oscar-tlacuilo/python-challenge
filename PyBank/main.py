import csv

# Define the path to the CSV file
csv_file_path = "budget_data.csv"

# Initial variables
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

# Read the CSV file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(csvreader)

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Extract date and profit/loss values
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total months and net total
        total_months += 1
        net_total += profit_loss

        # Calculate profit/loss changes and store the values
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            months.append(date)

        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_increase_date = months[profit_loss_changes.index(greatest_increase)]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_date = months[profit_loss_changes.index(greatest_decrease)]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Finantial analysis results
with open("financial_analysis_results.txt", 'w') as result_file:
    result_file.write("Financial Analysis\n")
    result_file.write("----------------------------\n")
    result_file.write(f"Total Months: {total_months}\n")
    result_file.write(f"Total: ${net_total}\n")
    result_file.write(f"Average Change: ${round(average_change, 2)}\n")
    result_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    result_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
