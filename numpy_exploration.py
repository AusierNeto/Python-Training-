import numpy as np

# Criando um array NumPy a partir de uma lista
array1 = np.array([10, 20, 30, 40])
print(array1)

# Criando um array a partir de list comprehension
array_divisible_by_4 = np.array([e for e in range(20) if e % 4 == 0])
print(array_divisible_by_4)

# Criando um array de números de 0 a 10
array_to_10 = np.array(range(10))
print(array_to_10)

print(len(array_to_10))



import numpy as np

precos = np.array([10.4, 40.2, 100, 22.46])
idades = np.array([12, 13, 14, 15])

# Calcular estatísticas
print("Média:", np.mean(precos))
print("Mínimo:", np.min(precos))
print("Máximo:", np.max(precos))

# Simular aumento de 10% nos preços
precos_aumentados = precos * 1.1
print(precos_aumentados)

# Idades daqui 2 anos
idades_mais_2 = idades + 2
print(idades_mais_2)