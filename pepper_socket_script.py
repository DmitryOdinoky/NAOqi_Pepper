import time
import qi
import sys
import socket

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)



    def onLoad(self):

        SERVER_IP = '192.168.4.12'
        PORT = 8080
        SIZE = 1024
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        self.s.connect((SERVER_IP,PORT))
        self.s.send('prev')
        time.sleep(0.5)
        pass




    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box# -*- coding: utf-8 -*-

