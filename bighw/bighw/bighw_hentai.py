__author__ = 'vigo@vigo.su'

import math
import getopt
import sys
import os
import fnmatch
import logging
from Gato import *
import Gato.GatoGlobals as GatoGlobals
g = GatoGlobals.AnimationParameters

f = open('input.txt','r')
data = f.readlines()
f.close()

w = open('graph.cat','w')


vertex = []

def is2pow(xxk):

    return (xxk==(2**int(math.log(xxk,2))))
def low2pow(xxk):
    if xxk>0:
        return int(math.log(xxk,2))
    return 0
def parentn(n):
    if n>0:
        return long((n+1)/2)-1
    return 0

def load_data():
    mylen = len(data)
    #some = low2pow(len(data))
    xx = 0
    yy = 1.0
    znak = 1;
    iid = 1
    some = low2pow(len(data))
    for i in xrange(0,len(data),1):
        somedata = []
        if i<1:
            somedata.append(data[i])
            somedata.append(0)
            somedata.append(0)
        else:
            somedata.append(data[i])
            x = int((vertex[parentn(i)][1]  + 10*((some-low2pow(i-1))*znak* (1.0/(low2pow(i+1))) )))
            somedata.append(x)
            somedata.append(100*(low2pow(i-1))+100)
            znak*=-1
            print somedata[2]




        vertex.append(somedata)

    w.write('graph:\n')
    w.write('dir:0; simp:1; eucl:1; int:0; ew:1; vw:0;\n')
    w.write('scroller:\n')
    w.write('vdim:1000; hdim:1000; vlinc:10; hlinc:10; vpinc:50; hpinc:50;\n')
    ver = 'vertices:'+str(len(vertex))+';\n'
    w.write(ver)
    for i in xrange(0,len(vertex),1):
        ss = 'n:'+str(i)+'; x:'+str(700+vertex[i][1])+str('; y:')+str(vertex[i][2])+';\n'
        w.write(ss)

    w.close()

load_data()
print low2pow(7)
print parentn(0)