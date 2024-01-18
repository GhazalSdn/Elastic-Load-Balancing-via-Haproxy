#!/usr/bin/env python

import subprocess
import datetime
import time
import statistics

cpu_weight = 0.5
mem_weight = 0.5

t = datetime.datetime.now()
date = (str(t))[0:10]
sender1 = "sara@192.168.56.5:/var/lib/collectd/csv/vmp1"
sender2 = "sara@192.168.56.7:/var/lib/collectd/csv/vmp2"
sender3 = "sara@192.168.56.8:/var/lib/collectd/csv/vmp3"

vm2 = False
vm3 = False

subprocess.run(["mkdir", "-p", "/home/sara/percentage_1"])
subprocess.run(["mkdir", "-p", "/home/sara/percentage_2"])
subprocess.run(["mkdir", "-p", "/home/sara/percentage_3"])

while True:

    f = open("/home/sara/script.sh", "w")
    f.write("")
    f.close()

    if vm3 == False:
        subprocess.run(["scp", sender1 + "/cpu-0/percent-user-" + date, "/home/sara/percentage_1"])
        f1 = open("/home/sara/percentage_1/percent-user-" + date, "r")
        lineList1 = f1.readlines()
        f1.close()
        records1 = lineList1[-12:]
        percentage1 = []
        for rec in records1:
            percentage1.append(float(rec.rstrip('\n').split(',')[1]))

        subprocess.run(["scp", sender1 + "/memory/percent-used-" + date, "/home/sara/percentage_1"])
        f1_2 = open("/home/sara/percentage_1/percent-used-" + date, "r")
        lineList1_2 = f1_2.readlines()
        f1_2.close()
        records1_2 = lineList1_2[-12:]
        percentage1_2 = []
        for rec in records1_2:
            percentage1_2.append(float(rec.rstrip('\n').split(',')[1]))
        finalPercentOne = cpu_weight * statistics.mean(percentage1) + mem_weight * statistics.mean(percentage1_2)

        if vm2 == False:
            if finalPercentOne > 80:
                f = open("/home/sara/script.sh", "w")
                f.write("#!/bin/bash\n")
                f.write("VBoxManage startvm VMp2")
                f.close()
                vm2 = True

        else:
            subprocess.run(["scp", sender2+"/cpu-0/percent-user-"+date, "/home/sara/percentage_2"])
            f2 = open("/home/sara/percentage_2/percent-user-" + date, "r")
            lineList2 = f2.readlines()
            f2.close()
            records2 = lineList2[-12:]
            percentage2 = []
            for rec in records2:
                percentage2.append(float(rec.rstrip('\n').split(',')[1]))

            subprocess.run(["scp", sender2 + "/memory/percent-used-" + date, "/home/sara/percentage_2"])
            f2_2 = open("/home/sara/percentage_2/percent-used-" + date, "r")
            lineList2_2 = f2_2.readlines()
            f2_2.close()
            records2_2 = lineList2_2[-12:]
            percentage2_2 = []
            for rec in records2_2:
                percentage2_2.append(float(rec.rstrip('\n').split(',')[1]))
            finalPercentTwo = cpu_weight * statistics.mean(percentage2) + mem_weight * statistics.mean(percentage2_2)

            if (finalPercentOne + finalPercentTwo)/2 > 80:
                f = open("/home/sara/script.sh", "w")
                f.write("#!/bin/bash\n")
                f.write("VBoxManage startvm VMp3")
                f.close()
                vm3 = True

            elif (finalPercentOne + finalPercentTwo)/2 < 40:
                f = open("/home/sara/script.sh", "w")
                f.write("#!/bin/bash\n")
                f.write("VBoxManage controlvm VMp2 poweroff")
                f.close()
                vm2 = False

    else:       # vm3 == True
        subprocess.run(["scp", sender1 + "/cpu-0/percent-user-" + date, "/home/sara/percentage_1"])
        f1 = open("/home/sara/percentage_1/percent-user-" + date, "r")
        lineList1 = f1.readlines()
        f1.close()
        records1 = lineList1[-12:]
        percentage1 = []
        for rec in records1:
            percentage1.append(float(rec.rstrip('\n').split(',')[1]))
        subprocess.run(["scp", sender1 + "/memory/percent-used-" + date, "/home/sara/percentage_1"])
        f1_2 = open("/home/sara/percentage_1/percent-used-" + date, "r")
        lineList1_2 = f1_2.readlines()
        f1_2.close()
        records1_2 = lineList1_2[-12:]
        percentage1_2 = []
        for rec in records1_2:
            percentage1_2.append(float(rec.rstrip('\n').split(',')[1]))
        finalPercentOne = cpu_weight * statistics.mean(percentage1) + mem_weight * statistics.mean(percentage1_2)

        subprocess.run(["scp", sender2 + "/cpu-0/percent-user-" + date, "/home/sara/percentage_2"])
        f2 = open("/home/sara/percentage_2/percent-user-" + date, "r")
        lineList2 = f2.readlines()
        f2.close()
        records2 = lineList2[-12:]
        percentage2 = []
        for rec in records2:
            percentage2.append(float(rec.rstrip('\n').split(',')[1]))
        subprocess.run(["scp", sender2 + "/memory/percent-used-" + date, "/home/sara/percentage_2"])
        f2_2 = open("/home/sara/percentage_2/percent-used-" + date, "r")
        lineList2_2 = f2_2.readlines()
        f2_2.close()
        records2_2 = lineList2_2[-12:]
        percentage2_2 = []
        for rec in records2_2:
            percentage2_2.append(float(rec.rstrip('\n').split(',')[1]))
        finalPercentTwo = cpu_weight * statistics.mean(percentage2) + mem_weight * statistics.mean(percentage2_2)

        subprocess.run(["scp", sender3 + "/cpu-0/percent-user-" + date, "/home/sara/percentage_3"])
        f3 = open("/home/sara/percentage_3/percent-user-" + date, "r")
        lineList3 = f3.readlines()
        f3.close()
        records3 = lineList3[-12:]
        percentage3 = []
        for rec in records3:
            percentage3.append(float(rec.rstrip('\n').split(',')[1]))
        subprocess.run(["scp", sender3 + "/memory/percent-used-" + date, "/home/sara/percentage_3"])
        f3_2 = open("/home/sara/percentage_3/percent-used-" + date, "r")
        lineList3_2 = f3_2.readlines()
        f3_2.close()
        records3_2 = lineList3_2[-12:]
        percentage3_2 = []
        for rec in records3_2:
            percentage3_2.append(float(rec.rstrip('\n').split(',')[1]))
        finalPercentThree = cpu_weight * statistics.mean(percentage3) + mem_weight * statistics.mean(percentage3_2)

        if (finalPercentOne + finalPercentTwo + finalPercentThree)/3 < 50:
            f = open("/home/sara/script.sh", "w")
            f.write("#!/bin/bash\n")
            f.write("VBoxManage controlvm VMp3 poweroff")
            f.close()
            vm3 = False

    time.sleep(30)
