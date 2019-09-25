import preprocessing
import os
import sys
import numpy as np
import keras
import random
from sklearn.model_selection import train_test_split
import pickle
from underthesea import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer , CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA
path = './preprocessing_data/'
path_file = os.listdir(path)
path_topic = "./topic/"
path_topics = os.listdir(path_topic)
path_topics = [e[:-4] for e in path_topics]
path_topics = sorted(path_topics,key=len,reverse=True)
doc = []
label = []
for i in path_file:
	p = path+i
	with open(p,"r") as f:
		data = f.read()
		link, data = data.split('\n')[0], data.split('\n')[1:]
		link = link[23:link.find('/', 23)]
		check = False
		for tp in range(len(path_topics)):
			t = path_topics[tp]
			if link.find(t) != -1:
				label.append(tp)
				check = True
				break
		if check == False:
			print(p)
			print(link)
		data = ' '.join(str(e) for e in data)
		doc.append(data)
		#print(link+ " "+path_topics[label[-1]])
print(str(len(label))+" "+str(len(doc)))

def diff(list1, list2):
	return list(set(list1).symmetric_difference(set(list2)))

label  = np.array(label)
vectorizer_tfidf = TfidfVectorizer()
X_nmf = vectorizer_tfidf.fit_transform(doc).toarray()
r = [e for e in range(len(label))]
train_ = random.sample(r,int(len(label)*0.8))
X_train , y_train  = np.array([X_nmf[e]  for e in train_]) , np.array([label[e] for e in train_])
r = diff(r,train_)
test_ = random.sample(r,int(len(r)/2))
X_test , y_test  = np.array([X_nmf[e]  for e in test_]) , np.array([label[e] for e in test_])
r = diff(r,test_)
X_validate , y_validate = np.array([X_nmf[e]  for e in r]) , np.array([label[e] for e in r])
#sys.exit()
# X_train , X_test , y_train , y_test = train_test_split(X_nmf,label,test_size=0.2)
# X_train , X_validate , y_train , y_validate = train_test_split(X_train,y_train,test_size=0.1)

model  = keras.models.Sequential()
model.add(keras.layers.Dense(53,activation='softmax'))
model.compile(optimizer='adam',metrics=['acc'],loss='sparse_categorical_crossentropy')
model.fit(X_nmf,label,epochs=50,batch_size=64,validation_data=(X_validate,y_validate))
model.evaluate(X_test,y_test)
# vectorizer_count = CountVectorizer()
# X_lda = vectorizer_count.fit_transform(doc)
# tf_feature_names = vectorizer_count.get_feature_names()
# # Tweak the two parameters below
# number_topics = len(path_topics)
# # Create and fit the LDA model
# lda = LDA(n_components=number_topics, n_jobs=-1)
# lda.fit(X_lda)
# def display_topics(model, feature_names, no_top_words):
# 	for topic_idx, topic in enumerate(model.components_):
# 		print("Topic %d:" % (topic_idx))
# 		print(" ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]))
#
# no_top_words = 10
# display_topics(lda, tf_feature_names, no_top_words)
# #database = lda.fit_transform(X_lda)
# #np.save('weights',database)
# database = np.load('weights.npy')
# print("Input file directory : ")
# file = input()
# with open(file,"r") as f:
# 	data = f.read()
# 	data = word_tokenize(data)
# 	with open('vietnamese-stopwords.txt','r') as v:
# 		list_stopwords = v.read().split('\n')
# 	res = ""
# 	for w in data:
# 		if w not in list_stopwords:
# 			res+=w
# 	data = [res]
# 	data = vectorizer_count.fit_transform(data)
# 	result = lda.fit_transform(data)
# min = 9999
# topic = ""
# for i in range(len(doc)):
# 	temp = database[i]
# 	dist = np.linalg.norm(temp - result)
# 	if dist<min:
# 		dist = min
# 		topic = path_topics[label[i]]
# print("Your doc topic is : "+topic)
# # check maxlen of doc : 3720
# # maxim = 0
# # for i in path_file:
# # 	p = path+i
# # 	with open(p,'r') as f:
# # 		data = f.read()
# # 		link,data = data.split('\n')[0],data.split('\n')[1:]
# # 		data = ' '.join(str(e) for e in data)
# # 		if maxim < len(word_tokenize(data)):
# # 			maxim = len(word_tokenize(data))
# # print(maxim)
#
