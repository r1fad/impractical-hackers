import sys
import serial
import time
import re
from os.path import join, dirname
from datetime import datetime
from threading import Thread, Lock
from audio import play_audio

TIME_INTERVAL = 5

# Globally accessible
ser = serial.Serial('/dev/cu.usbmodem1411', 9600, timeout=5)

serial_lock = Lock()

def eventMonitoring():
    time_spent_procrastinating = 0
    prompts = 0

    bad_apps = set(["facebook", "twitter", "netflix", "reddit", 
                    "quora", "messenger", "9gag", "instagram", "linkedin", "whatsapp"])

    # Receive events from Shell Script
    for line in sys.stdin: 
        event_string = set(re.sub("[^A-Za-z0-9]+", ' ', line.strip().lower()).split(" "))
  
        bad_app = list(event_string.intersection(bad_apps))
        is_bad_app = len(bad_app) != 0
        if is_bad_app:
            time_spent_procrastinating += 1
            print ("Bad app - {} - time spent: {} - prompted: {}".format(bad_app[0], time_spent_procrastinating, prompts))
            
            serial_lock.acquire()
            ser.write(bytes("a","UTF-8"))
            serial_lock.release()
            
            if time_spent_procrastinating % TIME_INTERVAL == 0:
                prompts += 1
                thread = Thread(target=play_audio, args=(prompts, bad_app)).start()
        else:
            prompts = 0
            time_spent_procrastinating = 0


            
if __name__ == "__main__":
    try:
        Thread(target=eventMonitoring).start()
    except:
        print ("Error: unable to start thread")

# how to run - python3 run.py
