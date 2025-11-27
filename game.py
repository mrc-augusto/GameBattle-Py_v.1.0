import random

#character class
class Character:
  def __init__(self, name, health, level, defense):
    self.name = name
    self.health = health
    self.level = level
    self.defense = defense

    def get_name(self):
      return self.name
    
    def get_health(self):
      return self.health
    
    def get_level(self):
      return self.level
    
    def get_defense(self):
      return self.defense
    
    def show_info(self):
      return f'Nome: {self.name}, Vida: {self.health}, Nível: {self.level}, Defesa: {self.defense}'
    
    # # Attack, Defense and Damage methods
    # def attack(self, target):
    #   damage = random.randint(self.get_leve() * 2, self.get_level() * 4)
    #   target.take_damage(damage)
    #   print(f'{self.get_name()} atacou {target.get_name()} causando {damage} de dano!')

    # def special_attack(self, target):
    #   pass

    # def damage(self, damage):
    #   pass

    # def defense(self, target):
    #   pass

    # def special_defense(self, target):
    #   pass
  
#Hero
class Hero(Character):
  def __init__(self, name, health, level, defense, skill):
    super().__init__(name, health, level, defense)
    self.__skill = skill

  def get_skill(self):
    return self.__skill
  
  def show_info(self):
    base_info = super().show_info()
    return f'{base_info}, \nHabilidade: {self.__skill}'
  
class Enemy(Character):
  def __init__(self, name, health, level, defense, type):
    super().__init__(name, health, level, defense)
    self.__type = type
  
  def get_type(self):
    return self.__type
  
  def show_info(self):
    base_info = super().show_info()
    return f'{base_info}, \nTipo: {self.__type}'
