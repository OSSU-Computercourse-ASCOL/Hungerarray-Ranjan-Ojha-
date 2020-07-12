#--------------------------------------------------------------------
# Exercise: Classes [building person]
#--------------------------------------------------------------------
import datetime

class Person(object):
    
    def __init__(self, name):
        '''Create a person called name'''
        self.name = name
        self.birthday = None
        self.lastName = name.split(" ")[-1]
    
    def __lt__(self, other):
        """Return True if self's name is lexicographically less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        else:
            return self.lastName < other.lastName
        
    def setBirthday(self, month, day, year):
        """sets self's birthday to birthdate"""
        self.birthday = datetime.date(year, month, day)
        
    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def getLastName(self):
        """Return self's last name"""
        return self.lastName

    def __str__(self):
        """Return self's name"""
        return self.name
    
    