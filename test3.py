import win32com.client
#使用IE浏览器类的ID号，进行COM对象的实例化。
clsid = '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}'
windows = win32com.client.Dispatch(clsid)
for browser in windows:
    print (browser.LocationUrl)
    #print (browser.)