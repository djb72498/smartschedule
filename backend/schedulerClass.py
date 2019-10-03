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
        self.w3 = .5 # -(|prefered start - actual start|)
        self.w4 = .5 # -(|prefered end - actual end|)
        self.w5 = .5 # -(|prefered Total - acutal total|)

    #pass in list of all employees
    def updateEmployees(self, employeeList):
        self.employeeList = employeeList

    def calculate(self):
        employeeInfo = self.employeeList[0] #consider only one employee right now

        #establish problem
        prob = LpProblem("Schedule Employees", LpMaximize)
        
        #define variables
        empHap = LpVariable("Employee Hapiness")
        totalHours = LpVariable("Total Hours")
        
        actualTotal = LpVariable("total hours for employee")
        actualStart = LpVariable("employees actual start time")
        actualEnd = LpVariable("employees actual end time")

        #add the objective function
        prob += (self.w1 * empHap) + (self.w2 * totalHours)

        #add constraints
        for i in range(len(self.employeeList)):
            prob += (-1*self.w3*(employeeList[i].prefStart-actualStart)) + (-1*self.w4*(employeeList[i].prefEnd-actualEnd)) + (-1*self.w5*(employeeList[i].prefTotalHours-actualTotal)) == empHap

        #prob += totalHours <= 40 #cant work him more than 40, and he preferes 10

        prob.solve()

        print("Status:", LpStatus[prob.status])


if __name__ == "__main__":
    #create some employees
    employee1 = Employee()
    employee2 = Employee()
    employee3 = Employee()

    #Establish their prefered stuffs
    employee1.setParams(12,18,6,0,10)
    employee2.setParams(9,5,8,0,10)
    employee3.setParams(10,7,9,0,10)

    #create a list and add all of them to it
    employeeList = list()
    employeeList.append(employee1)
    employeeList.append(employee2)
    employeeList.append(employee3)

    #create a new schedule, then call calculate
    newSched = Scheduler(employeeList)
    newSched.calculate()

