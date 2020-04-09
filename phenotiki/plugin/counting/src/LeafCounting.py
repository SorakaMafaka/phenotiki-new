from typing import List, Any
import os  # Used to get absolute current working directory
import numpy


class LeafCounting:
    def __init__(self):
        self.properties()  # Transient doesn't exist in Python, TODO: https://stackoverflow.com/questions/6313421/can-i-mark-variables-as-transient-so-they-wont-be-pickled
        dataset = {} # Not sure if correct?
        internalListener: []

    def currentDirectory(self):
        os.getcwd()
        pass

    def properties(self):
        global parameters
        experimentName: str = 'noname'
        parameters = {'PatchSize': 19,
                                 'RatioCurveWindowWidth': 20,
                                 'LogPolarPoolingBands': 5,
                                 'CartesianPoolingBands': 3,
                                 'PoolingCallback': max,
                                 'LogPolarNormalization': 0,  # it means dynamic
                                 'CartesianNormalization' : 100,
                                 'CartesianFeatures' : True,
                                 'LogPolarFeatures': True,
                                 'DictionarySize' : 50,
                                 'PoolingShifts' : 4,
                                 'SVMMatrixNormalization' : 'zscore',
                                 'Fast': False,
                                 'CacheDirectory': print(self.currentDirectory),
                                 'Autosave': True,
                                 'SVR_OPT' : {'C' : 1, 'gamma' : 0.003, 'epsilon' : 1},
                                 'RF_OPT' : {'NumTrees' : 100, 'MinLeafSize' : 5},
                                 'CategoricalField' : 'Group',
                                 'Fields' : 'ProjectedLeafArea',
                                 'TimeFeature' : ''}  # unix - delta

    ## Matts function
    def leafCounting(self,Dataset,Name):
        Dataset = self.Dataset
        if 'Name' in locals():
            self.properties.experimentName = Name
        internalListener: object = listener(object, 'ComputationInProgress', )
    # Not finished

    ## Extract Patches
    def extractingImagePatches(self, index):
        ##LogPolar Reprocessing#
        if (not parameters['Fast'])
            ##progress update
            progressUpdate('LeafCountingTrain', 1/8*100, 'Logpolar reprocessing')
            if parameters['LogPolarFeatures']:
                self.computeLogPolarPreprocessing(index)

    def computeLogPolarPreprocessing(self, index):
        N = len(index)
        Pathsize = parameters['PatchSize']
        resp_curve_width = parameters['RatioCurveWindowWidth']
        D = parameters['LogPolarNormalization']

        for x in index

    def patchClustering(self, F_lp, F_c): #Start clustering


        # End clustering