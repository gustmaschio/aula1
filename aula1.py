# Soma de dois números:
def soma_dois_numeros():
    num1 = float(input("Insira o primeiro número: ")) 
    num2 = float(input("Insira o segundo número: ")) 
    soma = num1 + num2
    return f"A soma de {num1} e {num2} é {soma}."

# Par ou Ímpar:
def par_ou_impar():
    numero = int(input("Insira um número inteiro: "))
    if numero % 2 == 0: 
        return f"O número {numero} é par."
    else: 
        return f"O número {numero} é ímpar."

# Maior de três números:
def maior_de_tres():
    num1 = float(input("Insira o primeiro número: ")) 
    num2 = float(input("Insira o segundo número: ")) 
    num3 = float(input("Insira o terceiro número: ")) 
    maior = max(num1, num2, num3) 
    return f"O maior número entre {num1}, {num2}, e {num3} é {maior}."

# Contagem de 1 a 10:
def contagem():
    return list(range(1, 11))

# Tabuada de um número:
def tabuada():
    num = int(input("Insira um número para ver sua tabuada: "))
    return [f"{num} x {i} = {num * i}" for i in range(1, 11)]

# Verificação de idade:
def verificar_idade(): 
    idade = int(input("Insira sua idade: "))
    if idade >= 18: 
        return "Maior de idade." 
    else: 
        return "Menor de idade."

# Soma de números pares de 1 a 100:
def soma_pares(): 
    soma = sum([i for i in range(1, 101) if i % 2 == 0]) 
    return f"A soma de todos os números pares de 1 a 100 é {soma}."