#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Sofa
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import csv
import random
import time
import numpy as np
import socket
#import pandas as pd

x = []
y = []
p = []
#i = 1

sock = socket.socket()
port = 12345
sock.bind(('', port))
sock.listen(5)
c, addr = sock.accept()
print "Socket Up and running with a connection from", addr



class controller(Sofa.PythonScriptController):

    def initGraph(self, node):

            self.node = node
            self.ReduceNode = self.node.getChild('Reduced_test')
            self.ModelNode = self.ReduceNode.getChild('pneu_MOR')
            self.pneu1Node = self.ModelNode.getChild('pneu')
            self.pressureConstraint1Node = self.pneu1Node.getChild('cavity')
            self.i = 0
            self.rand = 0
            self.it = 0
            self.switch = 0
            # create pointer towards the MechanicalObject
            self.myMechanicalObjectPointer = self.pneu1Node.getObject('tetras')
            # self.pneu1Node.getObject('FEM').findData('youngModulus').value = 100000000000

    def onBeginAnimationStep(self, dt):
        # do whatever you want at the beginning of the step
        global pressureValue
        global myMOpositions
        
        
        # incr = t*1000.0

        self.MecaObject1 = self.pneu1Node.getObject('tetras')
        self.pressureConstraint1 = self.pressureConstraint1Node.getObject(
            'SurfacePressureConstraint')

        if self.i == 0:
            
            rcvdData = c.recv(1024).decode()
    
            if str(rcvdData) == "reset":
                self.pneu1Node.reset()
            
            else:
                p = float(rcvdData)
                pressureValue = p
                self.pressureConstraint1.findData('value').value = str(pressureValue)
        
    

        if self.i == 20:

            myMOpositions = self.myMechanicalObjectPointer.findData('position').value
            c.send(str(myMOpositions[75][0]).encode()) 

            self.i = -1
        
        self.i += 1

    # called on each animation step

