#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# helloworld.py
# Ein einfaches ”Hello World” Beispiel

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

def main(args) :
         #Jede Applikation muss über eine QApplication verfügen.
         app=QApplication(args)
         #ein Button
         button=QPushButton("Hello World !", None)
         #das man zeigt..
         button.show()
         #Endet die Applikation wenn alle Fenster geschlossen sind
         app.connect(app,SIGNAL("lastWindowClosed()"),app,SLOT("quit()"))   
         #Endet die Applikation wenn das Button geduckt wird
         app.connect(button, SIGNAL("clicked()"),app,SLOT("quit()"))   
         #hauptschlaufe der GUI Events
         app.exec_()

#Entry point
if __name__ == "__main__" :
   main(sys.argv)
