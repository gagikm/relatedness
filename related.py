import numpy
import random
from time import time

result = ""
n = 1000000
print n
# def test():
father = ([None]*n, [None]*n)
mother = ([None]*n, [None]*n)

fp = [None]*n
mp = [None]*n


s1g = ([None]*n, [None]*n)
s2g = ([None]*n, [None]*n)

s1p = [None]*n
s2p = [None]*n

for i in range(n):
	father[0][i]=random.randint(0,1)
	father[1][i]=random.randint(0,1)
	mother[0][i]=random.randint(0,1)
	mother[1][i]=random.randint(0,1)

	num1 = random.randint(0,1)
	if(num1 == 0):
		s1g[0][i] = father[0][i]
		s1g[1][i] = mother[1][i]
	else:
		s1g[0][i] = mother[0][i]
		s1g[1][i] = father[1][i]

	num2 = random.randint(0,1)
	if(num2 == 0):
		s2g[0][i] = father[0][i]
		s2g[1][i] = mother[1][i]
	else:
		s2g[0][i] = mother[0][i]
		s2g[1][i] = father[1][i]

	if(s1g[0][i] == 1):
		if(s1g[1][i] == 1):
			s1p[i] = 1
		elif(s1g[1][i] == 0):
			s1p[i] = 2
		else:
			print "break1"

	elif(s1g[0][i] == 0):
		if(s1g[1][i] == 1):
			s1p[i] = 2
		elif(s1g[1][i] == 0): 
			s1p[i] = 0
		else:
			print "break2"
	else:
		print "break12"

	if(s2g[0][i] == 1):
		if(s2g[1][i] == 1):
			s2p[i] = 1
		elif(s2g[1][i] == 0):
			s2p[i] = 2
		else:
			print "break3"

	elif(s2g[0][i] == 0):
		if(s2g[1][i] == 1):
			s2p[i] = 2
		elif(s2g[1][i] == 0): 
			s2p[i] = 0
		else:
			print "break4"
	else:
		print "break11"


for i in range(n):
	if(father[0][i] == 1):
		if(father[1][i] == 1):
			fp[i] = 1
		elif(father[1][i] == 0):
			fp[i] = 2
		else:
			print "break5"

	elif(father[0][i] == 0):
		if(father[1][i] == 1):
			fp[i] = 2
		elif(father[1][i] == 0): 
			fp[i] = 0
		else:
			print "break6"
	else:
		print "break10"

for i in range(n):
	if(mother[0][i] == 1):
		if(mother[1][i] == 1):
			mp[i] = 1
		elif(mother[1][i] == 0):
			mp[i] = 2
		else:
			print "break7"

	elif(mother[0][i] == 0):
		if(mother[1][i] == 1):
			mp[i] = 2
		elif(mother[1][i] == 0): 
			mp[i] = 0
		else:
			print "break8"
	else:
		print "break9"

#print fp
#print mp
counter = 0.
for i in range(n):
 	if(fp[i] == mp[i]):
 		counter += 1

# print counter/n

def baseline(n, snp1, snp2):
	nf = float(n)
	counter = 0
	for i in range(n):
		if (snp1[i] == snp2[i]):
			counter = counter + 1

	similar = counter/nf
	#print similar
	global result
	if(similar >= 0.65):
		# print "Baseline Result: Related."
		result = "related"
	else:
		# print "Baseline Result: Unrelated."
		result = "unrelated"


p = 0.3
def relatedness(snp1, snp2):
	unrelated = [[0 for x in range(3)] for x in range(3)]
	unrelated[0][0] = (1-p)**4
	unrelated[0][1] = (1-p)**2 * 2 * p * (1-p)
	unrelated[1][1] = (4*(p**2))*((1-p)**2)
	unrelated[2][2] = (p**4)
	unrelated[2][1] = (p**2) * 2 * p * (1-p)
	unrelated[2][0] = (p**2) * ((1-p)**2)
	# print unrelated[0][0] + 2*unrelated[0][1] + 2*unrelated[2][0] + unrelated[1][1] + 2*unrelated[2][1] + unrelated[2][2]

	ur_count = 0
	for i in range(len(snp1)):
		if(snp1[i] == 1):
			if(snp2[i] == 1):
				ur_count = ur_count +  unrelated[1][1]
			elif(snp2[i] == 0):
				ur_count = ur_count +  unrelated[0][1]
			elif(snp2[i] == 2):
				ur_count = ur_count +  unrelated[2][1]

		elif(snp1[i] == 2):
			if(snp2[i] == 1):
				ur_count = ur_count +  unrelated[2][1]
			elif(snp2[i] == 0): 
				ur_count = ur_count +  unrelated[2][0]
			elif(snp2[i] == 2):
				ur_count = ur_count +  unrelated[2][2]

		elif(snp1[i] == 0):
			if(snp2[i] == 1):
				 ur_count = ur_count +  unrelated[0][1]
			elif(snp2[i] == 2):
				 ur_count = ur_count +  unrelated[2][0]
			elif(snp2[i] == 0):
				 ur_count = ur_count +  unrelated[0][0]


		else:
			print "WHY AM I HERE"
	ur_count += .01*n

	related = [[0 for x in range(3)] for x in range(3)]
	related[0][0] = unrelated[0][0] + 2*0.25*unrelated[0][1] + 0.0625*unrelated[1][1]
	related[0][1] = 2*.25*unrelated[0][1] + .125*unrelated[1][1]
	related[1][1] = 0.25*unrelated[1][1] + 2*.25*unrelated[2][1] + 2*.25*unrelated[0][1] + 2*unrelated[2][0]
	related[2][2] = unrelated[1][1]*.0625 + unrelated[2][2] + 2*.25*unrelated[2][1]
	related[2][1] = 2*.25*unrelated[2][1] + 0.125*unrelated[1][1]
	related[2][0] = .0625*unrelated[1][1]

	# print related[0][0] + 2*related[0][1] + 2*related[2][0] + related[1][1] + 2*related[2][1] + related[2][2]

	r_count = 0
	for i in range(len(snp1)):
		if(snp1[i] == 1):
			if(snp2[i] == 1):
				r_count = r_count +  related[1][1]
			elif(snp2[i] == 0):
				r_count = r_count +  related[0][1]
			elif(snp2[i] == 2):
				r_count = r_count +  related[2][1]


		elif(snp1[i] == 2):
			if(snp2[i] == 1):
				r_count = r_count +  related[2][1]
			elif(snp2[i] == 0): 
				r_count = r_count +  related[2][0]
			elif(snp2[i] == 2):
				r_count = r_count +  related[2][2]

		elif(snp1[i] == 0):
			if(snp2[i] == 1):
				 r_count = r_count +  related[0][1]
			elif(snp2[i] == 2):
				 r_count = r_count +  related[2][0]
			elif(snp2[i] == 0):
				 r_count = r_count +  related[0][0]

		else:
			print "WHY AM I HERE 2"
	
	global result
	if(r_count > ur_count):
		# print "Alternate Result: Related."
		result = "related"
	else:
		# print "Alternate Result: Unrelated."
		result = "unrelated"
	# print "r_count: "; print r_count;
	# print "ur_count: "; print ur_count;


# print "Two individuals that we know are UNRELATED."
# baseline(n, fp, mp);	 
# relatedness(fp, mp);

t = time()

# print"\n"
# print "Two individuals that we know are RELATED."
# baseline(n, s1p, s2p) 
relatedness(s1p, s2p)

tt = time() - t
print tt


# times = 1
# r = 0.
# u = 0.
# for i in range(times):
	# test()
# 	if (result == "unrelated"):
# 		u += 1
# 	elif(result == "related"):
# 		r += 1
# 	else:
# 		print "error"
# print "Returned with result:"
# u_pct = 100*(u/times)
# r_pct = 100*(r/times)
# print "Unrelated: %d (%f%%)" % (u, u_pct)
# print "Related: %d (%f%%)" % (r, r_pct)

