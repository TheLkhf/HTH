class hero:
    def_init_(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health





def battle(self, opponent)
    '''Fight another hero and randomly declare a winner'''
    self.opponent = opponent
     print(f"{self.name} battles {opponent}!")

     # Randomly choose winner
     winner = random.choice([self.opponent])
     print(f"{Winner} wins the battle!")



if_name_ == "__main__":
    my_hero = Hero("Moon Knight", 200)
    print(my_hero.name)              # Moon Knight
    print(my_hero.current_health)    # 200

    my_hero1 = Hero("Iron Man", 200)
    print(my_hero.name)              # Moon Knight
    print(my_hero.current_health)    # 200

    my_hero1.battle("Zombie Flash")

    class ability:
        def_init_(self, name, max_damage):
            self.name = name
            self.max_damage = int(max_damage)

            def attack(self):
                '''Returning a random value between 0 and max_damage'''
                return randomt.randint(0, self.max_damage)

            if_name_ == "__main__":
                fireball = Ability("Fireball", 50)
                print(fireball.attack())
