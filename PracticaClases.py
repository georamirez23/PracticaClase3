# Practica en clase

class Animal:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad= edad

    def correr(self):
        print('Llamar perro a comer')
        perro.raza= "pastor"


perro = Animal('Pirruzca','shit-tzu', 10)
print(perro.nombre + ", raza: " + perro.raza + " edad : " + str(perro.edad))

perro.correr()



class Planta:
    def __init__(self, especie, lugar, medida):
        self.especie=especie
        self.lugar= lugar
        self.medida= medida

    def verano(self):
        print("Planta necesita agua")
tipoplanta = Planta('Gerbera', 'Bosque tropical', 20)
print("Planta: " + tipoplanta.especie + " lugar que habita:  " + tipoplanta.lugar + " Estatura: " + str(tipoplanta.medida))

tipoplanta.verano()

print(tipoplanta.__dict__)
print(perro.__dict__)
