import os
import csv


# Establish the path
input_file = os.path.join("raw_data", "budget_data.csv")


#emply lists for month and revenue data
months = []
revenue = []


with open(input_file, 'r') as csvfile:
    csvread = csv.reader(csvfile)


next(csvread, None)

    
for row in csvread:
	months.append(row[0])
	revenue.append(row[1])


#find total months
total_months = len(months)

#create greatest increase, decrease variables and set them equal to the first revenue entry
#set total revenue = 0 
greatest_inc = revenue[0]
greatest_dec = revenue[0]
total_revenue = 0

#loop through revenue indices and compare # to find greatest inc and dec
#also add each revenue to total revenue
for r in range(len(revenue)):
    if revenue[r] >= greatest_inc:
        greatest_inc = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_dec:
        greatest_dec = revenue[r]
        great_dec_month = months[r]
    total_revenue += revenue[r]


#calculate average_change
average_change = round(total_revenue/total_months, 2)


# printing results to terminal
print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_revenue))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + greatest_inc_month + " ($" + str(greatest_inc) + ")")
print("Greatest Decrease in Profits: " + greatest_dec_month + " ($" + str(greatest_dec) + ")")

#sets path for output file
output_file = os.path.join("Output","summary" + ".txt")

# opens the output destination in write mode and prints the summary
with open(output_dest, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total: $' + str(total_revenue) + '\n')
    writefile.writelines('Average Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Profits: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Profits: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')

#opens the output file in r mode and prints to terminal
with open(output_dest, 'r') as readfile:
    print(readfile.read())













