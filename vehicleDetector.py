import RPi.GPIO as GPIO                    
import time
import PerformanceTest
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

First_TRIG = 23                               
First_ECHO = 24                                 

Second_TRIG = 7                               
Second_ECHO = 8 

GPIO.setup(First_TRIG,GPIO.OUT)                 
GPIO.setup(First_ECHO,GPIO.IN)

GPIO.setup(Second_TRIG,GPIO.OUT)                 
GPIO.setup(Second_ECHO,GPIO.IN)

class VehicleDetector:
  
  def UltrasonicWaveReceiver(object):
    start_time = time.time()
    
    GPIO.output(First_TRIG, False)                 # Frist ultraSonic Set TRIG as LOW
    print ""
    time.sleep(1)

    GPIO.output(Second_TRIG, False)                 # Second ultraSonic Set TRIG as LOW
    print ""
    time.sleep(1) 

    # First Ultra sonic
    GPIO.output(First_TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                            #Delay of 0.00001 seconds
    GPIO.output(First_TRIG, False)                 #Set TRIG as LOW

    while GPIO.input(First_ECHO)==0:               #Check whether the ECHO is LOW or not 
      First_pulse_start = time.time()              #Get time of LOW pulse

    while GPIO.input(First_ECHO)==1:               #Check whether the ECHO is HIGH or not
      First_pulse_end = time.time()                #Get time of HIGH pulse 

    First_pulse_duration = First_pulse_end - First_pulse_start           
    Frist_dis = (First_pulse_duration * 17150) #cm
    First_ft =  Frist_dis * 0.0328084;
    First_ftRound =  round(First_ft,2)
   

    # Second Ultra sonic
    GPIO.output(Second_TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                             #Delay of 0.00001 seconds
    GPIO.output(Second_TRIG, False)                 #Set TRIG as LOW

    while GPIO.input(Second_ECHO)==0:               #Check whether the ECHO is LOW or not 
      Second_pulse_start = time.time()              #Get time of LOW pulse

    while GPIO.input(Second_ECHO)==1:               #Check whether the ECHO is HIGH or not
      Second_pulse_end = time.time()                #Get time of HIGH pulse 

    Second_pulse_duration = Second_pulse_end - Second_pulse_start            
    Second_dis = (Second_pulse_duration * 17150) #cm
    second_ft = Second_dis * 0.0328084
    second_ftRound = round(second_ft,2)
    
    

    if ((First_ft < 3) or (second_ft < 3)):

        if(First_ft < second_ft):
          print "Ultrasonic Distance:",First_ftRound ,"ft"   
          print ""
          print "-------Vehicle Detected-------"
        
          #Performance Testing
          timeTaken = time.time() - start_time
          timeTakenMs = round(timeTaken * 1000 , 1)
          PerformanceTest.setVehicleDetectionTime(timeTakenMs)
          return 1

        if(First_ft > second_ft):
          print "Ultrasonic Distance:",second_ftRound ,"ft"   
          print ""
          print "-------Vehicle Detected-------"
        
          #Performance Testing
          timeTaken = time.time() - start_time
          timeTakenMs = round(timeTaken * 1000 , 1)
          PerformanceTest.setVehicleDetectionTime(timeTakenMs)
          return 1
      
    else:
        print "----No Any Vehicle Detected---" #display out of range
        PerformanceTest.setVehicleDetectionTime(0)
        return 0


#v = VehicleDetector()
#v.UltrasonicWaveReceiver()
