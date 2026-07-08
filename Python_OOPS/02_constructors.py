class Employee:
    company = "Dell"

    def __init__(self,salary,name,bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"{self.name} salary is {self.salary} and its bond is {self.bond} months ")

e=Employee(34000,"Rhydam",6)
print(e.get_salary())
e.get_info()            