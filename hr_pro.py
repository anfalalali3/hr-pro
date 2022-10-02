#Anfal alali
employee = []
manager = []
def get_options():
    return ["Show Employees", "Show Managers", "Add An Employee", "Add A Manager"]
def show_options(options):
    print()
    print("options:")
    for idx, option in enumerate (options, start=1):
        print (f"{idx}.{option}")
    print()

def get_user_option():
    show_options(options)
    choose = input("What would you like to do?")
    return choose

class Employee:
   #Employee class here
   def __init__(self, name, age, salary,employment_years):
        self.name = name 
        self.age = age 
        self.salary = salary 
        self.employment_years = employment_years

def get_annual_salary(self):
        self.salary = salary
        return salary * 12

    
        
        

    
    
    

class Manager(Employee):
    def __init__(self, name, age, salary,employment_years):
        super().__init__(self, name, age, salary,employment_years)
        self.bonus_percantage = bonus_percantage

    def get_bonus():
     return bonus_percantage * get_annual_salary()

    def __str__(self):
     return f"name: {self.name} , Age:  {self.age} , Salary: {self.salary} , working years:{get_annual_salary}"

def main():
    print("Welcome to HR Pro")
    get_options()
    print(f"what would you like to do?{get_user_option()}")
    if get_user_option() == 1 :
            return employee
    elif get_user_option() ==2:
            return manager
    elif get_user_option() ==3:
        return employee.append()
    elif get_user_option() ==4:
        return manager.append()
    
    name = employee.append(input(f"whats your name?{name}"))
    age = employee.append(input(f"whats your age?{age}"))
    salary = employee.append(input(f"How much your salary?{salary}"))
    print(f"Bonus percentage:{get_bonus()}")
    
    name = manager.append(input(f"whats your name?{name}"))
    age = manager.append(input(f"whats your age?{age}"))
    salary = manager.append(input(f"How much your salary?{salary}"))
    print(f"Bonus percentage:{get_bonus()}")



if __name__ == '__main__':
	main()
