import sys
import Configurations
import Display
import datetime
import time
import PeopleDetector

class TimeManagements:

    def __init__( self, VA, PA, EA, GreenLightTime, RedLightTime, DontWalk):
         self.VA = VA
         self.PA = PA
         self.EA = EA
         self.GreenLightTime = GreenLightTime
         self.RedLightTime = RedLightTime
         self.DontWalk = DontWalk

    def TimeManagement(self) :

        #######
        if self.EA == 1:
            AmbulanceRedLightTime = self.RedLightTime + 10
            
            print "========================================================================"
            print '\n' + "----Turn on Red with Addtional Secounds----" 
            print ""
            print AmbulanceRedLightTime, "S" #When (Vehicle:0, People:0, Ambulance:1)
            print "========================================================================"
            
            time = Display.DisplayTime(0, AmbulanceRedLightTime, "RED LIGHT ON",  self.DontWalk)
            time.Dtime()

        
        ######
        if self.EA == 0:
            ###### 
            if self.VA == 0: #Vehicles not avaliable
            
                if self.PA == 0:
                    
                    print "========================================================================"
                    print '\n' + "Sleep Mode" + '\n' 
                    print '\n' + "Activate PIR Sensor" + '\n'
                    print "========================================================================"

                    peopleDetect = PeopleDetector.PeopleDetector()
                    peopleDetect.sleepMode()       
                         
                      
                if self.PA == 1:
                    
                    print "========================================================================"
                    print '\n' + "----Turn on Green----" 
                    print ""
                    print self.GreenLightTime, "S"
                    print "========================================================================"
                    
                    time = Display.DisplayTime(self.GreenLightTime, 0, "GREEN LIGHT ON", self.DontWalk)
                    time.Dtime()
                        
               
                    
            #######            
            if self.VA == 1: #Vehicles avaliable
            
                if self.PA == 0:
                    print "========================================================================"
                    print '\n' + "----Turn on Red-----"
                    print ""
                    #Activate PIR : When people incoming detects calls to main
                    print "========================================================================"
                     
                    time = Display.DisplayTime(0, self.RedLightTime, "RED LIGHT ON",  self.DontWalk)
                    time.RedLight()
                                       
                if self.PA == 1:                   
                    #check time (Two redligh if rush time = double red light) (then turn on red)
                    
                    config = Configurations.Configuration()
                    FRT_StartTime = config.getFirstRushTimeSlot_StartTime()
                    FRT_endTime = config.getFirstRushTimeSlot_EndTime()
                    now = datetime.datetime.now()
                    
                    print "------------------------------"
                    print '\n' + "Rush Start Time (hour):" , FRT_StartTime
                    print "Rush End Time (hour):" , FRT_endTime
                    print "Current Time (hour):" , now.hour
                    print "------------------------------"
                    print '\n' + '\t' + "Checking time"
                    print "------------------------------"
                    if int(FRT_StartTime) <= now.hour <= int(FRT_endTime): #CheckWithSystemTime - hours
                        RedRushTime = self.RedLightTime*2
                        
                       
                        print '\n' + "-------Rush Time Detected------" + '\n'
                        print ""
                        print "========================================================================"
                        print '\n' + "----Rush Time : Turn on Maxmimum Red light Time----"
                        print RedRushTime, "S"
                        print ""
                        time = Display.DisplayTime(0, RedRushTime, "RED LIGHT ON",  self.DontWalk)
                        time.Dtime()                   
                        print "========================================================================"


                        print "========================================================================"
                        print '\n' + "----Rush Time : Turn on Minimum Green Light Time----"
                        print 7, "S"
                        print ""
                        time = Display.DisplayTime(5, 0, "GREEN LIGHT ON",  self.DontWalk)
                        time.Dtime()                   
                        print "========================================================================"

                    else:
                        print "========================================================================"
                        print '\n' + "----Turn on Green-----"
                        print ""
                        print self.GreenLightTime, "S"
                        print ""
                        time = Display.DisplayTime(self.GreenLightTime, 0, "GREEN LIGHT ON",  self.DontWalk)
                        time.Dtime()
                        print "========================================================================"
                    

                        print "========================================================================"
                        print '\n' + "----Turn on Red-----"
                        print ""
                        print self.RedLightTime, "S"
                        print "========================================================================"
                     
                        time = Display.DisplayTime(0, self.RedLightTime, "RED LIGHT ON",  self.DontWalk)
                        time.Dtime()
                                    
