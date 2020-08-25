#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Sofa
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

x = []
y = []
p = []
#tmax = 1

class controller(Sofa.PythonScriptController):

    def initGraph(self, node):

            self.node = node
            self.pneuNode=self.node.getChild('pneu')
            self.pressureConstraint1Node = self.pneuNode.getChild('cavity')

            # create pointer towards the MechanicalObject
            self.myMechanicalObjectPointer = self.pneuNode.getObject('tetras')

    def onBeginAnimationStep(self, dt):
        #do whatever you want at the beginning of the step
        global t
        global pressureValue
        global myMOpositions

        t = self.pneuNode.findData('time').value
        incr = t*1000.0;

        self.MecaObject1=self.pneuNode.getObject('tetras');
        self.pressureConstraint1 = self.pressureConstraint1Node.getObject('SurfacePressureConstraint')

        myMOpositions = self.myMechanicalObjectPointer.findData('position').value
        pressureValue = self.pressureConstraint1.findData('value').value[0][0]

        #DRL Patch communication
        



    def onKeyPressed(self,c):
            self.dt = self.node.findData('dt').value
            incr = self.dt*1000.0;

            self.MecaObject1=self.pneuNode.getObject('tetras');

            self.pressureConstraint1 = self.pressureConstraint1Node.getObject('SurfacePressureConstraint')

            if (c == "="):
                pressureValue = self.pressureConstraint1.findData('value').value[0][0] + 0.01
                if pressureValue > 0.1:
                    pressureValue = 0.1
                self.pressureConstraint1.findData('value').value = str(pressureValue)

            if (c == "-"):
                pressureValue = self.pressureConstraint1.findData('value').value[0][0] - 0.01
                if pressureValue < -0.1:
                    pressureValue = -0.1
                self.pressureConstraint1.findData('value').value = str(pressureValue)

            #p.append(pressureValue)

    #called on each animation step
    #def onBeginAnimationStep(self, dt):
        #do whatever you want at the beginning of the step
        #t = self.rootNode.findData('time').value
        #return 0

    #called on each animation step
    def onEndAnimationStep(self, dt):

        # print the first value of the DOF 0 (Vec3 : x,y,z) x[0] y[0] z[0]
        #print str(t)
        #print str(myMOpositions[5783][0])+' '+str(myMOpositions[5783][1])+' '+str(myMOpositions[5783][2])

        p.append(pressureValue)
        x.append(t)
        y.append(myMOpositions[23][0])

        #print 'current state :', myMOpositions[23][0]


        return 0
