from pyvi import ViTokenizer
from bs4 import BeautifulSoup
from underthesea import word_tokenize
import os

path = "./data/"
path_file = os.listdir(path)
# check html in raw text file

# j = 0
# for i in path_file:
# 	j+=1
# 	print(j)
# 	p = path+i
# 	with open(p,"r") as f:
# 		data = f.read()
# 		data = data.split('\n')[1:]
# 		data = ''.join(str(e) for e in data)
# 		if bool(BeautifulSoup(data, "html.parser").find()):
# 			print(p)

#remove stopwords
def remove_stopwords():
	with open('vietnamese-stopwords.txt', 'r') as f:
		list_stopwords = f.read().split('\n')
	cnt = 0
	for i in path_file:
		cnt += 1
		p = path + i
		with open(p, "r") as f:
			data = f.read()
			link, data = data.split('\n')[0], data.split('\n')[1:]
			data = ' '.join(str(e) for e in data)
			data = data.split(' ')
			temp = []
			for w in data:
				if w not in list_stopwords:
					temp.append(w)
			data = ' '.join(str(e) for e in temp)
			preprocessing_file = './preprocessing_data/' + i
			with open(preprocessing_file, 'w') as write:
				write.write(link + '\n')
				write.write(data)
			print('Saved new file' + preprocessing_file + ' after preprocessing !')
	print("No of saved doc : " + str(cnt))

#Tokenize
def tokenize(doc):
	with open(doc,'r') as f:
		data = f.read()
		link,data = data.split('\n')[0],data.split('\n')[1:]
		data = ' '.join(str(e) for e in data)
		return word_tokenize(data)	


