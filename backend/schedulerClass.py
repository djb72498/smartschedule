#You need to pip3 install pulp to get this library
from pulp import *
import employeeClass 

class Scheduler:

    #pass in list of employee objects 
    def __init__ (self, employeeList):
        self.employeeList = employeeList
        
        #weights assosciated with Goodness equation
        self.weightEmpHap = 1
        self.weightTotalHours = 1

        #Weights assosciated with Emp Hapiness Equation
        #The 'actual' values are the parameters we are messing with
        self.w1 = .5 # -(|prefered start - actual start|)
        self.w2 = .5 # -(|prefered end - actual end|)
        self.w3 = .5 # -(|prefered Total - acutal total|)
        self.w4 = .5 # -(|cantWorkStart - actual cantWorkStart|)
        self.w5 = .5 # -(|cantWorkEnd - actual cantWorkEnd|)

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
        prob += (self.weightEmpHap * empHap) + (self.weightTotalHours * totalHours)

        #add constraints
        #right now empHap is defined by a single 
        prob += -1*self.w1*abs(employeeInfo.prefTotalHours-actualTotal) = empHap

        prob.solve()






if __name__ == "__main__":
    employee1 = employeeClass.Employee()
    employee1.setParams(12,18,6,0,10)

    employeeList = list()
    employeeList.append(employee1)

    newSched = Scheduler()

