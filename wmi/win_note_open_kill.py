import wmi
c = wmi.WMI ()
process_id, return_value = c.Win32_Process.Create (CommandLine="notepad.exe")
for process in c.Win32_Process (ProcessId=process_id):
  print (process.ProcessId, process.Name)
process.Terminate()