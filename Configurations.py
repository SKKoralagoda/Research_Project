import pickle
class Configuration:

    #####crosswalk

    def getcLength(self):
        pickle_in = open("lengthWidth.pickle","rb")
        values_dict = pickle.load(pickle_in)
        
        intcLength = float(values_dict[1])
        return intcLength

    def getcWidth(self):
        pickle_in = open("lengthWidth.pickle","rb")
        values_dict = pickle.load(pickle_in)
        
        intcWidth = float(values_dict[2])
        return intcWidth
      
    def setLengthWidth(self, cLength, cWidth):
        self.cLength = cLength
        self.cWidth = cWidth
        
        values_dict = {1:self.cLength, 2:self.cWidth}
        pickle_out = open("lengthWidth.pickle","wb")
        pickle.dump(values_dict, pickle_out)
        pickle_out.close()

    #####rush time
       
    def setFirstRushTimeSlot(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime

        timevalues_dict = {1:self.startTime, 2:self.endTime}
        pickle_out = open("RushTimes.pickle","wb")
        pickle.dump(timevalues_dict, pickle_out)
        pickle_out.close()

    def getFirstRushTimeSlot_StartTime(self):
        pickle_in = open("RushTimes.pickle","rb")
        timevalues_dict = pickle.load(pickle_in)
        
        startTime = timevalues_dict[1]
        return startTime

    def getFirstRushTimeSlot_EndTime(self):
        pickle_in = open("RushTimes.pickle","rb")
        timevalues_dict = pickle.load(pickle_in)
        
        endTime = timevalues_dict[2]
        return endTime

    #####red light

    def setRedLightTime(self, redlightTime):
        self.redlightTime = redlightTime
        
        values_dict = {1:self.redlightTime}
        pickle_out = open("redlight.pickle","wb")
        pickle.dump(values_dict, pickle_out)
        pickle_out.close()

    def getRedLightTime(self):
        pickle_in = open("redlight.pickle","rb")
        values_dict = pickle.load(pickle_in)
        
        redlight = float(values_dict[1])
        return redlight

    #####register

    def setLogindetails(self, userName, passWord):
        self.userName = userName
        self.passWord = passWord
        
        values_dict = {1:self.userName, 2:self.passWord}
        pickle_out = open("login.pickle","wb")
        pickle.dump(values_dict, pickle_out)
        pickle_out.close()

    def getUserName(self):
        pickle_in = open("login.pickle","rb")
        values_dict = pickle.load(pickle_in)
        
        username = values_dict[1]
        return username

    def getPassword(self):
        pickle_in = open("login.pickle","rb")
        values_dict = pickle.load(pickle_in)
        
        password = values_dict[2]
        return password

    #####walking spped
    
    def setPeopleWalkingSpeed(self, speed):
        self.speed = speed
        
        values_dict = {1:self.speed}
        pickle_out = open("wSpeed.pickle","wb")
        pickle.dump(values_dict, pickle_out)
        pickle_out.close()

    def getPeopleWalkingSpeedgetRedLightTime(self):
        pickle_in = open("wSpeed.pickle","rb")
        values_dict = pickle.load(pickle_in)
        
        redlight = float(values_dict[1])
        return redlight

    #####cropping
    
    def setCropping(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        values_dict = {1:self.x, 2:self.y, 3:self.w, 4:h}
        pickle_out = open("Cropping.pickle","wb")
        pickle.dump(values_dict, pickle_out)
        pickle_out.close()
    
