from PIL import Image
import pytesseract

image0 = Image.open('C://Users//xuejian//Downloads//1627700442020.png')
# print(image0)
# captcha = pytesseract.image_to_string(image0)
captcha = pytesseract.image_to_string(image0)
print(captcha)
