from __future__ import division
import PerformanceTest
import time


class CalculateTime:
   
   def __init__( self, cLength, cwidth, noOfPeople ):
      self.cLength = cLength
      self.cwidth = cwidth
      self.noOfPeople = noOfPeople
   
   def displayvalue( self ):
      print '\t' + "Crosswalk length : ", self.cLength
      print '\t' + "Crosswalk Width: ", self.cwidth
      print '\t' + "Estimated number of People: ", self.noOfPeople

   def greenIntervalCalculation(self):
      start_time = time.time()
      if self.cwidth > 10:
          answer = 3.2 + (self.cLength/3.5) + (2.7 * (self.noOfPeople / self.cwidth))

          #Performance Testing
          timeTaken = time.time() - start_time
          timeTakenMs = round(timeTaken * 1000 , 1)
          PerformanceTest.setCalGreenLightTime(timeTakenMs)
          
          return answer;  

      if self.cwidth == 10 or self.cwidth < 10:
          answer = 3.2 + (self.cLength/3.5) + ( 0.27 * self.noOfPeople )

          #Performance Testing
          timeTaken = time.time() - start_time
          timeTakenMs = round(timeTaken * 1000 , 1)
          PerformanceTest.setCalGreenLightTime(timeTakenMs)
          
          return answer;

   def redIntervalCalculation(self, pw):
      self.pw = pw
      
      redInterval = self.cLength / 3.5 + self.pw
      return redInterval


   def flashingDontWalk(self):
      
      redInterval = self.cLength / 3.5
      return redInterval
