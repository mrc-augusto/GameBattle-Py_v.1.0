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
    
    