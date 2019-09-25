import requests
from bs4 import BeautifulSoup
import re

from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


r = requests.get('https://www.24h.com.vn/')
soup = BeautifulSoup(r.content,'lxml')
#print(soup.prettify())
link_topic = []
i=1
for link in soup.findAll('a', attrs={'href': re.compile("^https:\/\/.+c\d{2,3}\.html$")}):
	#print(str(i)+" "+str(link.get('href')))
	i+=1
	link_topic.append(link.get('href'))
list_topic = []
save_doc = 0
for topic in link_topic:
	beg = topic.find("/", 8)
	end = topic.rfind("-")
	#print(topic[beg + 1:end])
	list_topic.append(topic[beg + 1:end])
	list_doc = []
	for j in range(1,21):
		print("Processing page : "+str(j)+" topic : "+list_topic[-1])
		print("Crawling "+topic+"?vpage="+str(j))
		path = topic+"?vpage="+str(j)
		r = requests.get(path)
		soup = BeautifulSoup(r.content,'html.parser')
		#print(soup.prettify())
		for link in soup.findAll('a',attrs={'href': re.compile(("^https://"))}):
			if list_topic[-1]+"/" in link.get('href'):
				list_doc.append(link.get('href'))
	list_doc = list(dict.fromkeys(list_doc))
	file_name = "./topic/"+list_topic[-1]+".txt"
	with open(file_name,"w+") as f:
		for doc in list_doc:
			f.write(doc+'\n')
			#print(doc)
			r = requests.get(doc)
			soup = BeautifulSoup(r.content, 'lxml')
			file_doc = "./data/"+str(save_doc)+".txt"
			save_doc+=1
			with open(file_doc,"w+") as g:
				g.write(doc+'\n')
				data = strip_tags(str(soup.findAll('p'))).replace("Cơ quan chủ quản: Công ty Cổ phần Quảng cáo Trực tuyến 24H Trụ sở: Tầng 12, Tòa nhà Geleximco, 36 Hoàng Cầu, Phường Ô Chợ Dừa, Quận Đống Đa, TP Hà Nội. Tel: (84-24) 73 00 24 24 hoặc (84-24) 3512 1806 - Fax: (84-24) 3512 1804. Chi nhánh: Tầng 7, Tòa nhà Việt Úc, 402 Nguyễn Thị Minh Khai, Phường 5, Quận 3, TP. Hồ Chí Minh. Tel: (84-28) 7300 2424 / Giấy phép số 332/GP – TT ĐT ngày cấp 22/01/2018 SỞ THÔNG TIN VÀ TRUYỀN THÔNG HÀ NỘI. Chịu trách nhiệm xuất bản: Phan Minh Tâm. HOTLINE: 0965 08 24 24]","")
				g.write(data)
				print("Saved doc "+file_doc)

#print(soup.find("li",class_='sbLi'))