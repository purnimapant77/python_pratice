class student:
    def __init__(self,name , gpa):
        self.name=name
        self.gpa=gpa
    
    def is_topper(self):
        if self.gpa>3.6:
            print(f"{self.name} is a topper student.")
        else:
            print(f"{self.name} is not a topper student.")
            
student1=student("Purnima", 3.2)
student2=student("Rabi", 3.8)

student1.is_topper()
student2.is_topper()