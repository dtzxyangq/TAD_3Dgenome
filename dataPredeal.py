import seaborn as sns
import numpy as np 
from pylab import *
# import matplotlib.pyplot as pyplot

f = open("/home/qyang/GitAllProjects/TAD_3Dgenome/GM12878_chr22")
len_list = []
eps = 1e-5
first_line = True
cnt = 0
for line in f.readlines():
	line = line.strip("\n")
	cnt = cnt + 1
	print('The %d  line:' % cnt)
	nums = line.split("\t")
	nums = [float(x) for x in nums]
	# print (len([x for x in nums if x>eps]))
	for i in range(len(nums)):
		if nums[i]<100 and nums[i]>eps:
			nums[i] = 1
		else:
			if nums[i]<3000 and nums[i]>=100:
				nums[i] = 2
			else:
				if nums[i]>=3000:
					nums[i] = 3



	if first_line:
		matrix = np.array(nums)
		# nonzero_distribution = np.array([x for x in nums if x>eps])
		first_line = False
	else:
		matrix = np.c_[matrix,nums]
		# nonzero_distribution = np.append(nonzero_distribution,[x for x in nums if x>eps])
	# len_list.append(len([x for x in nums if x>0.0001]))
print(matrix.size, cnt, np.max(matrix),np.min(matrix))

cmap = sns.diverging_palette(200,20,sep=20,as_cmap=True)
sns.set()
sns.heatmap(matrix,cmap = cmap)

# nonzero_distribution =zeros(1000)
# plot(len_list,'o')
# hist(nonzero_distribution,3000,log =True)
savefig('./hist_bin_22_structure.png')
show()


