# -*- coding: utf-8 -*-
import os
import imp
import platform
from sys import argv

#   STLIB IMPORT
try:
	from stlib.scene.wrapper import Wrapper
except:
    raise ImportError("ModelOrderReduction plugin depend on SPLIB"\
                     +"Please install it : https://github.com/SofaDefrost/STLIB")

# MOR IMPORT
from mor.utility import sceneCreation as u

slash = '/'
if "Windows" in platform.platform():
    slash = "\\"

# Our Original Scene IMPORT
originalScene = r'/home/owen/Softwares/ext_plugin_repo/SoftRobots/Simulation/Ex3_MOR/Ex3.pyscn'
originalScene = os.path.normpath(originalScene)
originalScene = imp.load_source(originalScene.split(slash)[-1], originalScene)

paramWrapper = ('/pneu', {'paramForcefield': {'periodSaveGIE': 6, 'prepareECSW': True, 'modesPath': '/home/owen/Softwares/ext_plugin_repo/SoftRobots/Simulation/Ex3_MOR/MOR_Results/data/modes.txt', 'nbTrainingSet': 5}, 'paramMORMapping': {'input': '@../MechanicalObject', 'modesPath': '/home/owen/Softwares/ext_plugin_repo/SoftRobots/Simulation/Ex3_MOR/MOR_Results/data/modes.txt'}, 'paramMappedMatrixMapping': {'object1': '@./MechanicalObject', 'object2': '@./MechanicalObject', 'template': 'Vec1d,Vec1d', 'timeInvariantMapping2': True, 'performECSW': False, 'timeInvariantMapping1': True, 'nodeToParse': '@./pneu'}})

def createScene(rootNode):

    if (len(argv) > 1):
        stateFileName = str(argv[1])
    else:	
        stateFileName="stateFile.state"
    originalScene.createScene(rootNode)

    path , param = paramWrapper
    pathToNode = path[1:]

    u.createDebug(rootNode,pathToNode,stateFileName)