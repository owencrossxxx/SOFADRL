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

x = []
y = []
p = []
tmax = 30000
#i = 1



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
        global t
        global pressureValue
        global myMOpositions

        
        # incr = t*1000.0

        self.MecaObject1 = self.pneu1Node.getObject('tetras')
        self.pressureConstraint1 = self.pressureConstraint1Node.getObject(
            'SurfacePressureConstraint')

        self.i += 1

        if self.i>20:
            self.rand = random.uniform(-0.03, 0.03)
            self.i = 0
            t = self.pneu1Node.findData('time').value
            pressureValue = self.pressureConstraint1.findData('value').value[0][0]
            myMOpositions = self.myMechanicalObjectPointer.findData('position').value
            self.pressureConstraint1.findData('value').value = str(self.rand) 
            self.switch = 1    
        
        

    # called on each animation step

    def onEndAnimationStep(self, dt):

        #time.sleep(.05)
        # print the first value of the DOF 0 (Vec3 : x,y,z) x[0] y[0] z[0]
        # print str(t)
        # print str(myMOpositions[5783][0])+' '+str(myMOpositions[5783][1])+' '+str(myMOpositions[5783][2])
        if self.switch == 1:
            p.append(pressureValue)
            x.append(t)
            y.append(myMOpositions[75][0])
            self.switch = 0

        # print 'current state :', myMOpositions[23][0]

        self.it += 1

        if self.it> 500000:
            with open('pressurevsposition_break.csv', 'wb') as f:
                wr = csv.writer(f)
                mylist = [x,y,p]
                array = np.array(mylist)
                transpose = array.T
                mylist = transpose.tolist()
                wr.writerows(mylist)

        #print(self.it)
        if self.it> 1000000:
            self.pneu1Node.getRootContext().animate = False
            with open('pressurevsposition.csv', 'wb') as f:
                wr = csv.writer(f)
                mylist = [x,y,p]
                array = np.array(mylist)
                transpose = array.T
                mylist = transpose.tolist()
                wr.writerows(mylist)

        return 0
