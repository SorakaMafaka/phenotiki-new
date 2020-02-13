import csv
import matplotlib
from Plugin.Modules.DataExtraction.UI import DataExtractionUI

data_array = []

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
