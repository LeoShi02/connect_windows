# import os
# os.system("c:\\sam.bat")

import subprocess

cmd = 'cmd.exe c:\\sam.bat'
p = subprocess.Popen("cmd.exe /c" + "D:\\bat\sam.bat abc", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
curline = p.stdout.readline()
while (curline != b''):
    print(curline)
    curline = p.stdout.readline()

p.wait()
print(p.returncode)