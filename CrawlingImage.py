#coding:utf8
import urllib2
from PIL import Image
import cStringIO
url = 'http://xk.suda.edu.cn/CheckCode.aspx'
url2 = 'http://202.195.136.14:8080/reader/captcha.php'

for i in range(100):
    request = urllib2.Request(url)
    res = urllib2.urlopen(request).read()
    image = Image.open(cStringIO.StringIO(res))
    image.save("/home/cj/图片/TImage/test"+str(i)+".png")

for i in range(100):
    request = urllib2.Request(url2)
    res = urllib2.urlopen(request).read()
    image = Image.open(cStringIO.StringIO(res))
    image.save("/home/cj/图片/LIBImage/image"+str(i)+".png")

