

def add(a, b):
		result = ""
		s = 0
		i = len(a)-1
		j = len(b)-1
		while i>=0 or j>=0 or s==1:
			if i>=0:
				s+=int(a[i])
			if j>=0:
				s+=int(b[j])
			result = str(s%2) + result
			s //= 2 
			i-=1
			j-=1
		return result

def xor(a, b):
		result = ""
		for i in range(1, len(b)):
			if a[i]==b[i]:
				result += '0'
			else:
				result += '1'
		return result

def divide(dividend, divisor):
		xorlen = len(divisor)
		temp = dividend[:xorlen]
		while len(dividend) > xorlen:
			if temp[0]=='1':
				temp=xor(divisor,temp)+dividend[xorlen]
			else:
				temp=xor('0'*xorlen,temp)+dividend[xorlen]
			xorlen += 1
		if temp[0]== '1':
			temp=xor(divisor,temp)
		else:
			temp=xor('0'*xorlen,temp)
		return temp
