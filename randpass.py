#!/usr/bin/python
# coding: utf-8

import sys,string,random
from signal import signal, SIGPIPE, SIG_DFL

signal(SIGPIPE,SIG_DFL)

def Run(self,arg):
    source = string.ascii_letters + string.digits + '!$%*+-[]{}?'
    print "".join(map(str,[random.choice(source) for i in range(int(arg))]))
            

    
if __name__ == "__main__":
    Run(sys.argv[1])
