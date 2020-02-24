import csv

from pymatreader import read_mat


data_array = []
live_data = []
live_dates = []


class dataset:
    def __init__(self):
        self.dict = {"Date": [],
                     "ProjectedLeafArea": [],
                     "Diameter": [],
                     "Perimeter": [],
                     "Stockiness": [],
                     "Compactness": [],
                     "Hue": [],
                     "Count": [],
                     "RelativeRateChange": [],
                     "AbsoluteGrowthRate": [],
                     "RelativeGrowthRate": []}


def open_file(filename):  # Load csv with following settings
    data = dataset()
    with open(filename, newline='') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            column = 0
            for key in data.dict:
                if column != 1:
                    data.dict[key].append(row[column])
                    print(row[column])
                column += 1
            # data_array.clear()


def open_mat_file(filename, dataSelections):  # Load mat with following settings
    data = read_mat(filename)
    mdata = data['ans']
    mdata = mdata['Sequences']
    print(mdata['Filename'][0])
    mdata = mdata['Subject']
    mdata = mdata[0]
    for key in dataSelections:
        print(key, mdata[key])

    print("Diameter - ", mdata['Diameter'])



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

#    print(live_dates)
#    print(live_data)
#    y_axis = live_dates[1::]
#    x_axis = live_data[1::]
#    print(y_axis)
#    print(x_axis)
#    fig, axs = plt.subplots(2, 2, figsize=(5, 5))
#    axs[0, 0].hist(live_data)
#    plt.show()
