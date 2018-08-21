import os
filepath = 'D:\\bat'  #定义第一波段的路径
resultpath = 'D:\\bat' #定义融合后影像存储路径
filelist = os.listdir(filepath) #遍历文件夹所有的文件
file_raw_list = filter(lambda filename:filename[-4:] == '.raw', filelist) #筛选出格式为.raw的文件
for i in range(len(file_raw_list)): #循环遍历第一波段文件夹中raw格式文件，生成其他波段影像的路径
    fileon0 = file_raw_list[i]
    file_path = [] #6波段影像的路径
    #根据命名规则和第一波段文件名得到6个波段影像的文件名和路径，存储在表file_path中
    for i in range(6):
        fileonname = fileon0[0:3] + str(i) + fileon0[4:]#各波段影像文件名，将文件名中的0替换为0-5
        fileonpath = filepath[0:-5] + str(i) + filepath[-4:]#各波段影像文件夹路径，将文件夹中的0替换为0-5
        file_path.append(fileonpath+'\\'+fileonname)#生成6个波段影像的访问路径，例：‘D:\\第一波段所在的文件夹\\1\\20m\\TTC1*(图像标号).raw’

    #输入要执行的命令(按照控制台程序的格式输入参数)，相当于直接在windows的cmd窗口中输入的命令
    command = r'D:\控制台程序所在的文件夹\Fusion.exe' + ' ' + file_path[1] + ' ' + file_path[2] + ' ' + file_path[3] + ' ' + file_path[4] + ' ' \
    + file_path[0] + ' ' + file_path[5] + ' '+ resultpath+'\\'+ fileon0[0:-4]+'.tiff'
    os.system(command)