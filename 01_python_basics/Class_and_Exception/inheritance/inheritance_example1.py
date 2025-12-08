# inheritance allow you to define a class that inherits all the methods and properties from another class.
# allow you to resuse the code and establish a relationship between different classes.



import datetime

class Player:
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        
    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.birth_year
    
    
class TennisPlayer(Player):
    pass


roger = TennisPlayer("roger", "federer", 1981)
print(roger.last_name)  

