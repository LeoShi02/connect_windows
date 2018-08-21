from urllib.request import urlopen
import pytesseract
from PIL import Image
from PIL import ImageOps
url = 'http://oa.ct108.com//WebForm/VerifyCode.aspx '
path = urlopen(url)
def cleanImage(imagePath):
    image = Image.open(imagePath)
    image.show()
    image = image.point(lambda x: 0 if x < 50 else 255)
    borderImage = ImageOps.expand(image, border=20, fill=255)
    borderImage.save("1.gif")
cleanImage(path)
image = Image.open('1.gif')
vcode = pytesseract.image_to_string(image)
print (vcode)
#p = subprocess.Popen(["tesseract", "1.gif", "captcha"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#p.wait()
#f = open("captcha.txt", "rb")
#b = f.read()
#s = b.decode()
#print(s.replace('\n', '').replace(' ', ''))