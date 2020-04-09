from typing import List, Any
import os  # Used to get absolute current working directory
import numpy as np
import math
from scipy.spatial.distance import cdist

from phenotiki.plugin.counting.src.PlantDataset import PlantDataset


class LeafCounting:
    def __init__(self):
        self.properties()  # Transient doesn't exist in Python, TODO: https://stackoverflow.com/questions/6313421/can-i-mark-variables-as-transient-so-they-wont-be-pickled
        self.dataset = PlantDataset() # Not sure if correct?
        self.internalListener: []

    def currentDirectory(self):
        os.getcwd()
        pass

    def properties(self):
        experimentName: str = 'noname'
        self.parameters = {'PatchSize': 19,
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
        if not self.parameters['Fast']:
            ##progress update
            progressUpdate('LeafCountingTrain', 1/8*100, 'Logpolar reprocessing')
            if self.parameters['LogPolarFeatures']:
                self.computeLogPolarPreprocessing(index)

    def computeLogPolarPreprocessing(self, index):
        N = len(index)
        Pathsize = self.parameters['PatchSize']
        resp_curve_width = self.parameters['RatioCurveWindowWidth']
        D = self.parameters['LogPolarNormalization']
        for x in range(0, N):
            #get plantindex in sequence
            [t, id] = self.dataset.getPlantIndex(x)
            #returns a dictionary with all the information needed for a specific subject
            T = self.dataset.getSample(t, id)
            #determin plants center
            self.dataset.Sequences[t].Subject[id].RelativeCenter = PlantDataset.getPlantCenter(T.FGMask);

            #Log Polar Transform Module
            I = T.RGB
            im = I[::2]
            center = T.RelativeCenter

            #Finding the optimum D parameters
            if D <=0 | D is not None:
                #returns two or three arguments
                [r, c, ] = PlantDataset.getContour(T.FGMask);
                const_coords = [r,c]
                #cdist replaces pdist2
                dist = cdist(center, const_coords)
                Dr = max(math.ceil(max(dist)), Pathsize)
            else:
                Dr = D

            #convert fg mask and green channel
            [fg_lg, ] = polartrans(T.FGMask, Dr, 360, np.double(center(2)), np.double(center(1)), 'log', 'full')
            fg_lg = np.uint8_t(round(fg_lg))
            lg = np.uint8_t(im, Dr, 360, np.double(center(2)), np.double(center(1)), 'log', 'full')
            lg = lg * fg_lg

            #storing
            self.dataset.Sequences[t].Subject[id].AdditionalData.polar.fg = fg_lg
            self.dataset.Sequences[t].Subject[id].AdditionalData.polar.green_ch = lg

            ###
            #Resp_curve submodule
            fg = self.dataset.Sequences[t].Subject[id].AdditionalData.polar.fg
            #not sure if this is right
            ratio = np.zeros(1, np.size(fg, 2))



    def patchClustering(self, F_lp, F_c): #Start clustering


        # End clustering