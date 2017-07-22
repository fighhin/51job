#coding:utf-8
import re
import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getHtml(page):
    url='https://www.qiushibaike.com/8hr/page/2/?s=5001775'.format(page)
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    headers={'User-Agent':user_agent}
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    html=response.read()
    #print html
    return html
def getDZ(html):
    reg=re.compile(r'<div class="content">.*?<span>(.*?)</span>',re.S)
    duanzi=re.findall(reg,html)
    #print duanzi
    return  duanzi

for i in range(1,6):
    html=getHtml(i)
    for j in getDZ(html):
        with open('duanzi.txt','a') as f:
            f.write(j+'\n\n\n')
