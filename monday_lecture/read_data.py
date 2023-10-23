import numpy as np

def read_grades(filename):
    '''
    Read grades data from text file,
    return Numpy array.
    '''
    grades = np.loadtxt('grades.txt', delimiter=',')
    return grades