from math import log
import math

log2 = lambda x: log(x, 2)

def Unary(x):
	return (x-1)*'0'+'1'

def Binary(x, l = 1):
	s = '{0:0%db}' % l
	return s.format(x)
	
def Elias_Gamma(x):
	if(x == 0):
		return '0'
	n = 1 + int(log2(x))
	b = x - 2**(int(log2(x)))
	l = int(log2(x))
	return Unary(n) + Binary(b, l)

def Elias_Gamma_Decoding(x):
    x = list(x)
    K = 0
    while True:
        if not x[K] == '0':
            break
        K = K + 1
    x = x[K:2*K+1]
    n = 0
    x.reverse()
    for i in range(len(x)):
        if x[i] == '1':
            n = n+math.pow(2, i)
    return int(n)

print("Elias - Gamma Encoding and Decoding:\n")
heading = '{:<20}  {:<12}  {:<8}'.format("x(ranging[1-20])", "Encoding", "Decoding")
print("\033[4m"+heading+"\033[0m")
for x in range(2,21,2):
    string = str(Elias_Gamma(x))
    line_new = '{:<20}  {:<12}  {:>8}'.format("For x = " + str(x), string, Elias_Gamma_Decoding(string))
    print(line_new)


