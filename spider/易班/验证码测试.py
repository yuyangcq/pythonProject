from PIL import Image,ImageEnhance
import pytesseract
#上面都是导包，只需要下面这一行就能实现图片文字识别
im = Image.open('d:\\merge_source.jpg')


#灰度处理部分
im2=im.convert("L")
im2.show()
text=pytesseract.image_to_string(im2,lang='chi_sim').strip() #使用image_to_string识别验证码
print(text)