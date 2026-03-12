class Animal:
    def hacer_sonido(self):
        print('Hago un pitido...')


class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')


class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')


print('*** Ejemplo polimorfismo ***')
print('Clase padre Animal: ')
animal1 = Animal()
animal1.hacer_sonido()
# Definir un objeto de la clase perro
print('\nClase hija Perro: ')
perro1 = Perro()
# Polimorfismo (se manda a llamar el método según el objeto que se esta ejecutando)
perro1.hacer_sonido()
# Definir un objeto de la clase gato
print('\nClase hija Gato:')
gato1 = Gato()
gato1.hacer_sonido()
