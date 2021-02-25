import os
import os.path

if __name__ == '__main__':
    for parent, dirnames, filenames in os.walk("F:\\zupucaijian"):
        i=34
        for filename in filenames:
            print("parent is: " + parent)
            print("filename is: " + filename)
            print(os.path.join(parent, filename))  # 输出rootdir路径下所有文件（包含子文件）信息
            newName=str(i)+".jpg"
            os.rename(os.path.join(parent, filename), os.path.join(parent, newName))
            i=i+1