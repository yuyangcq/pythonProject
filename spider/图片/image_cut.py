
import os
import os.path
import cv2
from PIL import Image


#指明被遍历的文件夹
rootdir = r'F:\zupucaijian'

if __name__ == '__main__':

    for parent, dirnames, filenames in os.walk(rootdir):#遍历每一张图片
        count =1
        for filename in filenames:
            print('parent is :' + parent)
            print('filename is :' + filename)
            currentPath = os.path.join(parent, filename)
            print('the fulll name of the file is :' + currentPath)

            img = cv2.imread(currentPath)#cv2.imread必须是英文路径！！！！ 中文路径下：cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
            cropped = img[0:1080, 350:1570]  # 裁剪坐标为[y0:y1, x0:x1]
            cv2.imwrite("F:\\"+str(count)+".jpg", cropped)
            count=count+1








































    # im = Image.open("C:\\Users\\admin\\Desktop\\2020-10-30_132533.png")
    # # 图片的宽度和高度
    # img_size = im.size
    # print("图片宽度和高度分别是{}".format(img_size))
    # '''
    # 裁剪：传入一个元组作为参数
    # 元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
    # '''
    # # 截取图片中一块宽和高都是250的
    # x = 350
    # y = 0
    # w = 1220
    # h = 1080
    # region = im.crop((x, y, x+w, y+h))
    # region.save("C:\\Users\\admin\\Desktop\\1.jpg")
    #
