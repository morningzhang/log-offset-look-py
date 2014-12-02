#!/usr/bin/python
# -*- coding: utf-8 -*-
import struct,sys,os
from threading import Timer

def get_offset_value(logFile):
    logFileParts=logFile.split("/")
    return struct.unpack(">Q",open("%s/.%s.offset"%("/".join(logFileParts[:-1]),logFileParts[-1])).read(8))[0]

def get_file_length(logFile):
    return os.stat(logFile).st_size

def main(logFiles,n):
  print("==================================")
  for logFile in logFiles:
    try:
        offset=get_offset_value(logFile)
    except:
        offset=0

    try:
        length=get_file_length(logFile)
    except:
        length=0

    if length>0:
        precent=str(round(offset*100.0/length,2))
    else:
        precent="0.00"


    print("Name:%s => Offset : %d || Length : %d || O/L : %s%%"%(logFile.split("/")[-1],offset,length,precent))
  Timer(n, main,(logFiles,n)).start()

if __name__ == '__main__':
   main(sys.argv[1:-1],int(sys.argv[-1]))