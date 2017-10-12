#Little Reptile using to get information of exchange programs automatically
import urllib.request
from lxml import html
import requests
import tkinter

window1 = tkinter.Tk()
window1.mainloop()

response = requests.get("http://bksy.zju.edu.cn/dwjlfwpt/redir.php?catalog_id=1064225")
response.encoding = 'gbk'
tree = html.fromstring(response.text)

title = tree.xpath('//a[@class="highlight"]/text()')
for i in title:
	print(i)
