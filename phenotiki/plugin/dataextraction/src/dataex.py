import csv

from pymatreader import read_mat


def open_mat_file(filename):  # Load mat with following settings
    data = read_mat(filename)
    data = data['ans']
    matdata = data['Sequences']

    return matdata
  #  print(mdata['Timestamp'])
   # timeData = mdata['Timestamp']
    # Subject holds the main plantdatasets
    #mdata = mdata['Subject']

    #matdata = mdata



