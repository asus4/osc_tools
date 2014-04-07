#! /usr/bin/env python
# coding: utf-8

'''
Osc Test Send Tool
'''

import osc
import Tkinter as Tk

class OscCommand:
    def __init__(self, address, port, ipaddress, params):
        print "params", params
        self.address = address
        self.port = port
        self.ipaddress = ipaddress
        self.params = params

    def __call__(self, event=None):
        print "send" , self.address, self.params, self.ipaddress.get(), self.port
        osc.sendMsg(self.address, self.params, self.ipaddress.get(), self.port)

class Frame(Tk.Frame):
    """ main Frame """

    def __init__(self, port, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('OSC Test Tool')
        self.port = port
        
        self.ipaddress = Tk.StringVar()
        self.ipaddress.set("127.0.0.1")

        # create ui
        # ip
        f = Tk.Frame(self, None)
        Tk.Label(f, text="IP : ").pack(side=Tk.LEFT)
        Tk.Entry(f, textvariable=self.ipaddress).pack(side=Tk.LEFT)
        f.pack(fill=Tk.X, expand=1)

        # general button
        f = Tk.Frame(self, None)
        Tk.Label(f, text="BUTTONS").grid(row=0, column=0, columnspan=3)
        Tk.Button(f, text="A", command=OscCommand("/A", self.port, self.ipaddress, [2])).grid(row=1, column=0)
        Tk.Button(f, text="B", command=OscCommand("/B", self.port, self.ipaddress, [0.6])).grid(row=1, column=1)
        Tk.Button(f, text="C", command=OscCommand("/C", self.port, self.ipaddress, ["foo"])).grid(row=1, column=2)
        f.pack(fill=Tk.X, expand=1)        

def main(port):
    osc.init()

    # start tkinter
    frame = Frame(port)
    frame.port = port
    frame.pack()
    frame.mainloop()


if __name__ == '__main__':
    import sys

    argvs = sys.argv
    argc  = len(argvs)

    main(int(argvs[1]))