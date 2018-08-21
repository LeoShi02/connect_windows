import wmi
c = wmi.WMI ()
for disk in c.Win32_LogicalDisk (DriveType=3):
  print (disk.Caption, "%0.2f%% free" % (100.0 * int (disk.FreeSpace) / int (disk.Size)))