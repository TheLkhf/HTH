# ability.py
import random

class Ability:


    
    def __init__(self, name, max_damage):
   	# implement code here
        self.name = "Omniman"
        self.max_damage = 100
print(max_damage)


    def attack(self,damage):
        '''Return a random value between 0 and max_damage'''
        self.damage = random.randint(0,max_damage)
	# implement code here


# testing!
if __name__ == "__main__":
    fireball = Ability("Fireball", 50)
    print(fireball.attack())
