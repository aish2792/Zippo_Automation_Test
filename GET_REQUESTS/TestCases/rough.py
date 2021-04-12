import csv

with open('testdata.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for i in data:
        print(i)