notas_impares = [] # lista para armazenar as notas dos alunos ímpares
notas_pares = [] # lista para armazenar as notas dos alunos pares

i = 1 # contador para o número do aluno

#  receber as notas dos alunos ímpares
while len(notas_impares) < 25:
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
    print("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO", i, end=": ")
    nota = float(input())
    notas_impares.append(nota)
    i += 2 # aumentar o contador em 2 para passar para o próximo número ímpar

i = 2 # iniciar o contador para o número do aluno

# loop para receber as notas dos alunos pares
while len(notas_pares) < 25:
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
    print("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO", i, end=": ")
    nota = float(input())
    notas_pares.append(nota)
    i += 2 # aumenta o contador em 2 para passar para o próximo número par

# calcular a média de cada metade da sala
media_impares = sum(notas_impares) / len(notas_impares)
media_pares = sum(notas_pares) / len(notas_pares)

# exibir a média de cada metade da sala
print("Média dos alunos ímpares:", media_impares)
print("Média dos alunos pares:", media_pares)

# verificar qual metade teve a maior nota
if media_impares > media_pares:
    print("A metade dos alunos ímpares obtém a maior nota.")
elif media_pares > media_impares:
    print("A metade dos alunos pares obtém a maior nota.")
else:
    print("As duas metades tiveram a mesma nota média.")
