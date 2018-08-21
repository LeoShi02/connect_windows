
import wmi
c = wmi.WMI ()
for physical_disk in c.Win32_DiskDrive ():
    for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"):
        for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"):
            print (physical_disk.Caption, partition.Caption, logical_disk.Caption)