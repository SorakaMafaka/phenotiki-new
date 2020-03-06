import csv

from pymatreader import read_mat

matdata = {}
data_array = []
live_data = []
live_dates = []


def open_mat_file():  # Load mat with following settings
    #This could probably get cleaned up...
    global matdata
    data = read_mat("testmat.mat")
    data = data['ans']
    mdata = data['Sequences']
    #Subject holds the main plantdatasets
    mdata = mdata['Subject']
    #By setting this to 0 only the first plant data set gets used.
    #This is just, so we can access the keys of the individual datasets.
    #So at the moment it will only save the first one.
    mdata = mdata[1]
    matdata = mdata

    print(matdata)


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
   # live_dates.clear()
   # live_data.clear()

   # for i in data_array:
   #     live_dates.append(i[0])
   #prints selection from choice buttton and then the selected values for the first plantdataset
    print(selection)
    print(matdata[selection])
    #for i in data_array:
        #live_data.append(i[selection])

#    print(live_dates)
#    print(live_data)
#    y_axis = live_dates[1::]
#    x_axis = live_data[1::]
#    print(y_axis)
#    print(x_axis)
#    fig, axs = plt.subplots(2, 2, figsize=(5, 5))
#    axs[0, 0].hist(live_data)
#    plt.show()
