def multiplyTuples(t1, t2):
	tup = []
	for i in range(len(t1)):
		tup.append(t1[i] * t2[i])

	return tup 
	
def multiplyScalar(t1, x):
    
	tup = []
	for i in range(len(t1)):
		tup.append(t1[i] * x)
	return tup
	
def addTuples(t1, t2):
	tup = []
	for i in range(len(t1)):
		tup.append(t1[i]+t2[i])
	return tup 		
