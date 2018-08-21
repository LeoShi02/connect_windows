

codeurl = 'http://www.pss-system.gov.cn/sipopublicsearch/portal/login-showPic.shtml'
valcode = requests.get(codeurl)

f = open('valcode.png', 'wb')
    # 将response的二进制内容写入到文件中
    f.write(valcode.content)
    # 关闭文件流对象
    f.close()

code = input('请输入验证码：')
    data["j_validation_code"] = str(code)


data = {
        "j_loginsuccess_url": "",
        "j_validation_code": "",
        "j_username": base64name,
        "j_password": base64pass
    }

checkUrl = 'http://www.pss-system.gov.cn/sipopublicsearch/wee/platform/wee_security_check'
resp = requests.post(checkUrl, headers = checkHeader, cookies = requests.utils.dict_from_cookiejar(valcode.cookies), data=data)