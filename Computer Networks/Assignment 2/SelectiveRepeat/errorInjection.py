import random

def injectRandomError(frame):
	pos = random.randint(0, len(frame)-1)
	frame = frame[:pos]+'1'+frame[pos+1:]
	return frame