#You need to pip3 install pulp to get this library
from pulp import *
from employeeClass import *


'''
Idea

Goodness = (W1*AvgEmployeeHappiness) + (W2*TotalHours)
                    |
                    |
                    |
                    \/
                    AvgEmployeeHapiness = (E1+E2+E3...En) / n
                                            |
                                            |
                                            |
                                            \/
                                            Ex = (-w3*ΔStartTime) + (-w4*ΔEndTime) + (-w5*ΔTotalHours)
'''

class Scheduler:

    #pass in list of employee objects 
    def __init__ (self, employeeList):
        self.employeeList = employeeList
        
        #weights assosciated with Goodness equation
        self.w1 = 1
        self.w2 = 1

        #Weights assosciated with Emp Hapiness Equation
        #The 'actual' values are the parameters we are messing with
        self.w3 = .1 # -(|prefered start - actual start|)
        self.w4 = .1 # -(|prefered end - actual end|)
        self.w5 = .5 # -(|prefered Total - acutal total|)

        self.employeeVars = list()

    #pass in list of all employees
    def updateEmployees(self, employeeList):
        self.employeeList = employeeList

    def calculate(self):
        employee = self.employeeList[0]

        #establish problem
        prob = LpProblem("Schedule Employees", LpMaximize)
        
        #define variables
        avgEmpHap = LpVariable("empHap")

        #the sum of each employees vars with weights will equal that employees hapiness
        empHaps = 0
        
        #each employee gets their own set of variable for actual
        employeeVars = [0]*3
        employeeVars[0] = LpVariable("aStart" + str(0),0, 23) 
        employeeVars[1] = LpVariable("aEnd"+ str(1), 1, 24)
        employeeVars[2] = LpVariable("aTotal"+ str(2), 0, 24) #will work between 0 and 10

        #add the objective function
        prob += (self.w1*avgEmpHap) 

        #add constraints
        #Add contraints for each employees 
        prob += (self.w5*(employee.prefTotalHours-employeeVars[2])) == empHaps #as this gets higher, employee gets happier b/c he's getting right hours
        prob += employee.prefStart <= employeeVars[0] #make sure times are within availability window
        prob += employee.prefEnd >= employeeVars[1]
        prob += employeeVars[1] - employeeVars[0] == employeeVars[2]


        prob += empHaps == avgEmpHap

        #prob += totalHours <= 40 #cant work him more than 40, and he preferes 10
        prob.solve()
        
        print(employeeVars[0].varValue)
        print(employeeVars[1].varValue)
        print(employeeVars[2].varValue)

        print("Status:", prob)
        print("Status:", LpStatus[prob.status])

    def printSched(self):
        print(self.employeeVars)
        '''
        for i in range(0,24):
            print(str(i)+":00 -> ", end = "")
            for j in range(len(self.employeeList)):
                if self.employeeVars[j][0] <= i and self.employeeVars[j][1] > i: #if current time greater than start time and less than end time
                    print("Emp"+str(j), end=" ")
                else:
                    print("   ", end = "")
            print("") # just to add a newline
        '''



if __name__ == "__main__":
    #create some employees
    employee1 = Employee()
    employee2 = Employee()
    employee3 = Employee()

    #Establish their prefered stuffs
    employee1.setParams(12,18,6)
    employee2.setParams(9,5,8)
    employee3.setParams(10,7,9)

    #create a list and add all of them to it
    employeeList = list()
    employeeList.append(employee1)
    employeeList.append(employee2)
    employeeList.append(employee3)

    #create a new schedule, then call calculate
    newSched = Scheduler(employeeList)
    newSched.calculate()
    newSched.printSched()

