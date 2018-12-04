import pytesseract
from PIL import Image
from PIL import ImageEnhance

def verificationCode():
    im = Image.open('D:\\xiang\\QQ截图20181203154729.png')
    im = im.convert('L')
    # im.show()
    im = ImageEnhance.Contrast(im)
    im = im.enhance(3)
    im.show()
    im = pytesseract.image_to_string(im)
    # im = im.replace(' ','')
    print(im)


if __name__ == '__main__':
    verificationCode()