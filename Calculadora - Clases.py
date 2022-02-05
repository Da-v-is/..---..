class Calculadora:
    def __init__ (self,n1,n2):
        self.n1 = n1
        self.n2 = n2
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.division = n1 / n2
        self.producto = n1 * n2

    def print(self):
        print("numero 1:",self.n1,"numero 2:",self.n2)
        print("suma:",self.suma)
        print("resta:",self.resta)
        print("division:",self.division)
        print("multiplicacion:",self.producto)
        
operacion = Calculadora(2,4)
operacion.print()
