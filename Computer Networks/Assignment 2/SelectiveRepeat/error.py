def checkError(frame):
	countOnes = 0
	for ch in frame:
		if ch == '1':
			countOnes += 1
	return countOnes%2