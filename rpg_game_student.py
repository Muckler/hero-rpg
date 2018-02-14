# Hero RPG Game
class Hero:
  def __init__(self, health, power):
    self.health = health
    self.power = power
    
  def attack(self, goblin):
    if self.alive() == True:
      goblin.health -= self.power
      print("You do {} damage to the goblin.".format(self.power))
      if goblin.alive() != True:
        print("The goblin is dead.")
  
  def alive(self):
    if self.health > 0:
      return True
    
  def print_status(self):
    print("You have {} health and {} power.".format(self.health, self.power))
    
class Goblin:
  def __init__(self, health, power):
    self.health = health
    self.power = power
    
  def attack(self, hero):
    if self.alive() == True:
      hero.health -= self.power
      print("The goblin does {} damage to you.".format(self.power))
      if hero.alive() != True:
        print ("You are dead.")
    
  def alive(self):
    if self.health > 0:
      return True
  def print_status(self):
    print("The goblin has {} health and {} power.".format(self.health, self.power))
    
def run():
  
  hero = Hero(10, 5)
  goblin = Goblin(6, 2)
  
  while goblin.alive() == True and hero.alive() == True:
    hero.print_status()
    goblin.print_status()
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
      # Hero attacks goblin
      hero.attack(goblin)
    elif raw_input == "2":
      pass
    elif raw_input == "3":
      print("Goodbye.")
      break
    else:
      print("Invalid input {}".format(raw_input))

    goblin.attack(hero)

if __name__ == "__main__":
  run()