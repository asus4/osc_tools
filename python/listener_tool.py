#! /usr/bin/env python
# coding: utf-8

'''
Osc Test Listen Tool
'''

import osc

def main(port):
    osc.init()
    listener = osc.createListener("",port)

    import time

    while 1:
        time.sleep(0.1)
        osc.getOSC(listener)


if __name__ == '__main__':
    import sys

    argvs = sys.argv
    argc  = len(argvs)

    print sys.argv
    main(int(argvs[1]))