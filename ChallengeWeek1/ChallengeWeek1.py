'''Exercise 1: Write a programme that reads an odd number from the keypad. If the user does not enter an odd number, the process must be repeated until the correct number is entered.
'''
while True:
    if int(input('Please enter an odd number: '))%2 == 0:
        print('Incorrect number entered, please enter an odd number')
    else:
        print('finished cycle')
        break

'''
Exercise 2:
Escribí un programa que pida al usuario cuantos números quiere introducir. Luego lee
todos los números y realiza una media aritmética:
'''
cantidad = int(input('Ingrese la cantidad de numeros para sacar la media:'))
lista=[]

for i in range(cantidad):
    a=float(input('Ingreseel numero {}:'.format(i+1)))
    lista.append(a)
print('La media aritmetica de los numeros es:', sum(lista)/len(lista))

''' Exercise 3:

# Utilizando la función range() y la conversión a listas genera las siguientes listas
# dinámicamente:

# ● Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# ● Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# ● Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# ● Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# ● Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
'''

print(list(range(0,11,1)));
print([x for x in range(-10,1)]);
print([x for x in range(0,21,1) if x%2 == 0])
print([x for x in range(-19,-1+1) if x%2 != 0])
print([x for x in range(0,51,1) if x%5 ==0])

# ##Alternativas:

lista_0_10 = list(range(0,11))
print(lista_0_10)

lista_menos10_0 = list(range(-11,0))
print(lista_menos10_0)

lista_pares0_10 = list(range(0,21,2))
print(lista_pares0_10)

lista_impar_menos20_0 = list(range(-19,0,2))
print(lista_impar_menos20_0)

lista_multiple5_0_50 = list(range(0,51,5))
print(lista_multiple5_0_50)


'''Exercise 4: 
Dadas dos listas, debes generar una tercera con todos los elementos que se
repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:
'''
lista_1 = [1,2,3,4,5,6,7,8,9,10,'g','l','i','f']
lista_2 = ['j','e','r','o','g','l','i','f','i','c','o',7,8,9]
lista_3 = []

for elements in lista_2:
    if elements in lista_1:
        lista_3.append(elements)

print([*set(lista_3)])
print(list(set(lista_3)))

'''Exercise 5: Escribí un programa que sume todos los números enteros impares desde el 0 hasta
el 100:
'''
lista= []

for i in range(0,101,1):
    if i%2 != 0:
        lista.append(0)
    else:
        lista.append(i)
        
print(sum(lista))

'''Exercise 6: Contar cuantas veces aparece un elemento en una lista
'''

def contando(lista,elemento):
    contador=0
    for elemento in lista:
        if(elemento == x):
            contador = contador + 1
            #contador += 1
    return contador

lista_contador = [90,9,6,34,5,9,123,44,9,4,9,67,9]
x = 9
print(contando(lista_contador,x))
#alternativa
print('{} aparece {} veces'.format(x, contando(lista_contador,x)))