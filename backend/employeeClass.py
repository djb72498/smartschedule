#this class just stores information, should not involve any calculations
#all calculations in the scheduler class
class Employee:

    def __init__ (self):
        self.prefStart = -1
        self.prefEnd = -1
        self.prefTotalHours = -1

    def setParams(self, preferedStart, preferedEnd,preferedTotalHours):
        self.prefStart = preferedStart
        self.prefEnd = preferedEnd
        self.prefTotalHours = preferedTotalHours

    def setParamsFile(self, fileName):
        #somehow read from a file
        return 

