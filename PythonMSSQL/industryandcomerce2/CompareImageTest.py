from PIL import Image
from PIL.ImageDraw import ImageDraw



def is_pixel_equal(img1, img2, x, y):
    pix1 = img1.load()[x, y]
    pix2 = img2.load()[x, y]
    if (abs(pix1[0] - pix2[0] < 60) and abs(pix1[1] - pix2[1] < 60) and abs(pix1[2] - pix2[2] < 60)):
        return True
    else:
        return False



img1 = Image.open(r'D:\test\_start.png')
img2 = Image.open(r'D:\test\10.png')


#w1, h1 = img1.size
#w2, h2 = img2.size
#if w1 != w2 or h1 != h2:
#    print(False)
#left = 0
#flag = False
#for i in range(0, w1):
#    for j in range(h1):
#        if not is_pixel_equal(img1, img2, i, j):
#            left = i
#            flag = True
#            break
#    if flag:
#        break
#if left == 60:
#    left -= 2
i = 593
plus = 97
drawObject  = ImageDraw(img1)
drawObject.line([i,0,i,768],"black",width=1)
img1.show()
drawObject2  = ImageDraw(img2)
drawObject2.line([i+plus,0,i+plus,768],"red",width=1)
img2.show()

del drawObject2
