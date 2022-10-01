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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

num_1 = int(input('Ingrese el primer numero: '))  
num_2 = int(input('Ingrese el segundo numero: '))

diferencia = num_1 - num_2

if diferencia > 0:
    print('La diferencia entre ambos numeros es positiva')
elif diferencia < 0:
    print('La diferencia entre ambos numeros es negativa')
else:
    print('La diferencia entre ambos numeros es cero')
