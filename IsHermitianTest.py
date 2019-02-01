import seaborn as sns
import numpy as np 
from pylab import *
# import matplotlib.pyplot as pyplot

f = open("/home/qyang/GitAllProjects/TAD_3Dgenome/GM12878_chr22")
len_list = []
eps = 1e-5
first_line = True
cnt = 0
start = 2000
stop = 4000
for line in f.readlines():
	line = line.strip("\n")
	if (cnt < start or cnt >= stop):
		cnt = cnt + 1
		continue
	else:
		cnt = cnt + 1

	print('The %d  line:' % cnt)
	nums = line.split("\t")
	nums = [float(x) for x in nums]
	nums = nums[start:stop]
	# print (len([x for x in nums if x>eps]))
	
	if first_line:
		matrix = np.array(nums)
		# nonzero_distribution = np.array([x for x in nums if x>eps])
		first_line = False
	else:
		matrix = np.c_[matrix,nums]

		# nonzero_distribution = np.append(nonzero_distribution,[x for x in nums if x>eps])
	# len_list.append(len([x for x in nums if x>0.0001]))
print(matrix.size, cnt, np.max(matrix),np.min(matrix))
print(np.transpose(matrix) == matrix)



