import pytest
import math
import numpy as np

def chemeq(Kd, Ca0, Cb0):
    Cab = 0.5*(Ca0 + Cb0 + Kd - sqrt(((Ca0 + Cb0 + Kd)**2) - 4*Ca0*Cb0)
    Ca = Ca0 - Cab
    Cb = Cb0 - Cab
    
