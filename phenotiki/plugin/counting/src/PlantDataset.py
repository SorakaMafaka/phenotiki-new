import struct

#Author(s):
#   Converted from "Phenotiki - True phenotyping-in-a-box solution"
#   by Steven Dixon, Milena Bromm, Mateusz Glowacki
#   Original "Phenotiki - True phenotyping-in-a-box solution"
#   by M. Minervini and M.V. Giuffrida from IMT Advanced Studies of Lucca, S. Tsaftaris from University of Edinburgh
#
#
#   Version:   1.0
#   Date:      24/04/2020

class PlantDataset:
    def __init__(self):
        self.Sequences = []  # Image sequences of the time lapse
        self.NumberOfSubjects = 0  # Total number of subjects across all the time lapse pictures
        self.MaxImageSize = [1, 1]  # Biggest plant image in the dataset
        self.Basepath = ''  # Dataset basepath
        self.ml = {}  # Machine learning data