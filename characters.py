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

class Hero(Character):
    def __init__(self, name, health, level, defense):
        super().__init__(name, health, level, defense)

class Villain(Character):
    def __init__(self, name, health, level, defense):
        super().__init__(name, health, level, defense)

heroes = [
    Hero("Arthur", 100, 5, 10),
    Hero("Luna", 90, 4, 12),
    Hero("Kai", 80, 3, 8)
]

villains = [
    Villain("Drako", 110, 5, 9),
    Villain("Morgana", 95, 4, 11),
    Villain("Shade", 85, 3, 7)
]

characters = heroes + villains

def choose_character():
    print("Escolha seu personagem:")
    for idx, char in enumerate(characters):
        print(f"{idx + 1}. {char.show_info()}")
    choice = int(input("Digite o número do personagem: "))
    selected_character = characters[choice - 1]
    print(f"Você escolheu: {selected_character.get_name()}")
    return selected_character
