# import dependencies
import os
import csv

# define variables
months = []
prof_loss_changes = []
net_change = []

avg_net_change = 0
total_months = 0

# load csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    reader = csv.reader(csvfile)
    next(reader, None)
    
# add values
    for row in reader:
        months = row[0]
        months.append(month)
        values = int(row[1])
        p.append(values)
        
total_months = len(months)
net_total = sum(p)
net_total_months = len(months) - 1
diff_budget_data = []

for i in range(len(p) - 1):
    diff_budget_data.append(float(p[i + 1]) - float(p[i]))
    new_net_total = sum(diff_budget_data)
    
# sum of prof/loss
avg_net_change = new_net_total/net_total_months

# greatest increase + decrease over entire period
min_p = p[p.index(min(p))] - p[p.index(min(p))-1]
max_p = p[p.index(max(p))] - p[p.index(max(p))-1]

# print results
print("Financial Analysis")
print("-------------------')
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(ave_net_change,2)}")
print(f"Greatest Increase in Profits: {months[p.index(max(p))]} (${max_p})")
print(f"Greatest Decrease in Profits: {months[p.index(min(p))]} ($min_p})")

# create a text file with results
output_file = 'Analysis/financial_analysis.txt"
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------'])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: ${net_total}"])
    csvwriter.writerow([f"Average Change: ${round(ave_net_change,2)}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {months[p.index(max(p))]} (${max_p})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {months[p.index(min(p))]} ($min_p})"])
    
