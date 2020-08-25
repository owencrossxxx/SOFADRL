#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Sofa
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import csv

x = []
y = []
p = []

tmax = 1

class controller(Sofa.PythonScriptController):

    def initGraph(self, node):

        self.node = node
        self.pneu1Node=self.node.getChild('pneu1')
        self.pressureConstraint1Node = self.pneu1Node.getChild('cavity')

        # create pointer towards the MechanicalObject
        self.myMechanicalObjectPointer = self.pneu1Node.getObject('tetras')
        self.count = 0

    def onBeginAnimationStep(self, dt):
        #do whatever you want at the beginning of the step
        global t
        global pressureValue
        global myMOpositions
    

        t = self.pneu1Node.findData('time').value
        incr = t*1000.0

        self.MecaObject1=self.pneu1Node.getObject('tetras')
        self.pressureConstraint1 = self.pressureConstraint1Node.getObject('SurfacePressureConstraint')

        myMOpositions = self.myMechanicalObjectPointer.findData('position').value
        pressureValue = self.pressureConstraint1.findData('value').value[0][0]



        if t > 0.5:
            self.forcefield = self.pneu1Node.getObject('FEM')
            self.forcefield.findData('youngModulus').value = 100000000

        #DRL Patch communication
        



    #def onKeyPressed(self,c):
            #self.dt = self.node.findData('dt').value
            #incr = self.dt*1000.0;

            #self.MecaObject1=self.pneu1Node.getObject('tetras');

            #self.pressureConstraint1 = self.pressureConstraint1Node.getObject('SurfacePressureConstraint')

            #if (c == "="):
              #  pressureValue = self.pressureConstraint1.findData('value').value[0][0] + 0.01
               # if pressureValue > 0.1:
                #    pressureValue = 0.1
                #self.pressureConstraint1.findData('value').value = str(pressureValue)

            #if (c == "-"):
             #   pressureValue = self.pressureConstraint1.findData('value').value[0][0] - 0.01
              #  if pressureValue < -0.1:
               #     pressureValue = -0.1
                #self.pressureConstraint1.findData('value').value = str(pressureValue)

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
        #pressureValue = self.pressureConstraint1.findData('value').value[0][0]

        #self.count += 1

#        if self.count >= 30:
 #           pressureValue = self.pressureConstraint1.findData('value').value[0][0]
  ##          myMOpositions = self.myMechanicalObjectPointer.findData('position').value
    #        self.count = 0
     #       if pressureValue <= 0.04 and pressureValue >= 0:
      #          pressureValue += 0.005
       #     elif pressureValue > 0.04:
        #        #pressureValue = 0
         #       pressureValue = -0.005
          #  else:
           #     pressureValue -= 0.005

            #print(pressureValue)
            #self.pressureConstraint1.findData('value').value = str(pressureValue)
            #p.append(pressureValue)
            #x.append(t)
            #y.append(myMOpositions[23][0])

            print (pressureValue)


        #if pressureValue < -0.015:
            #self.pneu1Node.getRootContext().animate = False
            #a = [x,p,y]
            #with open("output.csv", "wb") as f:
             #   writer = csv.writer(f)
              #  writer.writerows(a)






        #print 'current state :', myMOpositions[23][0]

        #if t>= tmax:
            #self.pneu1Node.getRootContext().animate = False

            #plt.figure()

            #plt.subplot(211)
            #plt.plot(x, y)
            #plt.yscale('linear')
            #plt.ylabel('Displacement/mm')
            #plt.grid(True)

            #l = [2*x for x in p]
            #plt.subplot(212)
            #plt.plot(x, p)
            #plt.yscale('linear')
            #plt.ylabel('Pressure/MPa')
            #plt.xlabel('time')
            #plt.grid(True)


            #plt.show()

    #return 0
