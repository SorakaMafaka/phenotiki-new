import struct


class PlantDataset:
    Sequences = []  # Image sequences of the time lapse
    NumberOfSubjects = 0  # Total number of subjects across all the time lapse pictures
    MaxImageSize = [1, 1]  # Biggest plant image in the dataset
    Basepath = ''  # Dataset basepath
    ml = struct()  # Machine learning data
