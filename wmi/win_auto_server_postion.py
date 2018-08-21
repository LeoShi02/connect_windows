
import wmi
c = wmi.WMI ()
for s in c.Win32_StartupCommand ():
    print ("[%s] %s <%s>" % (s.Location, s.Caption, s.Command))