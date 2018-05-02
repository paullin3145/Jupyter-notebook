import csv


with open('100 Records.csv', 'r')as csvfile:
    readCSV = csv.reader(csvfile)
    for line in readCSV:
        print(line)