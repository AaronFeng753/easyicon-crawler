#coding=utf-8

import requests
import re
import os

print('图标来源: https://www.easyicon.net/')
keyword = input('请输入您获取的图图标的关键词: ')
print('下载图标中...')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
r1=requests.get('https://www.easyicon.net/language.en/iconsearch/'+keyword+'/?s=download_png_DESC',headers=headers)

p1 = re.compile(r'<a href="\S+" title="PNG icons download">')
res1 = p1.findall(r1.text)

p2 = re.compile(r'https://www.easyicon.net/download/png/\S+/\S+/')
res2=[]
for res in res1:
	res2.append(p2.findall(res)[0])
	
filenum=0
current_dir = os.path.dirname(os.path.abspath(__file__))
KeyWordPath = current_dir + '\\'+keyword+'\\'
if os.path.exists(KeyWordPath) == False:
	os.mkdir(KeyWordPath)
for res in res2:
	filenum = filenum+1
	filename = KeyWordPath+str(filenum)+'.png'
	r2=requests.get(res,headers=headers)
	with open(filename,'wb+') as f:
		f.write(r2.content)
print('图标下载完成,已保存到:'+KeyWordPath)

