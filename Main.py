# Date, Close/Last, Volume, Open, High, Low
import csv
from unicodedata import name

ma5 = 0.0
ma10 = 0.0
ma20 = 0.0
ma50 = 0.0
ma100 = 0.0
ma200 = 0.0
c = 1


# Read csv file
file = open('HistoricalQuotesEdited.csv', mode='r')
csvreader = csv.reader(file)
rows = []
for row in csvreader:
        rows.append(row)

length = len(rows)

for i in range(length):
    #print(rows[i])
    # Calculate 5 day Moving Average adn add it to the end of the row
    if i >= 5:
        ma5 = float(rows[i-5][1]) + float(rows[i-4][1]) + float(rows[i-3][1]) + float(rows[i-2][1]) + float(rows[i-1][1])
        ma5 /= 5
        print(ma5)
        rows[i].append(ma5)

    # Calculate 10 day Moving Average adn add it to the end of the row
    if i >= 10:
        for j in range(11):
            if j == 0:
                j = 1
            ma10 += float(rows[i-j][1])
        ma10 /= 10
        print(ma10)
        rows[i].append(ma10)

    # Calculate 20 day Moving Average adn add it to the end of the row
    if i >= 20:
        for j in range(21):
            if j == 0:
                j = 1
            ma20 += float(rows[i-j][1])
        ma20 /= 20
        print(ma10)
        rows[i].append(ma20)

    # Calculate 50 day Moving Average adn add it to the end of the row
    if i >= 50:
        for j in range(51):
            if j == 0:
                j = 1
            ma50 += float(rows[i-j][1])        
        ma50 /= 50
        print(ma50)
        rows[i].append(ma50)
    
    # Calculate 100 day Moving Average adn add it to the end of the row
    if i >= 100:
        for j in range(101):
            if j == 0:
                j = 1
            ma100 += float(rows[i-j][1])
        ma100 /= 100
        print(ma100)
        rows[i].append(ma100)

    # Calculate 200 day Moving Average adn add it to the end of the row
    if i >= 200:
        for j in range(201):
            if j == 0:
                j = 1
            ma200 += float(rows[i-j][1])
        ma200 /= 200
        print(ma200)
        rows[i].append(ma200)

    
    #print(rows[i])


# close file
file.close()


#with open('Moving_Averages.csv', mode='w') as ma_file:
#    writers = csv.writer(ma_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#    for row in rows:
#        writers.writerow(row)
