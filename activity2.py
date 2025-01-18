class parent:
     def __init__(self,name,id):
            self.name = name
            self.id = id
     def display(self): 
            print(self.name)
            print(self.id)
class employe(parent):
     def __init__(self,name,id,position,salary):
      self.position = position
      self.salary = salary
      super().__init__(name,id)
a = employe("pengiun",18591,"intern",30,000)
a.display()
print(a.salary)
print(a.position)