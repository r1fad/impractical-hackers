import sys
import serial
import time
import re
from os.path import join, dirname
from datetime import datetime
from threading import Thread, Lock

# Globally accessible
# ser = serial.Serial('/dev/cu.usbmodem1411', 9600, timeout=5)

serial_lock = Lock()

def eventMonitoring():

    # Thread variables
    bad_apps = set(["facebook", "twitter", "netflix", "reddit", 
                    "quora", "messenger", "9gag", "instagram", "linkedin", "whatsapp"])

    # Receive events from Shell Script
    for line in sys.stdin: 
        event_string = re.sub("[^A-Za-z0-9]+", ' ', line.strip().lower()).split(" ")
  
        for keyword in event_string:
            if keyword in bad_apps:
                print ("Bad app - {}".format(keyword))
                serial_lock.acquire()
                # ser.write(bytes("a","UTF-8"))
                serial_lock.release()
            
if __name__ == "__main__":
    try:
        Thread(target=eventMonitoring).start()
    except:
        print ("Error: unable to start thread")

# how to run - python3 run.py
