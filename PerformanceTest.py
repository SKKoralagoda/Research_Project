import pickle

ambulanceDetectTime = None

def setImageProcessTime(timeTaken):
    
    values_dict = {1:timeTaken}
    pickle_out = open("ImageProcesTime.pickle","wb")
    pickle.dump(values_dict, pickle_out)
    pickle_out.close()

def getImageProcessTime():
    pickle_in = open("ImageProcesTime.pickle","rb")
    values_dict = pickle.load(pickle_in)
        
    testTime = values_dict[1]
    return testTime


def setVehicleDetectionTime(timeTaken):
    
    values_dict = {1:timeTaken}
    pickle_out = open("VehicleDetectTime.pickle","wb")
    pickle.dump(values_dict, pickle_out)
    pickle_out.close()
    

def getVehicleDetectionTime():
    pickle_in = open("VehicleDetectTime.pickle","rb")
    values_dict = pickle.load(pickle_in)
        
    testTime = values_dict[1]
    return testTime

def setPeopleDetectionTime(timeTaken):

    values_dict = {1:timeTaken}
    pickle_out = open("PeopleDetectTime.pickle","wb")
    pickle.dump(values_dict, pickle_out)
    pickle_out.close()

def getPeopleDetectionTime():
    pickle_in = open("PeopleDetectTime.pickle","rb")
    values_dict = pickle.load(pickle_in)
        
    testTime = values_dict[1]
    return testTime

def setPeopleCountTime(timeTaken):

    values_dict = {1:timeTaken}
    pickle_out = open("PeopleCountTime.pickle","wb")
    pickle.dump(values_dict, pickle_out)
    pickle_out.close()

def getPeopleCountTime():
    pickle_in = open("PeopleCountTime.pickle","rb")
    values_dict = pickle.load(pickle_in)
        
    testTime = values_dict[1]
    return testTime

def setTotalIRPIRTime(timeTaken):
    
    values_dict = {1:timeTaken}
    pickle_out = open("IrPirTime.pickle","wb")
    pickle.dump(values_dict, pickle_out)
    pickle_out.close()

def getTotalIRPIRTime():
    pickle_in = open("IrPirTime.pickle","rb")
    values_dict = pickle.load(pickle_in)
        
    testTime = values_dict[1]
    return testTime

def setAmbulanceDetectionTime(timeTaken):

    values_dict = {1:timeTaken}
    pickle_out = open("AmbulanceDetectTime.pickle","wb")
    pickle.dump(values_dict, pickle_out)
    pickle_out.close()

def getAmbulanceDetectionTime():
    pickle_in = open("AmbulanceDetectTime.pickle","rb")
    values_dict = pickle.load(pickle_in)
        
    testTime = values_dict[1]
    return testTime

def setDrawRectangleTime(timeTaken):

    values_dict = {1:timeTaken}
    pickle_out = open("RecTime.pickle","wb")
    pickle.dump(values_dict, pickle_out)
    pickle_out.close()

def getDrawRectangleTime():
    pickle_in = open("RecTime.pickle","rb")
    values_dict = pickle.load(pickle_in)
        
    testTime = values_dict[1]
    return testTime

def setCalGreenLightTime(timeTaken):

    values_dict = {1:timeTaken}
    pickle_out = open("CalGreenTime.pickle","wb")
    pickle.dump(values_dict, pickle_out)
    pickle_out.close()

def getCalGreenLightTime():
    pickle_in = open("CalGreenTime.pickle","rb")
    values_dict = pickle.load(pickle_in)
        
    testTime = values_dict[1]
    return testTime

def setOverallSystemTime(timeTaken):

    values_dict = {1:timeTaken}
    pickle_out = open("overRallTime.pickle","wb")
    pickle.dump(values_dict, pickle_out)
    pickle_out.close()


def getOverallSystemTTime():
    pickle_in = open("overRallTime.pickle","rb")
    values_dict = pickle.load(pickle_in)
    
    testTime = values_dict[1]
    return testTime

       
