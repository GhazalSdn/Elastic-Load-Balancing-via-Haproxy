import subprocess
import time
import os.path

while True:
    subprocess.run(["scp", "sara@192.168.56.9:/home/sara/script.sh", "C:/Users/Sara/Desktop/scripts"])
    subprocess.call("C:/Users/Sara/Desktop/scripts/script.sh", shell=True)
    # if os.path.isfile("C:/Users/Sara/Desktop/scripts/script.sh"):
    #     subprocess.run(["rm", "-f", "C:/Users/Sara/Desktop/scripts/script.sh"])
    time.sleep(30)