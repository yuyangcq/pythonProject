"""
2020.09.26:alian
改变图片的位深度
"""
from PIL import Image as ImagePIL, ImageFont, ImageDraw


im = ImagePIL.open('d:\\aa.jpg')
im.save(r'D:\\1.jpg',dpi=(96.0,96.0))