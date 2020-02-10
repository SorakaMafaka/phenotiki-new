import csv

with open('PhenotikiData.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)