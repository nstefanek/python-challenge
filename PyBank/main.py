# import dependencies
import os
import csv

# create lists
months = []
profit_total = []
profit_change = []

# load csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    reader = csv.reader(csvfile)
    next(reader, None) # skip header
    
# iterate through rows
    for row in reader:
    
        #append ttl months and profits to correspinding lists
        months.append(row[0])
        profit_total.append(int(row[1]))
    
    # iterate through profits to get monthly change
    for i in range(len(profit_total)-1):
    
        # difference between 2 months, append to profit change
        profit_change.append(profit_total[i+1]-profit_total[i])

# max and min of the profit change list
max_value = max(profit_change)
min_value = min(profit_change)

# add max and min to the right month
max_month = profit_change.index(max(profit_change)) + 1
min_month = profit_change.index(min(profit_change)) + 1

# print results
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit_total)}")
print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {months[max_month]} (${(str(max_value))})")
print(f"Greatest Decrease in Profits: {months[min_month]} (${(str(min_value))})")

# create a text file with results
output_file = 'Analysis/financial_analysis.txt'
with open(output_file,"w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow("Financial Analysis")
    csvwriter.writerow("-------------------")
    csvwriter.writerow(f"Total Months: {len(months)}")
    csvwriter.writerow(f"Total: ${sum(profit_total)}")
    csvwriter.writerow(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
    csvwriter.writerow(f"Greatest Increase in Profits: {months[max_month]} (${(str(max_value))})")
    csvwriter.writerow(f"Greatest Decrease in Profits: {months[min_month]} (${(str(min_value))})")
    
