# coding: utf-8

from PIL import Image
import aircv as ac
import cv2
imsrc = ac.imread('youimage.png') # 原始图像
imsch = ac.imread('searched.png') # 带查找的部分
ac.find_template(imsrc, imsch)
#返回值
#{'confidence': 0.5522063970565796, 'result': (557, 214), 'rectangle': ((489, 146), (489, 282), (625, 146), (625, 282))}
# result: 查找到的点
# rectangle： 目标图像周围四个点的坐标
# confidence: 查找图片匹配成功的特征点 除以 总的特征点

imsrc = ac.imread('cap4.jpg')
imobj = ac.imread('cap2.png')

# find the match position
pos = ac.find_template(imsrc, imobj)

print pos
# {'confidence': 0.5522063970565796, 'result': (557, 214), 'rectangle': ((489, 146), (489, 282), (625, 146), (625, 282))}

color = (0, 255, 0)
line_width = 10

draw_rectangle(imsrc, pos['rectangle'][0], pos['rectangle'][-1], color, line_width)

def draw_rectangle(img, pos1, pos2, color, line_width):
    cv2.rectangle(img, pos1, pos2, color, line_width)
    cv2.imshow('objDetect', imsrc)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def convert(imgName, saveName):
    im = Image.open(imgName)
    im = im.convert('RGBA')

    width = im.size[0]
    height = im.size[1]
    for h in range(0, height):
        for w in range(0, width):
            pixel = im.getpixel((w, h))
            if pixel[0] > 0 and pixel[1] > 0 and pixel[2] > 0 and pixel[3] > 0:
                im.putpixel((w, h), (0,0,0, 220))
            elif pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                im.putpixel((w, h), (0, 0, 0, 220))
            else:
                pass
    im.save(saveName)

convert('hycdn_2_1585354975542067968_0.png','cap2.png')





if __name__ == "__main__":
    Image.open('hycdn_1_1585354975542067968_0.jpeg').convert('L').save('cap4.jpg')
