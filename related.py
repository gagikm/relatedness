import numpy
import random

n = 5000

snp1 = [None]*n
	
for i in range(n):
	snp1[i]=random.randint(0,2)

snp2 = [None]*n

for i in range(n):
	num = random.randint(0,1)
	if(num == 0):
		snp2[i]=snp1[i]
	else:
		if (snp1[i] == 1):			
			num = random.randint(0,1)
			if(num == 0):
				snp2[i] = 0
			else:
				snp2[i] = 2
 		elif (snp1[i] == 2):
			num = random.randint(0,1)
			if(num == 0):
				snp2[i] = 0
			else:
				snp2[i] = 1
		elif (snp1[i] == 0):
			num = random.randint(0,1)
			if(num == 0):
				snp2[i] = 1
			else:
				snp2[i] = 2

def baseline(n, snp1, snp2):
	nf = float(n)
	counter = 0
	for i in range(n):
		if (snp1[i] == snp2[i]):
			counter = counter + 1

	similar = counter/nf
	if(similar >= 0.48 and similar <= 0.52 ):
		print "Base: Related."
	else:
		print "Base: Unrelated."

	# 1 2 0 1 1	(j)
 # 1  
 # 0
 # 2
 # 1
 # 1
 # (i)

p = 0.01
def relatedness(snp1, snp2):


	unrelated = [[0 for x in range(3)] for x in range(3)]
	unrelated[0][0] = (1-p)**2 * (1-p)**2
	unrelated[0][1] = (1-p)**2 * 2 * p * (1-p)
	unrelated[1][1] = (4*(p**2))*((1-p)**2)
	unrelated[2][2] = (p**2) * (p**2)
	unrelated[2][1] = (p**2) * 2 * p * (1-p)
	unrelated[2][0] = (p**2) * (1-p)**2
	print unrelated[0][0] + 2*unrelated[0][1] + unrelated[1][1] + unrelated[2][2] + 2*unrelated[2][1]
	ur_count = 0
	for i in range(len(snp1)):
		for j in range(len(snp2)):
			if(snp1[i] == 1):
				if(snp2[j] == 1):
					ur_count += unrelated[1][1]
				elif(snp2[j] == 0):
					ur_count += unrelated[0][1]
				elif(snp2[j] == 2):
					ur_count += unrelated[2][1]

			elif(snp1[i] == 2):
				if(snp2[j] == 1):
					ur_count += unrelated[2][1]
				elif(snp2[j] == 0): 
					ur_count += unrelated[2][0]
				elif(snp2[j] == 2):
					ur_count += unrelated[2][2]

			elif(snp1[i] == 0):
				if(snp2[j] == 1):
					 ur_count += unrelated[0][1]
				elif(snp2[j] == 2):
					 ur_count += unrelated[2][0]
				elif(snp2[j] == 0):
					 ur_count += unrelated[0][0]


	related = [[0 for x in range(3)] for x in range(3)]
	related[0][0] = ((1-p)**2 * (1-p)**2) + 2*0.25*((1-p)**2 * 2 * p * (1-p)) + 0.0625*(4*(p**2))*((1-p)**2)
	related[0][1] = 2*.25*((1-p)**2 * 2 * p * (1-p))+0.125*(4*(p**2))*((1-p)**2)
	related[1][1] = 0.25*(4*(p**2))*((1-p)**2)+2*.25*((p**2) * 2 * p * (1-p))+2*.25*((1-p)**2 * 2 * p * (1-p))+2*((p**2) * (1-p)**2)
	related[2][2] = ((p**2) * (p**2)) + (.0625*(4*(p**2))*((1-p)**2))+2*.25*((p**2) * 2 * p * (1-p))
	related[2][1] = 2*.25*((p**2) * 2 * p * (1-p))+.125*(4*(p**2))*((1-p)**2)
	related[2][0] = .0625*(4*(p**2))*((1-p)**2)

	print related[0][0] + 2*related[0][1] + related[1][1] + related[2][2] + 2*related[2][1]
	r_count = 0
	for i in range(len(snp1)):
		for j in range(len(snp2)):
			if(snp1[i] == 1):
				if(snp2[j] == 1):
					r_count += related[1][1]
				elif(snp2[j] == 0):
					r_count += related[0][1]
				elif(snp2[j] == 2):
					r_count += related[2][1]

			elif(snp1[i] == 2):
				if(snp2[j] == 1):
					r_count += related[2][1]
				elif(snp2[j] == 0): 
					r_count += related[2][0]
				elif(snp2[j] == 2):
					r_count += related[2][2]

			elif(snp1[i] == 0):
				if(snp2[j] == 1):
					 r_count += related[0][1]
				elif(snp2[j] == 2):
					 r_count += related[2][0]
				elif(snp2[j] == 0):
					 r_count += related[0][0]

	if(r_count > ur_count):
		print "Alt: Related."
	else:
		print "Alt: Unrelated."
	print "r_count: "; print r_count;
	print "ur_count: "; print ur_count;

baseline(n, snp1, snp2)
relatedness(snp1, snp2)
