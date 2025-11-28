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
  
heroes = [
  Hero(
    name='Batman',
    health=100,
    level=2,
    defense=5,
    skill='Estrategista'
  ),
  Hero(
    name='Superman',
    health=120,
    level=3,
    defense=6,
    skill='Força'
  ),
  Hero(
    name='Mulher Maravilha',
    health=110,
    level=2,
    defense=7,
    skill='Agilidade'
  ),
  Hero(
    name='Flash',
    health=90,
    level=2,
    defense=4,
    skill='Velocidade'
  ),
]
  
class Enemy(Character):
  def __init__(self, name, health, level, defense, type):
    super().__init__(name, health, level, defense)
    self.__type = type
  
  def get_type(self):
    return self.__type
  
  def show_info(self):
    base_info = super().show_info()
    return f'{base_info}, \nTipo: {self.__type}'

enemies = [
  Enemy(
    name='Coringa',
    health=100,
    level=2,
    defense=5,
    type='Psicopata'
  ),
  Enemy(
    name='Lex Luthor',
    health=110,
    level=3,
    defense=6,
    type='Gênio'
  ),
  Enemy(
    name='Ares',
    health=120,
    level=3,
    defense=7,
    type='Deus da Guerra'
  ),
  Enemy(
    name='Capuz Vermelho',
    health=90,
    level=2,
    defense=4,
    type='Vigilante'
  ),
]

class Game:
  def __init__(self):
    self.hero = None
    self.enemy = None
  def start(self):
    choose_class = int(input('\n1 - Herói\n2 - Inimigo\nEscolha a classe do seu personagem e digite o núemero desejado:'))

    if choose_class == 1:
      print('Escolha seu Personagem:')
      for index, hero in enumerate(heroes):
        print(f'{index + 1} - {hero.show_info()}')
      hero_choice = int(input('Digite o número do herói:')) 
      self.hero = heroes[hero_choice - 1]
      print(f'Você escolheu o herói:\n{self.hero.show_info()}')
      self.enemy = random.choice(enemies)
      print(f'Seu inimigo será:\n{self.enemy.show_info()}')


    elif choose_class == 2:
      print('Escolha seu Personagem: ')
      for index, enemy in enumerate(enemies):
        print(f'{index + 1} - {enemy.show_info()}')
        enemy_choice = int(input('Digite o número do vilão:'))
        self.enemy = enemies[enemy_choice -1]
        print(f'Você escolheu o vilão:\n{self.enemy.show_info()}')
        self.hero = random.choice(heroes)
        print(f'Seu inimigo será:\n{self.hero.show_info()}')
    else:
      print('Opção inválida. Por favor, escolha 1 ou 2.')
  
  # def start_battle(self):

game = Game()
game.start()

    
