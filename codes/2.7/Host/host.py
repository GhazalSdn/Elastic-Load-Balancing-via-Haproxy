import os
from pathlib import Path

while True:
	commandFile = "/Users/ghazal/Desktop/CommandForHost/res.txt"
	PathCommandFile = Path(commandFile)
	resExe = os.system("scp ws1@192.168.56.6:/home/ws1/autoscale/result/res.txt /Users/ghazal/Desktop/CommandForHost")
	if PathCommandFile.is_file():
		commandFile = open ( commandFile,"r" )
		lineList = commandFile.readlines()
		commandFile.close()
		vmName = lineList[0]
		if (vmName.split()[0] == "ON"):
			resExe = os.system('/Applications/VirtualBox.app/Contents/MacOS/VBoxManage startvm '+vmName.split()[1])
		elif (vmName.split()[0] == "OFF"):
			resExe = os.system('/Applications/VirtualBox.app/Contents/MacOS/VBoxManage controlvm '+vmName.split()[1]+' poweroff')
