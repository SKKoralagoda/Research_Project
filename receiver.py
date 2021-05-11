from pi_switch import RCSwitchReceiver
import PerformanceTest
import time
    
receiver = RCSwitchReceiver()
receiver.enableReceive(2)

class EmbulanceDetection:

    def RFreceiver(object):
        start_time = time.time()
        session = 0
        while session < 20:
           
            received_value = 0
            
             
            received_value = receiver.getReceivedValue()
           
            
            if received_value == 1:
                print ""
                print "-------Ambulance Detected------"
                print ""
                print "Session:" ,session ,
                print "Received value: ",received_value
                print received_value, receiver.getReceivedBitlength(),
                print "bit"
                print "Protocol: ",receiver.getReceivedProtocol()
                print ""
                receiver.resetAvailable()
                del received_value
                #Performance Testing
                timeTaken = time.time() - start_time
                timeTakenMs = round(timeTaken * 1000 , 1)
                PerformanceTest.setAmbulanceDetectionTime(timeTakenMs)
                return 1
                
        
            session += 1
            print "num", session
            
        if session == 20:
            print "num", session
            del received_value
            print ""
            print "----Ambulance NOT Detected-----"
            print ""
            PerformanceTest.setAmbulanceDetectionTime(0)
            return 0      



