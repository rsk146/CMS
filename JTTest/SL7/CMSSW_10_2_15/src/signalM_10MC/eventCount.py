import ROOT
import os
from ROOT import *
from array import array
import math
from math import *
import sys
import glob
import csv
import files10
from files10 import *
def GET(E,B):
    return getattr(E,B)

sum = 0
for file in A:
    print file
    f = TFile(file)
    T = f.Get("Events")
    print type(T)
    a = T.GetBranch("GenEventInfoProduct_generator__SIM.present")
    sum += a.GetEntries()
    
