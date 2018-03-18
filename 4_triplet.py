<<<<<<< HEAD
import math
for i in range(1,1000):
	for j in range(i+1,1000):
		for k in range(j+1,1000):
			if (math.pow(k,2)==math.pow(j,2)+math.pow(i,2))&(i+j+k==1000):
=======
import math
for i in range(1,1000):
	for j in range(i+1,1000):
		for k in range(j+1,1000):
			if (math.pow(k,2)==math.pow(j,2)+math.pow(i,2))&(i+j+k==1000):
>>>>>>> 317b9e4e9c1a3c343f1b0223fabe4bb3b114c96f
				print(i*j*k)