import os
path = "./topic/"
path_file = os.listdir(path)
for i in path_file:
	p = path+i
	if os.path.getsize(p) == 0:
		os.remove(p)
path_file = os.listdir(path)
print('There are '+str(len(path_file))+" topics.")