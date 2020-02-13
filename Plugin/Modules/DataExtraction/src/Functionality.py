import csv
import matplotlib
from Plugin.Modules.DataExtraction.UI import DataExtractionUI

data_array = []
live_data = []
live_dates = []


def open_file(filename):
    with open(filename, newline='') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            data_array.append(row)

# [0] = Date
# [1] = ID
# [2] = Group
# [3] = ProjectedLefArea
# [4] = Diameter
# [5] = Perimeter
# [6] = Stockiness
# [7] = Compactness
# [8] = Hue
# [9] = Count
# [10] = RelativeRateChange
# [11] = AbsoluteGrowthRate
# [12] = RelativeGrowthRate


def plot_graph(selection):
    live_dates.clear()
    live_data.clear()

    for i in data_array:
        live_dates.append(i[0])

    for i in data_array:
        live_data.append(i[selection])

    print(live_dates)
    print(live_data)