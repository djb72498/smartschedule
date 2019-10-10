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
        self.w4 = .3 # -(|prefered end - actual end|)
        self.w5 = .5 # -(|prefered Total - acutal total|)

    #pass in list of all employees
    def updateEmployees(self, employeeList):
        self.employeeList = employeeList

    def calculate(self):
        employees = self.employeeList

        #establish problem
        prob = LpProblem("Schedule Employees", LpMaximize)
        
        #define variables
        avgEmpHap = LpVariable("empHap")
        avgHours = LpVariable("avgHours")

        #the sum of each employees vars with weights will equal that employees hapiness
        empHaps = [0]*len(employees)
        for i in range(len(employees)):
            empHaps[i] = LpVariable("empHap"+ str(i))
        
        #each employee gets their own set of variable for actual
        # Ex = (-w3*ΔStartTime) + (-w4*ΔEndTime) + (-w5*ΔTotalHours)
        employeeVars = [[0]*3]*len(employees)
        for i in range(len(employees)):
            employeeVars[i][0] = LpVariable("aStart" + str(i),0, 23) 
            employeeVars[i][1] = LpVariable("aEnd"+ str(i), 1, 24)
            employeeVars[i][2] = LpVariable("aTotal"+ str(i), 0 , 10) #will work between 0 and 10



        #add the objective function
        prob += (self.w1*avgEmpHap) + (-1*self.w2*(10-avgHours)) #do not want more than 10 hours

        #add constraints

        #Add contraints for each employees 
        for i in range(len(employees)):
            #this equation equals a given employees hapiness
            prob += (-1*self.w3*(employees[i].prefStart-employeeVars[i][0])) + (-1*self.w4*(employees[i].prefEnd-employeeVars[i][1])) + (-1*self.w5*(employees[i].prefTotalHours-employeeVars[i][2])) == empHaps[i]

        prob += (empHaps[0]+empHaps[1]+empHaps[2])/3 == avgEmpHap


        #prob += totalHours <= 40 #cant work him more than 40, and he preferes 10
        prob.solve()

        print("Status:", prob)
        print("Status:", LpStatus[prob.status])


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

