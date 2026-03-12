# Flexibilidad en la creación de objetos
# Python toma la definición de constructor que se declaró al final

class Aritmetica:

    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado resta: {resultado}')

    # Agregar los métodos de multiplicación y división
    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'Resultado multiplicación: {resultado}')

    def division(self):
        resultado = self.operando1 / self.operando2
        print(f'Resultado división: {resultado}')


# Programa principal
if __name__ == '__main__':
    print('*** Ejemplo de clase Aritmetica ***')
    aritmetica1 = Aritmetica(5, 7)
    print('Primer objeto')
    aritmetica1.sumar()
    aritmetica1.restar()
    # Segundo objeto
    aritmetica2 = Aritmetica(12, 16)
    print('Segundo objeto')
    aritmetica2.sumar()
    aritmetica2.restar()
    # Tercer objeto
    print('Tercer objeto')
    aritmetica3 = Aritmetica(4)
    aritmetica3.operando2 = 7
    aritmetica3.sumar()
    # Cuarto objeto
    print('Cuarto objeto')
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 = 2
    aritmetica4.operando2 = 6
    aritmetica4.restar()
    # Quinto objeto
    print('Quinto objeto')
    aritmetica5 = Aritmetica(operando1=8, operando2=5)
    aritmetica5.multiplicar()
    aritmetica5.division()
