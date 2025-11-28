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
    
    def attack(self, target):
      damage = random.randint(self.level *2, self.level *5)
      target.take_damage(damage)
      print(f'{self.name} atacou {target.get_name()} causando {damage} de dano!')
    
    def special_attack(self, target):
      special_damage = random.randint(self.level *4, self.level *7)
      target.take_damage(special_damage)
      print(f'{self.name} usou um ataque especial em {target.get_name()} causando {special_damage} de dano!')

    def take_damage(self, damage):
      real_damage = damage - self.defense
      self.health -= real_damage
      print(f'{self.name} recebeu {real_damage} de dano! Vida restante: {self.healh}')
    
    def show_info(self):
      return f'Nome: {self.name}, \nVida: {self.health}, \nNível: {self.level}, \nDefesa: {self.defense}'
    
