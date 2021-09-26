import csv

path = 'your_database.csv'

with open(path) as file:
    readCSV = csv.reader(file, delimiter=';')
    for row in readCSV:
        print(row)
