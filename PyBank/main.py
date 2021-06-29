import os
import csv

total_profit_losses = 0
current = 0
last = 0

total_change = 0
date = 0
change = 0

greatest_increase = 0
greatest_decrease = 999999999999

budget_csv = os.path.join('Resources', 'budget_data.csv')

with open (budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_profit_losses=total_profit_losses + int(row[1])
        date = date +1
        current = int(row[1])

        if date >1:
            change = current - last

            total_change = total_change + change

        last = int(row[1])
    
        average_change = total_change / date
        
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]

        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]

print("Financial Analysis")
print("_________________________")
print(f"Total Months: {date}")
print (f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} {greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} {greatest_decrease}")

file_name = "budget.txt"
with open(os.path.join("Analysis",file_name), "w") as txt_file:

    txt_file.write("Financial Analysis\n")
    txt_file.write("_________________________\n")
    txt_file.write(f"Total Months: {date}\n")
    txt_file.write(f"Total: ${total_profit_losses}\n")
    txt_file.write(f"Average Change: ${average_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} {greatest_increase}\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} {greatest_decrease}\n")
    