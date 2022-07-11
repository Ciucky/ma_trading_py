# Date, Close/Last, Volume, Open, High, Low
import csv
from unicodedata import name

ma5 = []
c = 1

# Read csv file
file = open('HistoricalQuotesEdited.csv', mode='r')
csvreader = csv.reader(file)
rows = []
for row in csvreader:
        rows.append(row)


#for i in range(10):
    # print(row)
#    if i > 5:
#        csv_reader[i][]
print(rows[2][1])


# close file
file.close()