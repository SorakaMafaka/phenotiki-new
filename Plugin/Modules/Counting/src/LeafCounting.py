from typing import List, Any
import os  # Used to get absolute current working directory
import numpy
import wx
import struct


class LeafCounting:
    def __init__(self):
        self.properties()  # Transient doesn't exist in Python, TODO: https://stackoverflow.com/questions/6313421/can-i-mark-variables-as-transient-so-they-wont-be-pickled
        dataset = struct  # Not sure if correct?
        internalListener: []

    def currentDirectory(self):
        os.getcwd()
        pass

    def properties(self):
        experimentName: str = 'noname'
        parameters = struct.pack('PatchSize', 19, ...,
                                 'RatioCurveWindowWidth', 20, ...,
                                 'LogPolarPoolingBands', 5, ...,
                                 'CartesianPoolingBands', 3, ...,
                                 'PoolingCallback', max, ...,
                                 'LogPolarNormalization', 0, ...,  # it means dynamic
                                 'CartesianNormalization', 100, ...,
                                 'CartesianFeatures', True, ...,
                                 'LogPolarFeatures', True, ...,
                                 'DictionarySize', 50, ...,
                                 'PoolingShifts', 4, ...,
                                 'SVMMatrixNormalization', 'zscore', ...,
                                 'Fast', False, ...,
                                 'CacheDirectory', print(self.currentDirectory), ...,
                                 'Autosave', True, ...,
                                 'SVR_OPT', struct.pack('C', 1, 'gamma', 0.003, 'epsilon', 1), ...,
                                 'RF_OPT', struct.pack('NumTrees', 100, 'MinLeafSize', 5), ...,
                                 'CategoricalField', 'Group', ...,
                                 'Fields', 'ProjectedLeafArea', ...,
                                 'TimeFeature', '')  # unix - delta

    def leafCounting(self,Dataset,Name):
        Dataset = self.Dataset
        if 'Name' in locals():
            self.properties.experimentName = Name
        internalListener: object = listener(object, 'ComputationInProgress', )
    # Not finished