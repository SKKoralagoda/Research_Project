#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 15, 2017 09:39:41 AM
import sys
import Main
import configurationGUI
import PerformanceTestGUII
import Configurations
import tkFileDialog
import cv2
import numpy as np
import PIL.Image

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import dashboard_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = IPCS_CB005916 (root)
    dashboard_support.init(root, top)
    root.mainloop()

w = None
def create_IPCS_CB005916(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = IPCS_CB005916 (w)
    dashboard_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_IPCS_CB005916():
    global w
    w.destroy()
    w = None


class IPCS_CB005916:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font16 = "-family {Times New Roman} -size 13 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("596x391+463+29")
        top.title("IPCS_CB005916")
        top.configure(background="#ffffff")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.19, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#f3f3f3")
        self.Frame1.configure(width=575)

        self.lblname = Label(self.Frame1)
        self.lblname.place(relx=0.19, rely=0.27, height=31, width=364)
        self.lblname.configure(background="#f3f3f3")
        self.lblname.configure(disabledforeground="#a3a3a3")
        self.lblname.configure(font=font16)
        self.lblname.configure(foreground="#000000")
        self.lblname.configure(text='''Intellegent Pedestrian Controlling System''')
        self.lblname.configure(width=364)

        def RunClick():
            app = Main.Application()
            app.main()


        self.btnRun = Button(top)
        self.btnRun.place(relx=0.29, rely=0.46, height=34, width=115)
        self.btnRun.configure(activebackground="#d9d9d9")
        self.btnRun.configure(activeforeground="#000000")
        self.btnRun.configure(background="#b0ffc5")
        self.btnRun.configure(disabledforeground="#a3a3a3")
        self.btnRun.configure(foreground="#000000")
        self.btnRun.configure(highlightbackground="#d9d9d9")
        self.btnRun.configure(highlightcolor="black")
        self.btnRun.configure(pady="0")
        self.btnRun.configure(text='''RUN''', command=RunClick)
        self.btnRun.configure(width=115)

        def ConfigClick():
            configurationGUI.vp_start_gui()
            

        self.btnConfig = Button(top)
        self.btnConfig.place(relx=0.57, rely=0.46, height=34, width=115)
        self.btnConfig.configure(activebackground="#d9d9d9")
        self.btnConfig.configure(activeforeground="#000000")
        self.btnConfig.configure(background="#d9d9d9")
        self.btnConfig.configure(disabledforeground="#a3a3a3")
        self.btnConfig.configure(foreground="#000000")
        self.btnConfig.configure(highlightbackground="#d9d9d9")
        self.btnConfig.configure(highlightcolor="black")
        self.btnConfig.configure(pady="0")
        self.btnConfig.configure(text='''CONFIGURATIONS''', command=ConfigClick)
        self.btnConfig.configure(width=115)

        def browsefunc():
            try:
                image = tkFileDialog.askopenfilename()
                fp = open(image,"rb")
                img = PIL.Image.open(fp)
                #img = cv2.imread(image,1)         
                #cv2.imwrite('/home/pi/Desktop/FYP_Implementation(CB005916)/FYP_Images/ProcessImage.jpg', img)
                img.save("/home/pi/Desktop/FYP_Implementation(CB005916)/FYP_Images/ProcessImage.jpg")
                
                print "Image Uploaded succesfully"
            except:
                print "Upload Error. Please upload an image"

        self.btnBrowseImage = Button(top)
        self.btnBrowseImage.place(relx=0.03, rely=0.92, height=24, width=110)
        self.btnBrowseImage.configure(activebackground="#ffffff")
        self.btnBrowseImage.configure(activeforeground="#000000")
        self.btnBrowseImage.configure(background="#ffffff")
        self.btnBrowseImage.configure(disabledforeground="#a3a3a3")
        self.btnBrowseImage.configure(foreground="#000000")
        self.btnBrowseImage.configure(highlightbackground="#d9d9d9")
        self.btnBrowseImage.configure(highlightcolor="black")
        self.btnBrowseImage.configure(pady="0")
        self.btnBrowseImage.configure(text='''Browse Image >''', command = browsefunc)

        def Testbtn():
            PerformanceTestGUII.vp_start_gui()

        self.btnTest = Button(top)
        self.btnTest.place(relx=0.5, rely=0.92, height=25, width=200)
        self.btnTest.configure(activebackground="#d9d9d9")
        self.btnTest.configure(activeforeground="#bfeea4")
        self.btnTest.configure(background="#c6eccc")
        self.btnTest.configure(disabledforeground="#a3a3a3")
        self.btnTest.configure(foreground="#000000")
        self.btnTest.configure(highlightbackground="#d9d9d9")
        self.btnTest.configure(highlightcolor="black")
        self.btnTest.configure(pady="0")
        self.btnTest.configure(text='''Test Performance''' , command = Testbtn)
        self.btnTest.configure(width=107)


        self.lblwidth1 = Label(top)
        self.lblwidth1.place(relx=0.75, rely=0.74, height=21, width=101)
        self.lblwidth1.configure(anchor=NW)
        self.lblwidth1.configure(background="#ffffff")
        self.lblwidth1.configure(disabledforeground="#a3a3a3")
        self.lblwidth1.configure(foreground="#000000") 
        self.lblwidth1.configure(text= '''Road Width''')
        self.lblwidth1.configure(width=101)

        self.lblwidth = Label(top)
        self.lblwidth.place(relx=0.9, rely=0.74, height=21, width=101)
        self.lblwidth.configure(anchor=NW)
        self.lblwidth.configure(background="#ffffff")
        self.lblwidth.configure(disabledforeground="#a3a3a3")
        self.lblwidth.configure(foreground="#000000")
        config = Configurations.Configuration()
        self.lblwidth.configure(text=config.getcWidth())
        self.lblwidth.configure(width=101)


        self.lblLength1_ = Label(top)
        self.lblLength1_.place(relx=0.75, rely=0.79, height=21, width=101)
        self.lblLength1_.configure(activebackground="#ffffff")
        self.lblLength1_.configure(activeforeground="black")
        self.lblLength1_.configure(anchor=NW)
        self.lblLength1_.configure(background="#ffffff")
        self.lblLength1_.configure(disabledforeground="#a3a3a3")
        self.lblLength1_.configure(foreground="#000000")
        self.lblLength1_.configure(highlightbackground="#d9d9d9")
        self.lblLength1_.configure(highlightcolor="black")
        self.lblLength1_.configure(text='''Road Length''')
        self.lblLength1_.configure(width=101)

        self.lblLength_ = Label(top)
        self.lblLength_.place(relx=0.9, rely=0.79, height=21, width=101)
        self.lblLength_.configure(activebackground="#ffffff")
        self.lblLength_.configure(activeforeground="black")
        self.lblLength_.configure(anchor=NW)
        self.lblLength_.configure(background="#ffffff")
        self.lblLength_.configure(disabledforeground="#a3a3a3")
        self.lblLength_.configure(foreground="#000000")
        self.lblLength_.configure(highlightbackground="#d9d9d9")
        self.lblLength_.configure(highlightcolor="black")
        self.lblLength_.configure(text=config.getcLength())
        self.lblLength_.configure(width=101)


        self.lbldashboard = Label(top)
        self.lbldashboard.place(relx=0.39, rely=0.33, height=21, width=155)
        self.lbldashboard.configure(background="#ffffff")
        self.lbldashboard.configure(disabledforeground="#a3a3a3")
        self.lbldashboard.configure(foreground="#000000")
        self.lbldashboard.configure(text='''- Administrator Dashboard -''')

        def exitbtn():
            root.destroy()

        self.btnExit = Button(top)
        self.btnExit.place(relx=0.86, rely=0.92, height=24, width=69)
        self.btnExit.configure(activebackground="#d9d9d9")
        self.btnExit.configure(activeforeground="#000000")
        self.btnExit.configure(background="#ee777a")
        self.btnExit.configure(disabledforeground="#a3a3a3")
        self.btnExit.configure(foreground="#000000")
        self.btnExit.configure(highlightbackground="#d9d9d9")
        self.btnExit.configure(highlightcolor="black")
        self.btnExit.configure(pady="0")
        self.btnExit.configure(text='''Exit''', command=exitbtn)
        self.btnExit.configure(width=69)






if __name__ == '__main__':
    vp_start_gui()


