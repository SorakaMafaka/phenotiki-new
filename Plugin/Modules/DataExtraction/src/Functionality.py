import csv

with open('PhenotikiData.csv', newline='') as File:
    reader = csv.reader(File, delimeter=' , ', quotechar=' \' ' quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)