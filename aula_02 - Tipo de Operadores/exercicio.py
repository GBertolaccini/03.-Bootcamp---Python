
# https://github.com/lvgalvao/data-engineering-roadmap
# https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados


import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero_01 = int(input("Insira um numero inteiro: "))
numero_02 = int(input("Insira um numero inteiro: "))
print("Resultado: ", numero_01 + numero_02)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero_01 = int(input("Insira um numero inteiro: "))
print("Resultado: ", numero_01 * 5)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero_01 = int(input("Insira um numero inteiro: "))
numero_02 = int(input("Insira um numero inteiro: "))
print("Resultado: ", numero_01 * numero_02)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero_01 = int(input("Insira um numero inteiro: "))
numero_02 = int(input("Insira um numero inteiro: "))
print("Resultado: ", numero_01 // numero_02)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero_01 = int(input("Insira um numero inteiro: "))
print("Resultado: ", numero_01 ** 2)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero_01 = float(input("Insira um numero: "))
numero_02 = float(input("Insira um numero: "))
print("Resultado: ",numero_01 + numero_02)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero_01 = float(input("Insira um numero: "))
numero_02 = float(input("Insira um numero: "))
print("Resultado: ", (numero_01 + numero_02)/2)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero_01 = float(input("Insira um numero (base): "))
numero_02 = float(input("Insira um numero (expoente): "))
print("Resultado: ",numero_01 ** numero_02)
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
numero_01 = float(input("Insira a temperatura em graus Celcius: "))
print("Resultado: ", ( numero_01 * (9/5))+32)
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
numero_01 = float(input("Insira o raio da circunferencia: "))
print("Resultado: ", math.pi() * numero_01 ** 2)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
string_01 = (input("Insira um texto: "))
print("Resultado: ",string_01.upper())
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
string_01 = (input("Insira um texto: "))
print("Resultado: ",string_01.lower())
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
string_01 = (input("Insira um texto: "))
print("Resultado: ", string_01.strip())
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
string_01 = (input("Insira uma Data: "))
dia, mes, ano = string_01.split()
print("Dia: ", dia)
print("Mes: ", mes)
print("Ano: ", ano)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string_01 = (input("Insira um texto: "))
string_02 = (input("Insira um texto: "))
texto_concatenado = string_01 + string_02
print ("Texto Concatenado: ", texto_concatenado)
# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
boolean_01 = bool((input("Insira um texto: " )))
boolean_02 = bool((input("Insira um texto: " )))
resultado_and = boolean_01 and boolean_02
print("Resultado do AND lógico:", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
boolean_01 = bool((input("Insira um texto: " )))
boolean_02 = bool((input("Insira um texto: " )))
resultado_and = boolean_01 or boolean_02
print("Resultado do OR lógico:", resultado_and)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
boolean_01 = bool((input("Insira um texto: " )))
print("Resultado da igualdade:", not boolean_01)
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
boolean_01 = bool((input("Insira um texto: " )))
boolean_02 = bool((input("Insira um texto: " )))
print("Resultado do OR lógico:", boolean_01 == boolean_02)
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
boolean_01 = bool((input("Insira um texto: " )))
boolean_02 = bool((input("Insira um texto: " )))
print("Resultado do OR lógico:", boolean_01 != boolean_02)

# #### try-except e if

# 21: Conversor de Temperatura
try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F.")
except ValueError:
    print("Por favor, digite um número válido para a temperatura.")
    
# 22: Verificador de Palíndromo
entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")
    
# 23: Calculadora Simples
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")
    
# 24: Classificador de Números
try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
    
# 25: Conversão de Tipo com Validação

entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")


