# 导入包
import muggle_ocr

# 初始化；model_type 包含了 ModelType.OCR/ModelType.Captcha 两种
sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.OCR)
# ModelType.OCR 可识别光学印刷文本 这里个人觉得应该是官方文档写错了 官方文档是ModelType.Captcha 可识别光学印刷文本
with open(r"test1.png", "rb") as f:
    b = f.read()
text = sdk.predict(image_bytes=b)
print(text)

# ModelType.Captcha 可识别4-6位验证码
sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
with open(r"test1.png", "rb") as f:
    b = f.read()
text = sdk.predict(image_bytes=b)
print(text)