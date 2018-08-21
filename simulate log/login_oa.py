from http import cookiejar
from urllib.request import urlopen
from PIL import ImageOps
from urllib import request
import pytesseract
import urllib.parse
from PIL import Image
#reload(sys)

url = 'http://oa.ct108.com//WebForm/VerifyCode.aspx '
path = urlopen(url)
#def cleanImage(imagePath):
#    image = Image.open(imagePath)
#    image.show()
#    image = image.point(lambda x: 0 if x < 50 else 255)
#    borderImage = ImageOps.expand(image, border=20, fill=255)
#    borderImage.save("1.png")
#cleanImage(path)


postUrl="http://oa.ct108.com/Login/ULogin"
cookie=cookiejar.CookieJar()
handler=request.HTTPCookieProcessor(cookie)
opener=request.build_opener(handler)


picture=opener.open(url).read()
local=open('1.png','wb')
local.write(picture)
local.close()
CheckCoden=input('CheckCoden:')

username='shiyx'
password='syx110966'
token='FE0EChZNVU1bWVdWXFpcWltdV1hZW1lZXVxWE15eWkFeVlpBXldcQVtZE11fXlZXWVpeWVxWXE1DTQoXHwYdChsGAgpNVU1dX15XQlhCXVZNEg%253D%253D'
image = Image.open('1.png')
CheckCode = pytesseract.image_to_string(image)
postData = {
'UserName': username,
'Password': password,
'VerificationCode': CheckCoden,
'CtOaToken': token,
}

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

data = urllib.parse.urlencode(postData).encode(encoding='UTF8')

request = request.Request(postUrl, data, headers)


#mobile_url='http://oa.ct108.com/Login/GetToken'

#mobile_post_data = input('mobile_post_data:')

#mobile_request = request.Request(mobile_url, mobile_post_data, headers)


try:

    response=opener.open(request)
    #moble_code =opener.open()
    result=response.read().decode('UTF8')
    print (result)
    print (CheckCode)

except urllib.error.HTTPError as e:
    print (e.code)