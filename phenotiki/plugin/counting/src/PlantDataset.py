import struct


class PlantDataset:
    def __init__(self):
        self.Sequences = []  # Image sequences of the time lapse
        self.NumberOfSubjects = 0  # Total number of subjects across all the time lapse pictures
        self.MaxImageSize = [1, 1]  # Biggest plant image in the dataset
        self.Basepath = ''  # Dataset basepath
        self.ml = {}  # Machine learning data