class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f"Employee Info: Firstname: {self.first}; Lastname: {self.last}; Pay: {self.pay}"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('First', 'Employee', 10000)
emp_2 = Employee('Other', 'Employee', 50000)

print(repr(emp_1))
print(emp_1)
print(emp_1 + emp_2)
print(len(emp_1))



### Decorator
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('Future', 'SDE')
print(emp_1.fullname)
emp_1.fullname = "Love Python"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname


