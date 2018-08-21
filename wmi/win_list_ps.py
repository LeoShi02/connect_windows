import wmi
c = wmi.WMI ()
for process in c.Win32_Process ():
  print ("%5s  %s" % (process.ProcessId, process.Name))