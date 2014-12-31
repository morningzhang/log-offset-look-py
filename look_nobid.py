#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

s_counter={}
n_counter={}

def counter(counter,cat):
     try:
        counter[cat]=counter[cat]+1
     except:
        counter[cat]=1

def sorter(counter):
 return sorted(counter.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

def get_log_content(logFile):
    for line in open(logFile):
        try:
            if "300x250" in line and "USA" in line and "android" in line:
                 line=line.strip().split("=>")[1]
                 items=line.split("^")
                 partner=items[0].strip()
                 if partner=="smaato":
                    counter(s_counter,items[-2])
                 elif partner=="nexage":
                    counter(n_counter,items[-2])
        except:
            pass


def main(logFiles):
    for logFile in logFiles:
        get_log_content(logFile)

    print "=====smaato======"
    for item in sorter(s_counter):
        print item
    print "=====nexage======"
    for item in sorter(n_counter):
        print item

if __name__ == '__main__':
   main(sys.argv[1:])