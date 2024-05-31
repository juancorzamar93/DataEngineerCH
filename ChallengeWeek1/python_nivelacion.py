class Calculadora:
    def __init__(self, nombre:str) -> none:
        self.nombre = nombre
        
    def calculo(self, n1:int, n2:int, cb:callable) ->any:
        return cb(n1, n2)


def main():
    iteracion:list = [x for x in [1,2,3,4,5]]
    print(iteracion)
    
    iteracion_dos:list=[_ for _ in [1,2,3,4,5] if _%2 == 0]
    print(iteracion_dos)
    
    iteracion_tres:list=[_ for _ in [1,2,3,4,5] if _%2 != 0]
    print(iteracion_tres)
    
    def suma(n1:int, n2:int) -> int:
        return n1 + n2
    
    calcula = Calculadora("data-engineer")
    print("El calculo es: suma, resultado: ", calcula.calculo(2,3,suma))
    print("El) calculo es: resta, resultado:  ", calcula.calculo(2,3, lambda x,y: x - y))
    print("El calculo es: multiplicacion, resultado: ", calcula.calculo(2,3, lambda x,y: x * y))
    print("El calculo es: division, resultado: ", calcula.calculo(2,3, lambda x,y: x / y))
    

    
    
if __name__ == "__main__":
    main()
    