import numpy.random as r
from sys import argv

SEED = float(argv[1])
NUM_CALLS = int(argv[2])

calls = []

def seed():
	r.seed(SEED)