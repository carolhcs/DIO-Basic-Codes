class Hero :
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def atack(self, type):
        atk = ""
        if type == "mago":
            atk = "magia"
        elif type == "monge":
            atk = "artes marciais"
        elif type == "guerreiro":
            atk = "espada"
        else:
            atk = "shuriken"
        return atk

    def atacar(self):
        print(f"o {self.type} atacou usando {self.atack(self.type)}")


newHeroName = input("Digite o nome do novo herói: ")
newHeroAge = int(input("Digite a idade do novo herói: "))
newHeroType = input("Digite o tipo do novo herói (mago, monge, guerreiro, ou ninja): ")

newHero = Hero(newHeroName, newHeroAge, newHeroType)

newHero.atacar()