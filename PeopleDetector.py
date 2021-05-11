from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time
import PerformanceTest
import Main

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pir = MotionSensor(4)

GPIO.setup(3,GPIO.OUT)




class PeopleDetector:
    session = 1 #Count PIR ACTIVE time : When it exceed 10s calls main
    
    def PIRDetection(object):
        start_time = time.time()
        if pir.motion_detected:     
            GPIO.output(3,GPIO.HIGH)
            print ""
            print "--------People Detected--------"
            #Performance Testing
            timeTaken = time.time() - start_time
            timeTakenMs = round(timeTaken * 1000 , 1)
            PerformanceTest.setPeopleDetectionTime(timeTakenMs)
            
            return 1
        else:
            GPIO.output(3,GPIO.LOW)
            print "----No Any People Detected-----"
            PerformanceTest.setPeopleDetectionTime(0)
            return 0
        
    def sleepMode(self):
            if pir.motion_detected:
                print "----Detected:People Entering---" 
                app = Main.Application()
                app.main()
            else:
                i = 1
                while i < 2:
                    time.sleep(i)    
                    print "PIR ACTIVE"                  
                    PeopleDetector.sleepMode(self)
                    i = i + 1

                    
    def RedlightOnMode(self): #People Avaliability = 0 , Vehicle Avaliability = 1 
            if pir.motion_detected:
                print "----Detected:People Entering---" 
                app = Main.Application()
                app.main()
            else:
                i = 1
                while i < 2:
                    time.sleep(i)    
                    print "PIR ACTIVE :RED LIGHT ON"
                    PeopleDetector.session = PeopleDetector.session+1
                    if(PeopleDetector.session == 10):
                        print "Call Main"
                        PeopleDetector.session = 1
                        app = Main.Application()
                        app.main()
                        
                    PeopleDetector.RedlightOnMode(self)
                    i = i + 1
