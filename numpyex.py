import numpy as np

xa_high = np.loadtxt('data/xa_high_food.csv', comments="#")
xa_low = np.loadtxt('data/xa_low_food.csv', comments = '#')

def xa_to_diameter(xa):
    """converts area to diameter"""

    #Compute diameter
    diameter = np.sqrt(xa * 4 / np.pi)
    return diameter

A = np.array([[6.7, 1.3, 0.6, 0.7],
              [0.1, 5.5, 0.4, 2.4],
              [1.1, 0.8, 4.5, 1.7],
              [0.0, 1.5, 3.4, 7.5]])

B = np.array([1.1, 2.3, 3.3, 3.9])


def easy_reshape(obj, ncols, order = 'C'):
    """Guarantee that reshaping works by defining only one shape parameter"""
    arr = np.reshape(obj, ncols, (len(obj)/ncols), order)
    return arr
