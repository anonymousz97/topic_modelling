# import facebook
# import requests
# import json
#
# access_token = "EAAY8BPJnX0ABAOt3PLOnQj5ZA1vJif5oGMxlD1RZBrIuWcQ5GZBdMZBFGPXyckohls3n2HvNRnXXmgXVOcVxlyBKbYx4LLvremGwmKTcy9Ts3BePpWHJSGkZBUcO48GAIoC9w8hth4uLZC7s6ZBPHLFItHKVlQ27ZCYFycMX1QdeOQZDZD"
# user = "https://www.facebook.com/AnonymousZ.PTIT"
# user_id = '100005198855294'
# graph = facebook.GraphAPI(access_token=	access_token)
# profile = graph.get_object(id=user_id,link=user)
# print(profile)
# #posts = graph.get_connections(profile['id'],connection_name='posts')
# #print(posts)
# # post_id = "808960762620545"
# # friends = graph.get_connections(id=user_id, connection_name='friends')
# # print(friends)
# # cmt = graph.get_connections(post_id,connection_name='comments')
# # print(cmt)
# r = requests.get("https://graph.facebook.com/v4.0/me/posts?access_token=EAAY8BPJnX0ABAOt3PLOnQj5ZA1vJif5oGMxlD1RZBrIuWcQ5GZBdMZBFGPXyckohls3n2HvNRnXXmgXVOcVxlyBKbYx4LLvremGwmKTcy9Ts3BePpWHJSGkZBUcO48GAIoC9w8hth4uLZC7s6ZBPHLFItHKVlQ27ZCYFycMX1QdeOQZDZD").json()
# j = 0
# for i in r.keys():
# 	if i == "previous" or i == "next":
# 		continue
# 	for post in r[i]:
# 		j+=1
# 		k=0
# 		for item in post.keys():
# 			k+=1
# 			if k==3:
# 				print(str(j)+" "+str(post[item]))
# #print(result)
# #print(result['data'][0])
import requests
from bs4 import BeautifulSoup
