import csv
import scipy.io
import matplotlib.pyplot as plt
from collections import Counter
from Plugin.Modules.DataExtraction.UI import DataExtractionUI

data_array = []
live_data = []
live_dates = []
live_data_float = []


def open_file(filename):  # Load csv with following settings
    with open(filename, newline='') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            data_array.append(row)
            # data_array.clear()


def open_mat_file(filename):  # Load mat with following settings
    mat = scipy.io.loadmat(filename)



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

    count = dict(Counter(live_dates))

    for i in data_array:
        live_data.append(i[selection])

    for i in live_data[1::]:
        live_data_float.append(float(i))


    print(live_data_float[1:24])
    print(sum(live_data_float[1:24]))
    print(data_array)
    print(count)
    print(live_dates)
    print(live_data)
    y_axis = live_dates[1::]
    y = list(dict.fromkeys(y_axis))
    print(y)
