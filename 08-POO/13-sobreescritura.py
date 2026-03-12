class Animal:
    def comer(self):
        print('Como muchas veces al día')

    def dormir(self):
        print('Duermo muchas horas')


class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

    # Sobreescribiendo el método heredado de la clase padre
    def dormir(self):
        print('Duermo 15 horas al día')


# Programa principal
print('*** Ejemplo de herencia en Python ***')
print('Clase padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()  # Se llama el método sobreescrito en la clase hija
perro1.hacer_sonido()
