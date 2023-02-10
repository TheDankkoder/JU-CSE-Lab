def createFrame(data):
	countOnes = 0
	for ch in data:
		if ch == '1':
			countOnes += 1
	data += str(countOnes%2)
	return data


def extractMessage(frame):
	endidx = -1
	for i in range(len(frame)-1):
		if frame[i] == '/' and endidx == -1:
			endidx = i 
			break
	return frame[:endidx]
	
def extractCount(frame):
	startidx = -1
	endidx = -1
	for i in range(len(frame)-1):
		if frame[i] == '/':
			if startidx == -1:
				startidx = i+1
			else:
				endidx = i
	cnt = frame[startidx:endidx]
	return int(cnt)
	
def extractStatus(frame):
	count = 0
	startidx = -1
	for i in range(len(frame)-1):
		if frame[i] == '/':
			count += 1
		if count == 2 and startidx == -1:
			startidx = i+1
			break
	return frame[startidx:]
