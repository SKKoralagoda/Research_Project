import RPi.GPIO as GPIO
import time
import PerformanceTest

First_IR = 17   #Green
Second_IR = 22  #Blue
Third_IR = 10   #Purple

GPIO.setmode(GPIO.BCM)
GPIO.setup(First_IR, GPIO.IN)
GPIO.setup(Second_IR, GPIO.IN)
GPIO.setup(Third_IR, GPIO.IN)

class PeopleCounter:
  
  def IRDetection(object):
    start_time = time.time()
    People  = 2
    
    First_IR_inputVal = GPIO.input(First_IR)
    Second_IR_inputVal = GPIO.input(Second_IR)
    Third_IR_inputVal = GPIO.input(Third_IR)

    ###
    if First_IR_inputVal == 0:
      People_count = People * 1
      
      if Second_IR_inputVal == 0:
        People_count = People * 2
        
      if Third_IR_inputVal == 0:
        People_count = People * 2
        
      if ((Second_IR_inputVal == 0) and (Third_IR_inputVal == 0)):
        People_count = People * 3
    ###
        
    ###
    if Second_IR_inputVal == 0:
      People_count = People * 1
       
      if First_IR_inputVal == 0:
        People_count = People * 2
      
      if Third_IR_inputVal == 0:
        People_count = People * 2
        
      if ((First_IR_inputVal == 0) and (Third_IR_inputVal == 0)):
        People_count = People * 3
    ###
      
    ###
    if Third_IR_inputVal == 0:
      People_count = People * 1
      
      if First_IR_inputVal == 0:
        People_count = People * 2
        
      if Second_IR_inputVal == 0:
        People_count = People * 2
        
      if ((First_IR_inputVal == 0) and (Second_IR_inputVal == 0)):
        People_count = People * 3
    ###
        
    ###
    if ((First_IR_inputVal == 1) and (Second_IR_inputVal == 1) and (Third_IR_inputVal == 1)):
      People_count = 0
    ###

        
    ### Check
    if (People_count == 0):
      print "No people"
      PerformanceTest.setPeopleCountTime(0)
      return 0
    
    else:     
      print "Number of People :", People_count      
      print ""
      print "-------------------------------"
      print ""
      
      #Performance Testing for one IR sensor
      timeTaken = time.time() - start_time
      timeTakenMs = round(timeTaken * 1000 , 1)
      PerformanceTest.setPeopleCountTime(timeTakenMs)     
      return People_count
