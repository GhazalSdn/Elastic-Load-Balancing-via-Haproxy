import os
import statistics
import datetime
import time


t = datetime.datetime.now()
date = (str(t))[0:10]
firstR=False
secondR=False
thirdR=False
fourthR=False

while True:
	if firstR == False:
		resExe = os.system("scp ws1@192.168.56.3:/var/lib/collectd/csv/ws1/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws1")
		fileFirst = open ('/home/ws1/autoscale/data/ws1/percent-user-'+date,"r")
		lineList1 = fileFirst.readlines()
		fileFirst.close()
		percentage1=[]
		records1 = lineList1[-12:]
		for rec in records1:
			percentage1.append(float(rec.rstrip('\n').split(',')[1]))
		finalPercentOne =statistics.mean(percentage1)
		print(finalPercentOne)
		if finalPercentOne >= 1:
			res= open("/home/ws1/autoscale/result/res.txt","w+")
			res.write("ON WS2")
			res.close()
			firstR = True
		time.sleep(30)
	elif firstR == True and secondR == False:
		resExe = os.system("scp ws1@192.168.56.3:/var/lib/collectd/csv/ws1/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws1")
		fileFirst = open ('/home/ws1/autoscale/data/ws1/percent-user-'+date,"r")
		lineList1 = fileFirst.readlines()
		fileFirst.close()
		percentage1=[]
		records1 = lineList1[-12:]
		for rec in records1:
			percentage1.append(float(rec.rstrip('\n').split(',')[1]))
		finalPercentOne =statistics.mean(percentage1)
		print(finalPercentOne)
		resExe = os.system("scp ws1@192.168.56.2:/var/lib/collectd/csv/ws2/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws2")
		fileSec = open ('/home/ws1/autoscale/data/ws2/percent-user-'+date,"r")
		lineList2 = fileSec.readlines()
		fileSec.close()
		percentage2=[]
		records2 = lineList2[-12:]
		for rec in records2:
			percentage2.append(float(rec.rstrip('\n').split(',')[1]))
		finalPercentTwo =statistics.mean(percentage2)
		print(finalPercentOne)
		print(finalPercentTwo)
		if finalPercentOne >= 1 and finalPercentTwo >= 1:
			res= open("/home/ws1/autoscale/result/res.txt","w+")
			res.write("ON WS3")
			res.close()
			secondR = True
		time.sleep(30)
	elif secondR == True and thirdR == False:
		resExe = os.system("scp ws1@192.168.56.3:/var/lib/collectd/csv/ws1/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws1")
		fileFirst = open ('/home/ws1/autoscale/data/ws1/percent-user-'+date,"r")
		lineList1 = fileFirst.readlines()
		fileFirst.close()
		percentage1=[]
		records1 = lineList1[-12:]
		for rec in records1:
			percentage1.append(float(rec.rstrip('\n').split(',')[1]))
		finalPercentOne =statistics.mean(percentage1)
		resExe = os.system("scp ws1@192.168.56.2:/var/lib/collectd/csv/ws2/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws2")
		fileSec = open ('/home/ws1/autoscale/data/ws2/percent-user-'+date,"r")
		lineList2 = fileSec.readlines()
		fileSec.close()
		percentage2=[]
		records2 = lineList2[-12:]
		for rec in records2:
			percentage2.append(float(rec.rstrip('\n').split(',')[1]))
		finalPercentTwo =statistics.mean(percentage2)
		resExe = os.system("scp ws1@192.168.56.4:/var/lib/collectd/csv/ws3/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws3")
		fileThird = open ('/home/ws1/autoscale/data/ws3/percent-user-'+date,"r")
		lineList3 = fileThird.readlines()
		fileThird.close()
		percentage3=[]
		records3 = lineList3[-12:]
		for rec in records3:
			percentage3.append(float(rec.rstrip('\n').split(',')[1]))
		finalPercentThree =statistics.mean(percentage3)
		print(finalPercentOne)
		print(finalPercentTwo)
		print(finalPercentThree)
		if finalPercentOne <= 50 and finalPercentTwo <= 50 and finalPercentThree <= 50:
			res= open("/home/ws1/autoscale/result/res.txt","w+")
			res.write("OFF WS3")
			res.close()
			thirdR = True
		time.sleep(30)
	elif thirdR == True and fourthR == False:
		resExe = os.system("scp ws1@192.168.56.3:/var/lib/collectd/csv/ws1/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws1")
		fileFirst = open ('/home/ws1/autoscale/data/ws1/percent-user-'+date,"r")
		lineList1 = fileFirst.readlines()
		fileFirst.close()
		percentage1=[]
		records1 = lineList1[-12:]
		for rec in records1:
			percentage1.append(float(rec.rstrip('\n').split(',')[1]))
		finalPercentOne =statistics.mean(percentage1)
		resExe = os.system("scp ws1@192.168.56.2:/var/lib/collectd/csv/ws2/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws2")
		fileSec = open ('/home/ws1/autoscale/data/ws2/percent-user-'+date,"r")
		lineList2 = fileSec.readlines()
		fileSec.close()
		percentage2=[]
		records2 = lineList2[-12:]
		for rec in records2:
			percentage2.append(float(rec.rstrip('\n').split(',')[1]))
		finalPercentTwo =statistics.mean(percentage2)
		print(finalPercentOne)
		print(finalPercentTwo)
		if finalPercentOne <=40 and finalPercentTwo <=40:
			res= open("/home/ws1/autoscale/result/res.txt","w+")
			res.write("OFF WS2")
			res.close()
			firstR = False
			secondR = False
			thirdR = False
		time.sleep(30)
