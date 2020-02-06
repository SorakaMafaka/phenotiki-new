from typing import List, Any
import os  # Used to get absolute current working directory
import numpy
import wx
import struct


class LeafCounting():
    property()  # Transient doesn't exist in Python, TODO: https://stackoverflow.com/questions/6313421/can-i-mark-variables-as-transient-so-they-wont-be-pickled
    Dataset = struct  # Not sure if correct?
    InternalListener: []
    property


def currentDirectory(args):
    os.getcwd()
    pass


def properties():
    ExperimentName: str = 'noname'
    Parameters = struct('PatchSize', 19, ...,
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
                        'CacheDirectory', print(currentDirectory), ...,
                        'Autosave', True, ...,
                        'SVR_OPT', struct('C', 1, 'gamma', 0.003, 'epsilon', 1), ...,
                        'RF_OPT', struct('NumTrees', 100, 'MinLeafSize', 5), ...,
                        'CategoricalField', 'Group', ...,
                        'Fields', 'ProjectedLeafArea', ...,
                        'TimeFeature', '')  # unix - delta
