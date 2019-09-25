from matplotlib import pyplot as plt
import os

path = './topic/'
path_topic = os.listdir(path)
list_topic = []
list_no_doc = []
for topic in path_topic:
	p = path+topic
	num_lines = sum(1 for line in open(p))
	list_topic.append(topic[:-4])
	list_no_doc.append(num_lines)
for i in range(len(list_no_doc)):
	print(list_topic[i]+" "+str(list_no_doc[i]))
plt.pie(x=list_no_doc[:5],labels=list_topic[:5])
plt.show()
