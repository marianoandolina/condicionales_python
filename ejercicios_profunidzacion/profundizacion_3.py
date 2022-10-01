# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

temperatura_1 = float(input("Ingrese la primera temperatura: "))
temperatura_2 = float(input("Ingrese la segunda temperatura: "))
temperatura_3 = float(input("Ingrese la tercera temperatura: "))
promedio = (temperatura_1 + temperatura_2 + temperatura_3) / 3

# Programa para saber el maximo:

if temperatura_1 > temperatura_2:
    if temperatura_1 > temperatura_3:
        print('La temperatura maxima es {}'.format(temperatura_1))
    else:
        print('La temperatura maximas es {}'.format(temperatura_3))
elif temperatura_2 > temperatura_3:
    print('La maximas temperatura es la {}'.format(temperatura_2))
else:
    print('La temperatura maximas es la {}'.format(temperatura_3))
        
# Programa para saber la minima

if temperatura_1 < temperatura_2:
    if temperatura_1 < temperatura_3:
        print(f'La temperatura minima es {temperatura_1}')
    else:
        print(f'La temperatura minima es {temperatura_3}')    
elif temperatura_2 < temperatura_3:
    print(f'La temperatura minima es {temperatura_2}')
else:
    print(f'La temperatura minima la {temperatura_3}')    
#Promedio

print('El promedio de las temperaturas es {}'.format(promedio))
