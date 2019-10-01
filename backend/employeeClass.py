#this class just stores information, should not involve any calculations
#all calculations in the scheduler class
class Employee:

    def __init__ (self):
        self.prefStart = -1
        self.prefEnd = -1
        self.prefTotalHours = -1
        self.prefCantWorkStart = -1
        self.prefCantWorkEnd = -1

    def setParams(self, preferedStart, preferedEnd,preferedTotalHours, cantWorkStart, cantWorkEnd):
        self.prefStart = preferedStart
        self.prefEnd = preferedEnd
        self.prefTotalHours = preferedTotalHours
        self.cantWorkStart = cantWorkStart
        self.cantWorkEnd = cantWorkEnd

    def setParamsFile(self, fileName):
        #somehow read from a file
        return 

