#1 «Птицы и их способности»
class Animal():
    def speak(self):
        return "Издаёт звук"
    
class MixinSwim():
    def swim(self):
        return ' Плавает'
    
class MixinFly():
    def fly(self):
        return "Летает"

class Duck(Animal, MixinSwim, MixinFly):
    def speak(self):
        return 'Кря-кря'
    
class Penguin(Animal, MixinSwim):
    def speak(self):
        return 'Буль-буль'   

animals = [Duck(), Penguin()] 
for i in range(len(animals)):
    print(animals[i].speak()) 
    print(animals[i].swim())  
    if isinstance(animals[i], MixinFly):  
        print(animals[i].fly()) 

#2 «Креативная личность»
class Writer():
    def write(self):
        return "Что-то пишет"
class Painter():
    def draw(self):
        return "Рисует картину"
class CreativePerson(Writer,Painter):
    def write(self):
        return "творчески пишет стихотворение"
    def draw(self):
        return "выразительно рисует пейзаж"
persons = [Writer(),Painter(),CreativePerson()]
for person in persons:
    if isinstance(person, Writer):
        print(person.write())  
    if isinstance(person, Painter):
        print(person.draw())  