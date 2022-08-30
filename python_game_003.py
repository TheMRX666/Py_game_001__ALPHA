from random import randint


class Hero():
    def __init__(self, name, class_hero):
        self.exp = 0
        self.class_hero = class_hero
        self.name = name
        self.level = 1
        self.health_potion = 1
        self.stamina_potion = 1
        self.sword=True
        if class_hero == "Fighter":
            self.health = 50*self.level
            self.stamina = 25*self.level
            self.power = 5*self.level
        elif class_hero == "Mage":
            self.health = 25*self.level
            self.stamina = 50*self.level
            self.power = 10*self.level
        
            
    def show_weapon(self):
        if self.sword == True:
            print("Do you have a sword")
        elif self.sword == False:
            print("You don't have a sword")
            
    def show_stat(self):
        print(f"""Name - {self.name}      LVL  -  {self.level}      EXP - {self.exp}
HP - {self.health*self.level}
SP - {self.stamina*self.level}
DP - {self.power*self.level}""")
        
    def add_exp(self, cout_exp):
        self.exp += cout_exp
        print(f"You get {cout_exp} EXP!!!")
        
    def level_up(self, cout_lvl):
        self.level += cout_lvl
        print("LEVEL UP!!!  To", cout_lvl, "LVL")
        
        
    def buy_level(self):
        if self.exp >= 100 + 20*self.level:
            self.exp -= 100 + 20*self.level
            self.level += 1
            print("You buy LeveL UP")
        else:
            print(f"You don't have a {100 + 20*self.level} EXP")
        
        
    def punch(self):
        if self.class_hero == "Fighter":
            self.punch = (self.power*self.level)*0.5
            self.stamina -=2
            if self.sword == True:
                self.punch = self.punch*1.2
        elif self.class_hero == "Mage":
            self.punch = (self.power*self.level)*0.5
            self.stamina -=2.2
            if self.sword == True:
                self.punch = self.punch*1.2
        print(f"You punch damage - {self.punch}")
        global punch_damage
        punch_damage = self.punch
        
        
    def heal_potion(self):
        if self.health_potion >0:
            if self.class_hero == "Fighter":
                if self.health*self.level <= 50*self.level - 65:
                    self.health += 5
                    print("You healed 65 health")
                    self.health_potion -=1
                else:
                    print("You have maximum health")
            elif self.class_hero == "Mage":
                if self.health*self.level <= 25*self.level - 65:
                    self.health += 5
                    print("You healed 65 health")
                    self.health_potion -=1
                else:
                    print("You have maximum health")
        else:
            print("You don't have a health potion")
            
            
    def energy_potion(self):
        if self.stamina_potion >0:
            if self.class_hero == "Fighter":
                if self.stamina*self.level <= 25*self.level - 65:
                    self.stamina += 5
                    print("You restored 65 stamina")
                    self.stamina_potion -=1
                else:
                    print("You have maximum stamina")
            elif self.class_hero == "Mage":
                if self.stamina*self.level <= 50*self.level - 65:
                    self.stamina += 5
                    print("You restored 65 stamina")
                    self.stamina_potion -=1
                else:
                    print("You have maximum stamina")
        else:
            print("You don't have a stamina potion")
            
            
    def dunge__get__damage(self, get_player_damage):
        self.health -= get_player_damage       
            
            
            
    def get_damage(self):
        self.health -= 5
        
 

class Mobs():
    def __init__(self, name, location):
        self.name = name
        if location == 1:
            location_id = randint(1,4)
        elif location == 2:
            location_id = randint(3,8)
        elif location == 3:
            location_id = randint(7,15)
        self.level = location_id  
            
            
            
        if name == "Slime":
            self.health = 5*self.level
            self.stamina = 7*self.level
            self.power = 2*self.level
        elif name == "Wolf":
            self.health = 10*self.level
            self.stamina = 15*self.level
            self.power = 3*self.level
        elif name == "Goblin":
            self.health = 20*self.level
            self.stamina = 25*self.level
            self.power = 5*self.level
        elif name == "Ork":
            self.health = 30*self.level
            self.stamina = 35*self.level
            self.power = 8*self.level
  
  
  
  
  
  
    def mob_show_stat(self):
        print(f"""Name - {self.name}      LVL  -  {self.level}
HP - {self.health*self.level}
SP - {self.stamina*self.level}
DP - {self.power*self.level}""")


    def dunge_get_damage(self, punch_damage):
        self.health -= punch_damage*0.1
        health_point_info = self.health
        return health_point_info



    def dunge_mob_punch(self):
        return self.power*0.5





#MAIN BLOCK


            
player_1 = Hero("Denis", "Mage")
player_1.show_stat()
player_1.level_up(12)
player_1.show_stat()
player_1.punch()
player_1.show_stat()


#slime_mob = Mobs("Slime", 1)
#wolf_mob = Mobs("Wolf", 1)
#goblin_mob = Mobs("Goblin", 1)
#ork_mob = Mobs("Ork", 1)


print("""


""")

while True:
    readline = input("What the next?    Type help to see commands\n")
    if readline == "help":
        print("""
Dunge  -  Go to the dungeon
Potion  -  Посмотреть зелья в инвентаре
Stat  - Посмотреть статистику
BuyLevel  - Level up for EXP
Weapon  -  Посмотреть оружие
End   -  Quit the game
Support   -  Technical support contacts
""")
        
    elif readline == "Dunge":
        print("You go to the dungeon")
        dunge__level__start = 1
        if dunge__level__start == 1:
            slime_mob = Mobs("Slime", 1)
            pvp_index = 0
            while pvp_index <= 5:
                player_1.show_stat
                slime_mob.mob_show_stat()
                dunge_event = input("Enter Punch\n")
                if dunge_event == "Punch":
                    slime_mob.dunge_get_damage(punch_damage)
                    player_get_to_damage = slime_mob.dunge_mob_punch()
                    player_1.dunge__get__damage(player_get_to_damage)
                else:
                    print("You missed")
                    player_1.dunge__get__damage(player__get__damage)
                pvp_index +=1
                
                if slime_mob.dunge_get_damage(0) <= 0:
                    print("You win!!!")
                    player_1.add_exp(20)
                    break
                    
        
        
    elif readline == "Potion":
        print("""
Heal  -  Restore health by 50 points
Energy  -  Restore stamina by 50 points   (NO WORK)""")
    elif readline == "Heal":
        player_1.heal_potion()
    elif readline == "Energy":
        player_1.energy_potion()
            
        
    elif readline == "Stat":
        player_1.show_stat()
    elif readline == "BuyLevel":
        player_1.buy_level()
    elif readline == "Weapon":
        player_1.show_weapon()
    elif readline == "GD":
        player_1.get_damage()
        print("Its Dev test func")
    elif readline == "End":
        print("""Thanks for playing
Pach: Alpha 0.0.2""")
        break
    elif readline == "Support":
        print("Telegram -  @TheMRX666   |    Gmail -  shainyt09@gmail.com")
    else:
        print(f"Error!!! Command {readline} does not exist")
                    

