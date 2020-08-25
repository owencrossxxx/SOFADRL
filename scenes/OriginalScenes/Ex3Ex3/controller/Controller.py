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
tmax = 1

class controller(Sofa.PythonScriptController):

    def initGraph(self, node):

            self.node = node
            self.pneu1Node=self.node.getChild('pneu1')
            self.pneu2Node=self.node.getChild('pneu2')
            self.pressureConstraint1Node = self.pneu1Node.getChild('cavity')

            # create pointer towards the MechanicalObject
            self.myMechanicalObjectPointer1 = self.pneu1Node.getObject('tetras')

            self.pressureConstraint2Node = self.pneu2Node.getChild('cavity')

            # create pointer towards the MechanicalObject
            self.myMechanicalObjectPointer2 = self.pneu2Node.getObject('tetras')

    def onBeginAnimationStep(self, dt):
        #do whatever you want at the beginning of the step
        global t
        global pressureValue1
        global myMOpositions1
        global pressureValue2
        global myMOpositions2

        t = self.pneu1Node.findData('time').value
        incr = t*1000.0;

        self.MecaObject1=self.pneu1Node.getObject('tetras');
        self.pressureConstraint1 = self.pressureConstraint1Node.getObject('SurfacePressureConstraint')

        myMOpositions1 = self.myMechanicalObjectPointer1.findData('position').value
        pressureValue1 = self.pressureConstraint1.findData('value').value[0][0]

        self.MecaObject2=self.pneu2Node.getObject('tetras');
        self.pressureConstraint2 = self.pressureConstraint2Node.getObject('SurfacePressureConstraint')

        myMOpositions2 = self.myMechanicalObjectPointer2.findData('position').value
        pressureValue2 = self.pressureConstraint2.findData('value').value[0][0]


    def onKeyPressed(self,c):
            self.dt = self.node.findData('dt').value
            incr = self.dt*1000.0;

            self.MecaObject1=self.pneu1Node.getObject('tetras');

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


            self.pressureConstraint2 = self.pressureConstraint2Node.getObject('SurfacePressureConstraint')

            if (c == "."):
                pressureValue = self.pressureConstraint2.findData('value').value[0][0] + 0.01
                if pressureValue > 0.1:
                    pressureValue = 0.1
                self.pressureConstraint2.findData('value').value = str(pressureValue)

            if (c == ","):
                pressureValue = self.pressureConstraint2.findData('value').value[0][0] - 0.01
                if pressureValue < -0.1:
                    pressureValue = -0.1
                self.pressureConstraint2.findData('value').value = str(pressureValue)

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

        p.append(pressureValue1)
        x.append(t)
        y.append(myMOpositions1[5783][0])

        """
        if t>= tmax:
            self.pneu1Node.getRootContext().animate = False

            plt.figure()

            plt.subplot(211)
            plt.plot(x, y)
            plt.yscale('linear')
            plt.ylabel('Displacement/mm')
            plt.grid(True)

            #l = [2*x for x in p]
            plt.subplot(212)
            plt.plot(x, p)
            plt.yscale('linear')
            plt.ylabel('Pressure/MPa')
            plt.xlabel('time')
            plt.grid(True)


            plt.show()
        """

        return 0
