# # -*- coding: utf-8 -*-
#
# import os, sys
# from PIL import Image
#
# # curdir="E:\\py\\WinPython-32bit-2.7.6.4\\study"
# #
# # os.chdir(curdir)
#
#
# def RGB2BlackWhite(filename):
#     im=Image.open(filename)
#     print "image info,", im.format, im.mode, im.size
#     (w, h) = im.size
#     R = 0
#     G = 0
#     B = 0
#
#     for x in xrange(w):
#         for y in xrange(h):
#             pos = (x, y)
#             rgb = im.getpixel( pos )
#             (r, g, b) = rgb
#             R = R+r
#             G = G+g
#             B = B+b
#
#     rate1 = R*1000/(R+G+B)
#     rate2 = G*1000/(R+G+B)
#     rate3 = B*1000/(R+G+B)
#
#     print "rate:", rate1, rate2, rate3
#
#
#     for x in xrange(w):
#         for y in xrange(h):
#             pos = (x, y)
#             rgb = im.getpixel( pos )
#             (r, g, b) = rgb
#             n = r*rate1/1000 + g*rate2/1000 + b*rate3/1000
#             #print "n:",n
#             if n >= 60:
#                 im.putpixel( pos, (255, 255, 255))
#             else:
#                 im.putpixel( pos, (0, 0, 0))
#
#     im.save("blackwhite.bmp")
#
# def saveAsBmp(fname):
#     pos1=fname.rfind('.')
#     fname1=fname[0:pos1]
#     fname1=fname1+'_2.bmp'
#     im = Image.open(fname)
#     new_im = Image.new("RGB", im.size)
#     new_im.paste(im)
#     new_im.save(fname1)
#     return fname1
#
# if __name__=="__main__":
#     filename=saveAsBmp("/home/cj/图片/3.bmp")
#     RGB2BlackWhite(filename)

from PIL import Image

def Binarized(Image,Threshold):
    '''

    用二分法做判别 处理每一个点
    :param Image: 原始图片
    :param Threshold: 阈值
    :return:
    '''

    ImgNew=Image.crop()
    ImgNew=ImgNew.convert("L")

    Pixels = ImgNew.load()
    (Width, Height) = ImgNew.size
    for i in xrange(Width):
        for j in xrange(Height):
            if Pixels[i, j] > Threshold:
                Pixels[i, j] = 255 #白色
            else:
                Pixels[i, j] = 0 #黑色
    ImgNew.save('/home/cj/图片/1_after.png')

if __name__=="__main__":
    Filename="/home/cj/图片/1.png"
    im=Image.open(Filename)
    Binarized(im, 150)
