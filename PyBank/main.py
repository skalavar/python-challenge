# import the os module
import os

# Module for reading CSV files
import csv

#CSV file location
csvpath = os.path.join('Resources', 'budget_data.csv')



#Open CSV file with no header
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #csv_header = (csvfile)
    #csv_header = next(csvreader)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    # find net amount of profit and loss
    total_amount = []
    months = []

    #Read though each row of data after header
    for rows in csvreader:
        total_amount.append(int(rows[1]))
        months.append(rows[0])

    # find revenue change
    revenue_change = []

    for x in range(1, len(total_amount)):
        revenue_change.append((int(total_amount[x]) - int(total_amount[x-1])))

    # calculate average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)

    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(revenue_change)
    # greatest decrease in revenue
    greatest_decrease = min(revenue_change)


    # print the Results
    print("Financial Analysis")

    print("..................")

    print("Total Months: " + str(total_months))

    print("Total: " + "$" + str(sum(total_amount)))

    print("Average change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))


    # output to a text file

    file = open("output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write(".................." + "\n")

    file.write("Total Months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(total_amount)) + "\n")

    file.write("Average Change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    file.close()
