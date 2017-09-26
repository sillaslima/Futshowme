class Dog:
    patas = 4
    cor = 'preto'
    tamanho = 'grande'
    def __init__(self,nome):
        self.nome = nome
        self.idade = 45

class Circulos:
    raio = 25.4
    def calcula_Area(self):
        self.area = 3.14 * (self.raio**2)
        return self.area
    def calcula_Volume(self,altura):
        self.volume = 3.14 * (self.raio**2) * altura
        return self.volume


if __name__ == '__main__':

    c = Circulos()
    print(c.raio)
    print(c.calcula_Area())
    print( c.calcula_Volume(23.))

    d = Dog('sillas')
    print(dir(Dog))
    #x = Dog()
    print(d.patas)
    print(d.tamanho)
    print(Dog.cor)
