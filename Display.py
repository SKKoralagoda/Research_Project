import time
import sys
import ImageProcess
import PeopleDetector
import CalculateTime
from Adafruit_CharLCD import Adafruit_CharLCD
from gpiozero import LED
import threading
import thread
peopleDetection = None

red = LED(20)
green = LED(21)
dontWalk = LED(2)

# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=26, en=19,
                       d4=13, d5=6, d6=5, d7=11,
                       cols=16, lines=2)

class DisplayTime:

    def __init__( self, GreenLightTime, RedLightTime, Line1 , FlashingDontWalk ):
         self.GreenLightTime = GreenLightTime
         self.RedLightTime = RedLightTime
         self.Line1 = Line1
         self.FlashingDontWalk = FlashingDontWalk

    def Dtime(self):
        red.off()
        if self.GreenLightTime != 0:   #GreenLight
            
            x =self.GreenLightTime
            green.on()
                  
            while x > 0:
                
                display = str(x)
                lcd.clear()
                lcd.message( self.Line1 +"\n " + display)
                  
                    
                if (x == 2):
                    thread.start_new_thread(DisplayTime.ThreadOneImageProcess, (self, 2, ) )   #1 second for image processing
                    
                if (x == 1):                    
                    DisplayTime.GreenLight(self)

                x -= 1                    
                time.sleep(1)
                dontWalk.off()
                lcd.clear()
                lcd.message("")

                if ((x == self.FlashingDontWalk) or (x < self.FlashingDontWalk)):
                    dontWalk.on()
                                    
        green.off()
        dontWalk.off()
        
        if self.RedLightTime != 0:  #RedLight
            x =self.RedLightTime
            
            red.on()
            while x > 0:
                display = str(x)
                lcd.clear()
                lcd.message( self.Line1 +"\n " + display)
                x -= 1
                time.sleep(1)
                
                lcd.clear()
                lcd.message("")
        red.off()

    def ThreadOneImageProcess(self, time):
        #print "in"
        PeopleDetect = ImageProcess.detect()
        #print "Imsgrprocess",PeopleDetect
        
        global peopleDetection
        peopleDetection = PeopleDetect
        #print "global", peopleDetection
        thread.exit()
        

    def GreenLight(self):
        import time
        global peopleDetection
        time.sleep(1.5)
        print "People detection of road crossing:", peopleDetection
    
        if ((peopleDetection == None) or (peopleDetection == 0)):
            x = 1
            while x > 0:
                display = str(x)
                lcd.clear()
                lcd.message( self.Line1 +"\n " + display)
                x -= 1    
                time.sleep(1)
                dontWalk.off()
                lcd.clear()
                lcd.message("")

                if((x == self.FlashingDontWalk) or (x < self.FlashingDontWalk)):
                    dontWalk.on()

        else:
            print '\n' + '\n' + "--Detect People Crossing--"
            print '\n' + "Added Extra Time: 5s"
            print "==============================="
                        
            x = 5
            while x > 0:
                
                display = str(x)
                lcd.clear()
                lcd.message( "Extra Time" +"\n " + display)
                x -= 1    
                time.sleep(1)
                dontWalk.off()
                lcd.clear()
                lcd.message("")

                if((x == self.FlashingDontWalk) or (x < self.FlashingDontWalk)):
                    dontWalk.on()
            
    
    def RedLight(self):
        
        red.on()
        lcd.clear()
        lcd.message( self.Line1 +"\n ")

        peopleDetect = PeopleDetector.PeopleDetector()
        peopleDetect.RedlightOnMode()
        red.off()
