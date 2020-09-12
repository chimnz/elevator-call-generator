import numpy.random as r
from sys import argv

SEED = int(argv[1])			# initial seed value
NUM_CALLS = int(argv[2])	# number of elevator calls to generate

offset = 0 					# seed offset, increment by one every time number is generated
current_time = 0
calls = []

def reseed():
	global offset
	r.seed(SEED + offset)
	offset += 1

def gen_npass():
	reseed()
	N = r.lognormal()		# default values work: mean=0, standard_deviation=1
	if 0 < N <= 5:			# will never be less than 0, can be greater than 5
		N = round(N)
	else:
		N = 5
	return N

def gen_floor():			# generate random floor in range [1, 100]
	reseed()
	return r.randint(1, 101)

def gen_time():
	global current_time
	reseed()
	time_delta = r.uniform(0.0, 600.0)  # next call can occur between 0 and 600 seconds (10 min) after previous call
	current_time += time_delta
	return round(current_time, 2)		# round to two decimal places

for i in range(NUM_CALLS):
	###num_passengers = gen_npass()		# this is irrelevant for part A
	pos = gen_floor()
	dest = gen_floor()					# obvious pattern between pos and dest is caused by re-use of gen_floor function w/o fancy seed mutation
	time = gen_time()
	calls.append( (time, pos, dest)	)

for call in calls:
	print(call)