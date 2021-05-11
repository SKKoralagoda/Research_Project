#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 22, 2017 11:15:50 AM
import sys
import PerformanceTest
import Main

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

import PerformanceTestGUII_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = IPCS (root)
    PerformanceTestGUII_support.init(root, top)
    root.mainloop()

w = None
def create_IPCS(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = IPCS (w)
    PerformanceTestGUII_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_IPCS():
    global w
    w.destroy()
    w = None


class IPCS:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font11 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("568x598+360+102")
        top.title("IPCS")
        top.configure(background="#ffffff")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.37, rely=0.03, height=27, width=169)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''- Performance Testing -''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.29, rely=0.08, height=21, width=260)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Elapsed Time for each Functionalities''')

        def exitbtn():
            root.destroy()
            
        self.btnExit = Button(top)
        self.btnExit.place(relx=0.9, rely=0.92, height=34, width=39)
        self.btnExit.configure(activebackground="#d9d9d9")
        self.btnExit.configure(activeforeground="#cd7961")
        self.btnExit.configure(background="#fbb7b9")
        self.btnExit.configure(disabledforeground="#a3a3a3")
        self.btnExit.configure(foreground="#000000")
        self.btnExit.configure(highlightbackground="#d9d9d9")
        self.btnExit.configure(highlightcolor="black")
        self.btnExit.configure(pady="0")
        self.btnExit.configure(text='''Exit''', command = exitbtn)
        self.btnExit.configure(width=39)
            

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.04, rely=0.18, relheight=0.71, relwidth=0.7)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(width=395)

        self.lbaa1 = Label(self.Frame1)
        self.lbaa1.place(relx=0.18, rely=0.08, height=21, width=320)
        self.lbaa1.configure(activebackground="#f9f9f9")
        self.lbaa1.configure(activeforeground="black")
        self.lbaa1.configure(background="#ffffff")
        self.lbaa1.configure(disabledforeground="#a3a3a3")
        self.lbaa1.configure(foreground="#000000")
        self.lbaa1.configure(highlightbackground="#d9d9d9")
        self.lbaa1.configure(highlightcolor="black")
        self.lbaa1.configure(text='''Vehicle detection using ultra sonic sensor -------------''')

        self.Label35 = Label(self.Frame1)
        self.Label35.place(relx=0.18, rely=0.17, height=21, width=310)
        self.Label35.configure(activebackground="#f9f9f9")
        self.Label35.configure(activeforeground="black")
        self.Label35.configure(background="#ffffff")
        self.Label35.configure(disabledforeground="#a3a3a3")
        self.Label35.configure(foreground="#000000")
        self.Label35.configure(highlightbackground="#d9d9d9")
        self.Label35.configure(highlightcolor="black")
        self.Label35.configure(text='''People detection using PIR sensor  ---------------------''')

        self.Label41 = Label(self.Frame1)
        self.Label41.place(relx=0.18, rely=0.26, height=21, width=296)
        self.Label41.configure(activebackground="#f9f9f9")
        self.Label41.configure(activeforeground="black")
        self.Label41.configure(background="#ffffff")
        self.Label41.configure(disabledforeground="#a3a3a3")
        self.Label41.configure(foreground="#000000")
        self.Label41.configure(highlightbackground="#d9d9d9")
        self.Label41.configure(highlightcolor="black")
        self.Label41.configure(text='''People count using IR sensor ---------------------------''')

        self.Label42 = Label(self.Frame1)
        self.Label42.place(relx=0.18, rely=0.36, height=21, width=180)
        self.Label42.configure(activebackground="#f9f9f9")
        self.Label42.configure(activeforeground="black")
        self.Label42.configure(background="#ffffff")
        self.Label42.configure(disabledforeground="#a3a3a3")
        self.Label42.configure(foreground="#000000")
        self.Label42.configure(highlightbackground="#d9d9d9")
        self.Label42.configure(highlightcolor="black")
        self.Label42.configure(text='''People detection and count''')

        self.Label43 = Label(self.Frame1)
        self.Label43.place(relx=0.23, rely=0.4, height=21, width=290)
        self.Label43.configure(activebackground="#f9f9f9")
        self.Label43.configure(activeforeground="black")
        self.Label43.configure(background="#ffffff")
        self.Label43.configure(disabledforeground="#a3a3a3")
        self.Label43.configure(foreground="#000000")
        self.Label43.configure(highlightbackground="#d9d9d9")
        self.Label43.configure(highlightcolor="black")
        self.Label43.configure(text='''using PIR and IR sensor network --------------------''')

        self.Label44 = Label(self.Frame1)
        self.Label44.place(relx=0.16, rely=0.5, height=21, width=320)
        self.Label44.configure(activebackground="#f9f9f9")
        self.Label44.configure(activeforeground="black")
        self.Label44.configure(background="#ffffff")
        self.Label44.configure(disabledforeground="#a3a3a3")
        self.Label44.configure(foreground="#000000")
        self.Label44.configure(highlightbackground="#d9d9d9")
        self.Label44.configure(highlightcolor="black")
        self.Label44.configure(text='''Ambulance detection using RF signal receiving ---''')
        self.Label44.configure(width=297)

        self.Label45 = Label(self.Frame1)
        self.Label45.place(relx=0.18, rely=0.59, height=21, width=301)
        self.Label45.configure(activebackground="#f9f9f9")
        self.Label45.configure(activeforeground="black")
        self.Label45.configure(background="#ffffff")
        self.Label45.configure(disabledforeground="#a3a3a3")
        self.Label45.configure(foreground="#000000")
        self.Label45.configure(highlightbackground="#d9d9d9")
        self.Label45.configure(highlightcolor="black")
        self.Label45.configure(text='''Detect People in Image (Image Processing) -------''')

        self.Label46 = Label(self.Frame1)
        self.Label46.place(relx=0.17, rely=0.78, height=21, width=288)
        self.Label46.configure(activebackground="#f9f9f9")
        self.Label46.configure(activeforeground="black")
        self.Label46.configure(background="#ffffff")
        self.Label46.configure(disabledforeground="#a3a3a3")
        self.Label46.configure(foreground="#000000")
        self.Label46.configure(highlightbackground="#d9d9d9")
        self.Label46.configure(highlightcolor="black")
        self.Label46.configure(text='''Calculate Green light phase time -------------------''')
        self.Label46.configure(width=288)

        self.Label47 = Label(self.Frame1)
        self.Label47.place(relx=0.17, rely=0.88, height=21, width=304)
        self.Label47.configure(activebackground="#f9f9f9")
        self.Label47.configure(activeforeground="black")
        self.Label47.configure(background="#ffffff")
        self.Label47.configure(disabledforeground="#a3a3a3")
        self.Label47.configure(font=font9)
        self.Label47.configure(foreground="#000000")
        self.Label47.configure(highlightbackground="#d9d9d9")
        self.Label47.configure(highlightcolor="black")
        self.Label47.configure(text='''Overall system performance  -------------------''')

        self.Label48 = Label(self.Frame1)
        self.Label48.place(relx=0.03, rely=0.17, height=21, width=41)
        self.Label48.configure(activebackground="#f9f9f9")
        self.Label48.configure(activeforeground="black")
        self.Label48.configure(background="#ffffff")
        self.Label48.configure(disabledforeground="#a3a3a3")
        self.Label48.configure(foreground="#000000")
        self.Label48.configure(highlightbackground="#d9d9d9")
        self.Label48.configure(highlightcolor="black")
        self.Label48.configure(text='''8.1''')

        self.Label49 = Label(self.Frame1)
        self.Label49.place(relx=0.03, rely=0.36, height=21, width=41)
        self.Label49.configure(activebackground="#f9f9f9")
        self.Label49.configure(activeforeground="black")
        self.Label49.configure(background="#ffffff")
        self.Label49.configure(disabledforeground="#a3a3a3")
        self.Label49.configure(foreground="#000000")
        self.Label49.configure(highlightbackground="#d9d9d9")
        self.Label49.configure(highlightcolor="black")
        self.Label49.configure(text='''8.3''')
        self.Label49.configure(width=41)

        self.Label50 = Label(self.Frame1)
        self.Label50.place(relx=0.03, rely=0.26, height=21, width=41)
        self.Label50.configure(activebackground="#f9f9f9")
        self.Label50.configure(activeforeground="black")
        self.Label50.configure(background="#ffffff")
        self.Label50.configure(disabledforeground="#a3a3a3")
        self.Label50.configure(foreground="#000000")
        self.Label50.configure(highlightbackground="#d9d9d9")
        self.Label50.configure(highlightcolor="black")
        self.Label50.configure(text='''8.2''')
        self.Label50.configure(width=41)

        self.Label51 = Label(self.Frame1)
        self.Label51.place(relx=0.03, rely=0.08, height=21, width=41)
        self.Label51.configure(activebackground="#f9f9f9")
        self.Label51.configure(activeforeground="black")
        self.Label51.configure(background="#ffffff")
        self.Label51.configure(disabledforeground="#a3a3a3")
        self.Label51.configure(foreground="#000000")
        self.Label51.configure(highlightbackground="#d9d9d9")
        self.Label51.configure(highlightcolor="black")
        self.Label51.configure(text='''8.0''')

        self.Label52 = Label(self.Frame1)
        self.Label52.place(relx=0.03, rely=0.5, height=21, width=41)
        self.Label52.configure(activebackground="#f9f9f9")
        self.Label52.configure(activeforeground="black")
        self.Label52.configure(background="#ffffff")
        self.Label52.configure(disabledforeground="#a3a3a3")
        self.Label52.configure(foreground="#000000")
        self.Label52.configure(highlightbackground="#d9d9d9")
        self.Label52.configure(highlightcolor="black")
        self.Label52.configure(text='''9.0''')

        self.Label53 = Label(self.Frame1)
        self.Label53.place(relx=0.03, rely=0.59, height=21, width=41)
        self.Label53.configure(activebackground="#f9f9f9")
        self.Label53.configure(activeforeground="black")
        self.Label53.configure(background="#ffffff")
        self.Label53.configure(disabledforeground="#a3a3a3")
        self.Label53.configure(foreground="#000000")
        self.Label53.configure(highlightbackground="#d9d9d9")
        self.Label53.configure(highlightcolor="black")
        self.Label53.configure(text='''10.0''')

        self.Label54 = Label(self.Frame1)
        self.Label54.place(relx=0.03, rely=0.78, height=21, width=41)
        self.Label54.configure(activebackground="#f9f9f9")
        self.Label54.configure(activeforeground="black")
        self.Label54.configure(background="#ffffff")
        self.Label54.configure(disabledforeground="#a3a3a3")
        self.Label54.configure(foreground="#000000")
        self.Label54.configure(highlightbackground="#d9d9d9")
        self.Label54.configure(highlightcolor="black")
        self.Label54.configure(text='''11.0''')

        self.Label55 = Label(self.Frame1)
        self.Label55.place(relx=0.03, rely=0.88, height=21, width=41)
        self.Label55.configure(activebackground="#f9f9f9")
        self.Label55.configure(activeforeground="black")
        self.Label55.configure(background="#ffffff")
        self.Label55.configure(disabledforeground="#a3a3a3")
        self.Label55.configure(foreground="#000000")
        self.Label55.configure(highlightbackground="#d9d9d9")
        self.Label55.configure(highlightcolor="black")
        self.Label55.configure(text='''12.0''')

        self.Label56 = Label(self.Frame1)
        self.Label56.place(relx=0.03, rely=0.69, height=21, width=41)
        self.Label56.configure(activebackground="#f9f9f9")
        self.Label56.configure(activeforeground="black")
        self.Label56.configure(background="#ffffff")
        self.Label56.configure(disabledforeground="#a3a3a3")
        self.Label56.configure(foreground="#000000")
        self.Label56.configure(highlightbackground="#d9d9d9")
        self.Label56.configure(highlightcolor="black")
        self.Label56.configure(text='''10.1''')

        self.Label57 = Label(self.Frame1)
        self.Label57.place(relx=0.17, rely=0.69, height=21, width=301)
        self.Label57.configure(activebackground="#f9f9f9")
        self.Label57.configure(activeforeground="black")
        self.Label57.configure(background="#ffffff")
        self.Label57.configure(disabledforeground="#a3a3a3")
        self.Label57.configure(foreground="#000000")
        self.Label57.configure(highlightbackground="#d9d9d9")
        self.Label57.configure(highlightcolor="black")
        self.Label57.configure(text='''Draw rectangles on detected regions ---------------''')

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.76, rely=0.18, relheight=0.71, relwidth=0.22)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#e8e8e8")
        self.Frame2.configure(width=125)

        self.lbl80 = Label(self.Frame2)
        self.lbl80.place(relx=0.08, rely=0.08, height=21, width=94)
        self.lbl80.configure(background="#e8e8e8")
        self.lbl80.configure(disabledforeground="#a3a3a3")
        self.lbl80.configure(foreground="#000000")
        self.lbl80.configure(text=PerformanceTest.getVehicleDetectionTime())
        self.lbl80.configure(width=94)

        self.lbl81 = Label(self.Frame2)
        self.lbl81.place(relx=0.08, rely=0.17, height=21, width=94)
        self.lbl81.configure(background="#e8e8e8")
        self.lbl81.configure(disabledforeground="#a3a3a3")
        self.lbl81.configure(foreground="#000000")
        self.lbl81.configure(text=PerformanceTest.getPeopleDetectionTime())
        self.lbl81.configure(width=94)

        self.lbl82 = Label(self.Frame2)
        self.lbl82.place(relx=0.08, rely=0.26, height=21, width=94)
        self.lbl82.configure(background="#e8e8e8")
        self.lbl82.configure(disabledforeground="#a3a3a3")
        self.lbl82.configure(foreground="#000000")
        self.lbl82.configure(text=PerformanceTest.getPeopleCountTime())
        self.lbl82.configure(width=94)

        self.lbl84 = Label(self.Frame2)
        self.lbl84.place(relx=0.08, rely=0.38, height=21, width=94)
        self.lbl84.configure(background="#e8e8e8")
        self.lbl84.configure(disabledforeground="#a3a3a3")
        self.lbl84.configure(foreground="#000000")
        self.lbl84.configure(text=PerformanceTest.getTotalIRPIRTime())
        self.lbl84.configure(width=94)

        self.lbl90 = Label(self.Frame2)
        self.lbl90.place(relx=0.08, rely=0.49, height=21, width=94)
        self.lbl90.configure(background="#e8e8e8")
        self.lbl90.configure(disabledforeground="#a3a3a3")
        self.lbl90.configure(foreground="#000000")
        self.lbl90.configure(text=PerformanceTest.getAmbulanceDetectionTime())
        self.lbl90.configure(width=94)

        self.lbl10 = Label(self.Frame2)
        self.lbl10.place(relx=0.08, rely=0.59, height=21, width=94)
        self.lbl10.configure(background="#e8e8e8")
        self.lbl10.configure(disabledforeground="#a3a3a3")
        self.lbl10.configure(foreground="#000000")
        self.lbl10.configure(text=PerformanceTest.getImageProcessTime())
        self.lbl10.configure(width=94)

        self.lbl101 = Label(self.Frame2)
        self.lbl101.place(relx=0.08, rely=0.68, height=21, width=94)
        self.lbl101.configure(background="#e8e8e8")
        self.lbl101.configure(disabledforeground="#a3a3a3")
        self.lbl101.configure(foreground="#000000")
        self.lbl101.configure(text=PerformanceTest.getDrawRectangleTime())
        self.lbl101.configure(width=94)

        self.lbl12 = Label(self.Frame2)
        self.lbl12.place(relx=0.08, rely=0.78, height=21, width=94)
        self.lbl12.configure(background="#e8e8e8")
        self.lbl12.configure(disabledforeground="#a3a3a3")
        self.lbl12.configure(foreground="#000000")
        self.lbl12.configure(text=PerformanceTest.getCalGreenLightTime())
        self.lbl12.configure(width=94)

        self.lbl13 = Label(self.Frame2)
        self.lbl13.place(relx=0.08, rely=0.88, height=21, width=94)
        self.lbl13.configure(activebackground="#f9f9f9")
        self.lbl13.configure(activeforeground="black")
        self.lbl13.configure(background="#e8e8e8")
        self.lbl13.configure(disabledforeground="#a3a3a3")
        self.lbl13.configure(foreground="#000000")
        self.lbl13.configure(highlightbackground="#d9d9d9")
        self.lbl13.configure(highlightcolor="black")
        self.lbl13.configure(text=PerformanceTest.getOverallSystemTTime())

        self.Label30 = Label(top)
        self.Label30.place(relx=0.04, rely=0.15, height=21, width=66)
        self.Label30.configure(activebackground="#f9f9f9")
        self.Label30.configure(activeforeground="black")
        self.Label30.configure(background="#d9d9d9")
        self.Label30.configure(disabledforeground="#a3a3a3")
        self.Label30.configure(foreground="#000000")
        self.Label30.configure(highlightbackground="#d9d9d9")
        self.Label30.configure(highlightcolor="black")
        self.Label30.configure(text='''Test ID''')
        self.Label30.configure(width=66)

        
        self.Label31 = Label(top)
        self.Label31.place(relx=0.18, rely=0.15, height=21, width=86)
        self.Label31.configure(activebackground="#f9f9f9")
        self.Label31.configure(activeforeground="black")
        self.Label31.configure(background="#d9d9d9")
        self.Label31.configure(disabledforeground="#a3a3a3")
        self.Label31.configure(foreground="#000000")
        self.Label31.configure(highlightbackground="#d9d9d9")
        self.Label31.configure(highlightcolor="black")
        self.Label31.configure(text='''Test Scenario''')
        self.Label31.configure(width=86)

      
        self.Label32 = Label(top)
        self.Label32.place(relx=0.8, rely=0.15, height=21, width=86)
        self.Label32.configure(activebackground="#f9f9f9")
        self.Label32.configure(activeforeground="black")
        self.Label32.configure(background="#d9d9d9")
        self.Label32.configure(disabledforeground="#a3a3a3")
        self.Label32.configure(foreground="#000000")
        self.Label32.configure(highlightbackground="#d9d9d9")
        self.Label32.configure(highlightcolor="black")
        self.Label32.configure(text='''Time (ms)''')
        self.Label32.configure(width=86)


if __name__ == '__main__':
    vp_start_gui()


