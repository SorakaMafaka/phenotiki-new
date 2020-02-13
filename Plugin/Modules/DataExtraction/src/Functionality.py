import csv

data_array = []
def open_file(filename):
    with open(filename, newline='') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            data_array.append(row)
    print(data_array)