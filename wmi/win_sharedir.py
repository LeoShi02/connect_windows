
import wmi
c = wmi.WMI ()
for share in c.Win32_Share ():
  print ("%6s   %s" % (share.Name, share.Path))