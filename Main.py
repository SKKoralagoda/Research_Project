import CalculateTime
import PeopleDetector
import PeopleCounter
import receiver
import vehicleDetector
import TimeManagement
import Configurations
import PerformanceTest



class Application:
    
    def config(object):
        
        config = Configurations.Configuration()
            
        print '\n' + "Configuration mode" + '\n'
        print "01: Road Width and Length" + '\n'
        print "02: Rush Times" + '\n'

        choice = int(raw_input("No :"))
            
        if choice == 01:
                config.setLengthWidth()
        if choice == 02:
                config.setFirstRushTimeSlot()
        
    
    def main(object):
        import time
        start_time = time.time()
        print '\n' + '\n' + '\t' + "Intelligent pedestrian crossing controlling system" + '\n'

              
        print '\n' + "Run"
        config = Configurations.Configuration()
        #config.setLogindetails()
        
        cLengh = config.getcLength()
        cwidth = config.getcWidth()
        i = 0
        while i < 1:
        #while True:
            embulance = receiver.EmbulanceDetection()
            EA = embulance.RFreceiver()
            print "Ambulance Avaliability:", EA
            print "-------------------------------"

            vehicle = vehicleDetector.VehicleDetector()
            VA = vehicle.UltrasonicWaveReceiver()
            print '\n' + "Vehicle Avaliability:", VA
            print "------------------------------"
            print ""

            peopleDetect = PeopleDetector.PeopleDetector()
            PA = peopleDetect.PIRDetection()
            print ""
            print "People Avaliability:", PA
            print "-------------------------------"

            print "==============================="

            if PA == 1:                
                peopleCount = PeopleCounter.PeopleCounter()
                count = peopleCount.IRDetection()
                
                timeCal = CalculateTime.CalculateTime(cLengh, cwidth, count)
                timeCal.displayvalue()

                GreenLight = timeCal.greenIntervalCalculation()
                dontWalk = int(round(timeCal.flashingDontWalk()))
                
                print '\n' , GreenLight
                GreenLightTime = int(round(GreenLight ,1))
                print '\n' + "GreenLight Time:", GreenLightTime
                print '\n' + "Flashing Dont Walk Starts:", dontWalk
                print ""
                print "==============================="
        
                RedLightTime = int(round(config.getRedLightTime(),1))
                print '\n' + "RedLight Time:", RedLightTime
                print "==============================="

                       
                management = TimeManagement.TimeManagements(VA, PA, EA, GreenLightTime, RedLightTime, dontWalk)
                management.TimeManagement()

                #Performance Testing
                timeTaken = time.time() - start_time
                timeTakenMs = round(timeTaken * 1000 , 1)
                PerformanceTest.setOverallSystemTime(timeTakenMs)
                

                #counr peopleDetectiontime
                peopleDetection =  PerformanceTest.getPeopleDetectionTime()
                peopleCount =  PerformanceTest.getPeopleCountTime()
                totalPeopleDetection = round(peopleDetection + peopleCount , 1)
                PerformanceTest.setTotalIRPIRTime(totalPeopleDetection)

                
            if PA == 0:
                
                RedLightTime = int(round(config.getRedLightTime(),1))
                print '\n' + "RedLight Time:", RedLightTime
                print "==============================="
                
                GreenLightTime = 0
 
                management = TimeManagement.TimeManagements(VA, PA, EA, GreenLightTime, RedLightTime, 0)
                management.TimeManagement()

                #Performance Testing
                timeTaken = time.time() - start_time
                timeTakenMs = round(timeTaken * 1000 , 1)
                PerformanceTest.setOverallSystemTime(timeTakenMs)
                
                print "Overall",PerformanceTest.getOverallSystemTTime()        
        i = i+1


