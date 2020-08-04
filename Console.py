#!/usr/bin python

from tkinter import *
import LayoutStandard
import Windows

mainWin = Tk()
mainWin.title("Word2Vec")
mainWin.resizable(False,False)

layout = LayoutStandard.LayoutStandard(mainWin)
layout.bg.pack()

bgFrame = Windows.Windows(layout.bg, mainWin)
centerFrame = layout.center
bgFrame.logo()
mainWin.after(5000, bgFrame.logo.forget)
mainWin.after(5000, centerFrame.pack)

choiseFrame = Windows.Windows(centerFrame, mainWin)
choiseFrame.choise()



mainWin.mainloop()
