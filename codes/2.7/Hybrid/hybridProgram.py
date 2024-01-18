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
coeficient = 0.5
sleepTime = 45
meanConf = -12


while True:
        if firstR == False:
                resExe = os.system("scp ws1@192.168.56.3:/var/lib/collectd/csv/ws1/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws1")
                fileFirst = open ('/home/ws1/autoscale/data/ws1/percent-user-'+date,"r")
                lineList1 = fileFirst.readlines()
                fileFirst.close()
                percentage1=[]
                records1 = lineList1[meanConf:]
                for rec in records1:
                        percentage1.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentOne =statistics.mean(percentage1)
                resExe = os.system("scp ws1@192.168.56.3:/var/lib/collectd/csv/ws1/memory/percent-used-"+date+" /home/ws1/autoscale/data/ws1")
                fileFirstMem = open ('/home/ws1/autoscale/data/ws1/percent-used-'+date,"r")
                lineList1Mem = fileFirstMem.readlines()
                fileFirstMem.close()
                percentage1Mem=[]
                records1Mem = lineList1Mem[meanConf:]
                for rec in records1Mem:
                        percentage1Mem.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentOneMem =statistics.mean(percentage1Mem)
                print(finalPercentOne)
                print(finalPercentOneMem)
                print("total percent for VM1: ", (coeficient*finalPercentOne)+(coeficient*finalPercentOneMem))
                if (coeficient*finalPercentOne)+(coeficient*finalPercentOneMem) >= 1:
                        res= open("/home/ws1/autoscale/result/res.txt","w+")
                        res.write("ON WS2")
                        res.close()
                        firstR = True
                time.sleep(sleepTime)
        elif firstR == True and secondR == False:
                resExe = os.system("scp ws1@192.168.56.3:/var/lib/collectd/csv/ws1/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws1")
                fileFirst = open ('/home/ws1/autoscale/data/ws1/percent-user-'+date,"r")
                lineList1 = fileFirst.readlines()
                fileFirst.close()
                percentage1=[]
                records1 = lineList1[meanConf:]
                for rec in records1:
                        percentage1.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentOne =statistics.mean(percentage1)
                resExe = os.system("scp ws1@192.168.56.3:/var/lib/collectd/csv/ws1/memory/percent-used-"+date+" /home/ws1/autoscale/data/ws1")
                fileFirstMem = open ('/home/ws1/autoscale/data/ws1/percent-used-'+date,"r")
                lineList1Mem = fileFirstMem.readlines()
                fileFirstMem.close()
                percentage1Mem=[]
                records1Mem = lineList1Mem[meanConf:]
                for rec in records1Mem:
                        percentage1Mem.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentOneMem =statistics.mean(percentage1Mem)
                resExe = os.system("scp ws1@192.168.56.2:/var/lib/collectd/csv/ws2/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws2")
                fileSec = open ('/home/ws1/autoscale/data/ws2/percent-user-'+date,"r")
                lineList2 = fileSec.readlines()
                fileSec.close()
                percentage2=[]
                records2 = lineList2[meanConf:]
                for rec in records2:
                        percentage2.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentTwo =statistics.mean(percentage2)
                resExe = os.system("scp ws1@192.168.56.2:/var/lib/collectd/csv/ws2/memory/percent-used-"+date+" /home/ws1/autoscale/data/ws2")
                fileSecMem = open ('/home/ws1/autoscale/data/ws2/percent-used-'+date,"r")
                lineList2Mem = fileSecMem.readlines()
                fileSecMem.close()
                percentage2Mem=[]
                records2Mem = lineList2Mem[meanConf:]
                for rec in records2Mem:
                        percentage2Mem.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentTwoMem =statistics.mean(percentage1Mem)
                print(finalPercentOne)
                print(finalPercentOneMem)
                print("total percent for VM1: ", (coeficient*finalPercentOne)+(coeficient*finalPercentOneMem))
                print(finalPercentTwo)
                print(finalPercentTwoMem)
                print("total percent for VM2: ", (coeficient*finalPercentTwo)+(coeficient*finalPercentTwoMem))
                if ((coeficient*finalPercentOne)+(coeficient*finalPercentOneMem) >= 1) and ((coeficient*finalPercentTwo)+(coeficient*finalPercentTwoMem) >= 1):
                        res= open("/home/ws1/autoscale/result/res.txt","w+")
                        res.write("ON WS3")
                        res.close()
                        secondR = True
                time.sleep(sleepTime)
        elif secondR == True and thirdR == False:
                resExe = os.system("scp ws1@192.168.56.3:/var/lib/collectd/csv/ws1/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws1")
                fileFirst = open ('/home/ws1/autoscale/data/ws1/percent-user-'+date,"r")
                lineList1 = fileFirst.readlines()
                fileFirst.close()
                percentage1=[]
                records1 = lineList1[meanConf:]
                for rec in records1:
                        percentage1.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentOne =statistics.mean(percentage1)
                resExe = os.system("scp ws1@192.168.56.3:/var/lib/collectd/csv/ws1/memory/percent-used-"+date+" /home/ws1/autoscale/data/ws1")
                fileFirstMem = open ('/home/ws1/autoscale/data/ws1/percent-used-'+date,"r")
                lineList1Mem = fileFirstMem.readlines()
                fileFirstMem.close()
                percentage1Mem=[]
                records1Mem = lineList1Mem[meanConf:]
                for rec in records1Mem:
                        percentage1Mem.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentOneMem =statistics.mean(percentage1Mem)
                resExe = os.system("scp ws1@192.168.56.2:/var/lib/collectd/csv/ws2/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws2")
                fileSec = open ('/home/ws1/autoscale/data/ws2/percent-user-'+date,"r")
                lineList2 = fileSec.readlines()
                fileSec.close()
                percentage2=[]
                records2 = lineList2[meanConf:]
                for rec in records2:
                        percentage2.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentTwo =statistics.mean(percentage2)
                resExe = os.system("scp ws1@192.168.56.2:/var/lib/collectd/csv/ws2/memory/percent-used-"+date+" /home/ws1/autoscale/data/ws2")
                fileSecMem = open ('/home/ws1/autoscale/data/ws2/percent-used-'+date,"r")
                lineList2Mem = fileSecMem.readlines()
                fileSecMem.close()
                percentage2Mem=[]
                records2Mem = lineList2Mem[meanConf:]
                for rec in records2Mem:
                        percentage2Mem.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentTwoMem =statistics.mean(percentage1Mem)
                resExe = os.system("scp ws1@192.168.56.4:/var/lib/collectd/csv/ws3/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws3")
                fileThird = open ('/home/ws1/autoscale/data/ws3/percent-user-'+date,"r")
                lineList3 = fileThird.readlines()
                fileThird.close()
                percentage3=[]
                records3 = lineList3[meanConf:]
                for rec in records3:
                        percentage3.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentThree =statistics.mean(percentage3)
                resExe = os.system("scp ws1@192.168.56.4:/var/lib/collectd/csv/ws3/memory/percent-used-"+date+" /home/ws1/autoscale/data/ws3")
                fileThirdMem = open ('/home/ws1/autoscale/data/ws2/percent-used-'+date,"r")
                lineList3Mem = fileThirdMem.readlines()
                fileThirdMem.close()
                percentage3Mem=[]
                records3Mem = lineList3Mem[meanConf:]
                for rec in records3Mem:
                        percentage3Mem.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentThreeMem =statistics.mean(percentage3Mem)
                print(finalPercentOne)
                print(finalPercentOneMem)
                print("total percent for VM1: ", (coeficient*finalPercentOne)+(coeficient*finalPercentOneMem))
                print(finalPercentTwo)
                print(finalPercentTwoMem)
                print("total percent for VM2: ", (coeficient*finalPercentTwo)+(coeficient*finalPercentTwoMem))
                print(finalPercentThree)
                print(finalPercentThreeMem)
                print("total percent for VM3: ", (coeficient*finalPercentThree)+(coeficient*finalPercentThreeMem))
                if ((coeficient*finalPercentOne)+(coeficient*finalPercentOneMem) <= 50) and ((coeficient*finalPercentTwo)+(coeficient*finalPercentTwoMem) <= 50) and ((coeficient*finalPercentThree)+(coeficient*finalPercentThreeMem) <= 50):
                        res= open("/home/ws1/autoscale/result/res.txt","w+")
                        res.write("OFF WS3")
                        res.close()
                        thirdR = True
                time.sleep(sleepTime)
        elif thirdR == True and fourthR == False:
                resExe = os.system("scp ws1@192.168.56.3:/var/lib/collectd/csv/ws1/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws1")
                fileFirst = open ('/home/ws1/autoscale/data/ws1/percent-user-'+date,"r")
                lineList1 = fileFirst.readlines()
                fileFirst.close()
                percentage1=[]
                records1 = lineList1[meanConf:]
                for rec in records1:
                        percentage1.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentOne =statistics.mean(percentage1)
                resExe = os.system("scp ws1@192.168.56.3:/var/lib/collectd/csv/ws1/memory/percent-used-"+date+" /home/ws1/autoscale/data/ws1")
                fileFirstMem = open ('/home/ws1/autoscale/data/ws1/percent-used-'+date,"r")
                lineList1Mem = fileFirstMem.readlines()
                fileFirstMem.close()
                percentage1Mem=[]
                records1Mem = lineList1Mem[meanConf:]
                for rec in records1Mem:
                        percentage1Mem.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentOneMem =statistics.mean(percentage1Mem)
                resExe = os.system("scp ws1@192.168.56.2:/var/lib/collectd/csv/ws2/cpu-0/percent-user-"+date+" /home/ws1/autoscale/data/ws2")
                fileSec = open ('/home/ws1/autoscale/data/ws2/percent-user-'+date,"r")
                lineList2 = fileSec.readlines()
                fileSec.close()
                percentage2=[]
                records2 = lineList2[meanConf:]
                for rec in records2:
                        percentage2.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentTwo =statistics.mean(percentage2)
                resExe = os.system("scp ws1@192.168.56.2:/var/lib/collectd/csv/ws2/memory/percent-used-"+date+" /home/ws1/autoscale/data/ws2")
                fileSecMem = open ('/home/ws1/autoscale/data/ws2/percent-used-'+date,"r")
                lineList2Mem = fileSecMem.readlines()
                fileSecMem.close()
                percentage2Mem=[]
                records2Mem = lineList2Mem[meanConf:]
                for rec in records2Mem:
                        percentage2Mem.append(float(rec.rstrip('\n').split(',')[1]))
                finalPercentTwoMem =statistics.mean(percentage1Mem)
                print(finalPercentOne)
                print(finalPercentOneMem)
                print("total percent for VM1: ", (coeficient*finalPercentOne)+(coeficient*finalPercentOneMem))
                print(finalPercentTwo)
                print(finalPercentTwoMem)
                print("total percent for VM2: ", (coeficient*finalPercentTwo)+(coeficient*finalPercentTwoMem))
                if ((coeficient*finalPercentOne)+(coeficient*finalPercentOneMem) <= 40) and ((coeficient*finalPercentTwo)+(coeficient*finalPercentTwoMem) <= 40):
                        res= open("/home/ws1/autoscale/result/res.txt","w+")
                        res.write("OFF WS2")
                        res.close()
                        firstR = False
                        secondR = False
                        thirdR = False
                time.sleep(sleepTime)
