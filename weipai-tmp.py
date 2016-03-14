# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
import os,os.path
import sys
import json
import urlparse
user_list = []
def download_video (user=[]):
	print "i'am download_video"
	idd2 = 1
	for url_list in user:
		request = urllib2.urlopen(str(url_list))
		content = request.read() #接收服务器发来的数据
		pattern = re.compile('http://enc.weipai.cn/.*?m3u8') #建立正则表达式
		items = re.findall(pattern,content) #对接受到内容进行正则匹配
		m3u8_url = []
		for m3u_list in items: ##把m3u8地址添加到m3u8 list里
			print m3u_list;
			m3u8_url.append(m3u_list)
#下载并摄取m3u8
#打开m3u8并提取ts文件存入tt[]
		print "downloading each ts video of m3u8_url"
		num = 1	#为下载m3u8地址计数
		for j in m3u8_url:
			print "i'am download ts"
			print j 
			f1=urllib2.urlopen(j) #对服务器进行下载ts的请求
			data=f1.read()#接收服务器发来的数据
			with open(str(num)+ '.m3u8','wb')as code:
				code.write(data)#新建m3u8文件
			ts_url=[]
			f2=open(str(num)+ '.m3u8','rb')#打开m3u8文件
			pattern2=re.compile('http://aliv.weipai.cn/.*?ts')#匹配出ts地址
			for i in f2:#把ts地址存入tt的值列表
				result = re.match(pattern2,i)
				if result:
					ts_url.append(i)
					print i
				f2.close
			num = num + 1
			print "downloading ts"
			idd = 0
			for k in ts_url:#下载ts并把结果文件存放到指定目录
				f3=urllib2.urlopen(ts_url[idd])
				data2=f3.read()
				idd=idd+1
				with open(str(idd)+"."+"ts","wb") as code1:
					code1.write(data2) 
#下载
#合并ts
			rootdir="e:\wppy"
			for filenames in os.walk(rootdir):#合并ts,并转移和删除
				for filename in filenames:
					print "file name is:" + str(filename)
				cmd1 = r'copy /b *.ts new.ts'
				os.system(cmd1)
				cmd2 = r'copy new.ts e:\\' + 'new' + str(idd2) + '.ts'
				os.system(cmd2)
				cmd3 = r'del *.ts'
				os.system(cmd3)
				cmd4 = r'del *.m3u8'
				os.system(cmd4)
				idd2 = idd2 + 1

		
		
		
		
def get_video_url(user_id):
	user_id_list = [user_id]
	cursor_value = 0
	for mod in user_id_list:
		while(cursor_value < 360):
			newURL = urlparse.urljoin('http://w1.weipai.cn/user/',"compresseduservideos?"+"&cursor=%s" % str(cursor_value)+"&user_id=%s" % str(mod) + "&count=18" + "&sort=hot" + "&relative=after" ) #在现成url加上文件路径
  #  ##判断是否为最后 一页 getm3u8判断是否为最后一页
			cursor_value = cursor_value + 18
			#print "\t" + newURL
			user_list.append(newURL)
			#print user_list
	return user_list

def main():
	print sys.argv[2]
	kk = get_video_url(sys.argv[2])
	print kk
	download_video(kk)
	
if __name__ == "__main__":
	print sys.argv[:]
	main()