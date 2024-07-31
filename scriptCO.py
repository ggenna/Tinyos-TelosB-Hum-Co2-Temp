
import time
import sys
import serial
import select
import binascii
import struct
import array

#import MySQLdb, MySQLdb.cursors
import urllib2, httplib
import time, datetime
import logging, logging.handlers
import re
import signal
import os
import csv
import argparse
import urlparse

#import MySQLdb
#ser = serial.Serial( '/dev/ttyUSB0', 115000, timeout=15 )
header=8
headerbuffer=bytearray(header)
payload=27
payloadbuffer=bytearray(payload)
startbyteHEADER=2
lastbyteheader=startbyteHEADER+header-1
startbytePAYLOAD=lastbyteheader+1
lastbytepayload=startbytePAYLOAD+payload-1



VALOREConv1=int(0)
VALOREConv2=float(0.00000)
VALOREConv3=float(0.00000)
VALOREConv4=float(0.00000)
VALOREConv5=float(0.00000)
VALOREConv6=float(0.00000)

try:
        ser = serial.Serial('/dev/ttyUSB0',115200, timeout=15)  # Open COM5, 5 second timeout 
        
except:
        print "Could not open serial port: ", sys.exc_info()[0]
        sys.exit(2)


#conn = MySQLdb.connect( host='localhost', db='emoncms', user='root', passwd='' )
#curs = conn.cursor()



# insert code here to parse the string s
# and assign values to all variables
# (humidity, sht15temp, scp1000tempC, scp1000press, scp1000tempF, temt6000light, battery))






while 1:
  try:
    ser.flushInput()
    s = ser.readline()
    headerbuffer=bytearray(header)
    payloadbuffer=bytearray(payload) 
    VALORE=bytearray(2)
    
    countH=0
    countP=0
    print len(s)
    if (s is not None) and (38 < len(s)) and (41 > len(s)):
	    
	    print s[7].encode('HEX')
	    print s.encode('hex') #How do I get the most recent line sent from the device?

   	    
   	    for index in range(startbyteHEADER,lastbyteheader):	
   	    	headerbuffer[countH]= bytes(s[index])
   	    	countH +=1  
   	    for index in range(startbytePAYLOAD,lastbytepayload):	
   	    	payloadbuffer[countP]= bytes(s[index])
   	    	countP +=1
   	    
   	    print "header"  
    	    print headerbuffer[5]
            print countH
            print "payload"
            print payloadbuffer[0]
            
            
             #node
            VALORE=bytearray(1) 
            VALORE[0]= headerbuffer[4]
        
            
            VALOREConv1= int(VALORE[0])
           
            
            #temperatura
            VALORE=bytearray(2)
            VALORE[1]= payloadbuffer[13]
            VALORE[0]= payloadbuffer[14]
            
            VALOREConv2= int(int(VALORE[0]) + int(VALORE[1] << 8)) * float(0.01) - float(39.6)
            
           # umidita
            VALORE=bytearray(2)
            VALORE[1]= payloadbuffer[15]
            VALORE[0]= payloadbuffer[16]
            
            #VALOREConv3= -float(2.0468)+float(0.0367) * int(int(VALORE[0]) + int(VALORE[1] << 8)) -float(1.5955) * pow(10,-6) *  pow(int(int(VALORE[0]) + int(VALORE[1] << 8)),2)
           
            VALOREConv3= -float(4.0)+float(0.0405) * int(int(VALORE[0]) + int(VALORE[1] << 8)) -float(2.8) * pow(10,-6) *  pow(int(int(VALORE[0]) + int(VALORE[1] << 8)),2)
            
           
            
            
        # Prepare URL string of the form
        # 'http://domain.tld/emoncms/input/bulk.json?apikey=12345&data=[[-10,10,1806],[-5,10,1806],[0,10,1806]]'
       # url_string = self._protocol+self._domain+self._path+"/input/bulk.json?apikey="+self._apikey+"&data="+data_string
           
  # url_string =" http://localhost/emoncms-master/input/post.json?node=1&json={temperature:16,humidity:20}&apikey=027087baa641ef8bc16fe7d9e11b784d"
  
  
  
            url_string =" http://localhost/emoncms-master/input/post.json?node="+str(VALOREConv1)+"&json={temperature:"+str(VALOREConv2)+",humidity:"+str(VALOREConv3)+"}&apikey=027087baa641ef8bc16fe7d9e11b784d"
            # Send data to server
            
            print url_string
            #result = urllib2.urlopen(url_string)
           
            print "risultato"
            print result
#        c = ser.read()

                
  #  for line in ser.read():

       # print(str(count) + str(': ') + chr(line) )
       # count = count+1
  except KeyboardInterrupt:
         break

ser.close()

    
    
    
    
#curs.execute(
#    'insert into weatherdata '
#    '(humiditycol, sht15tempcol, scp1000tempccol, scp1000presscol, scp1000tempfcol, temt6000lightcol, batterycol) '
#    'values '
#    '(%s, %s, %s, %s, %s, %s, %s)',
#    (humidity, sht15temp, scp1000tempC, scp1000press, scp1000tempF, temt6000light, battery))

