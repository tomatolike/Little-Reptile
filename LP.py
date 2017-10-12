#Little Reptile using to get information of exchange programs automatically
import urllib.request
from lxml import html
import requests
import os
import time

def test():
	response = requests.get("http://bksy.zju.edu.cn/dwjlfwpt/redir.php?catalog_id=1064225")
	response.encoding = 'gbk'
	tree = html.fromstring(response.text)

	title2 = tree.xpath('//a[@class="highlight"]/text()')
	ok=0
	for i in title2:
		if(i not in title1):
			op = "osascript -e \'display notification \""+i+"\" with title \"大哥！你有新的项目！\"\'"
			os.system(op)
			title1.append(i)
			ok=1
	if(ok==0):
		print("Nothing new")

title1=[]
title2=[]
while(1):
	test()
	time.sleep(3600)
