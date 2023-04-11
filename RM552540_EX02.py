# Contabilizar os votos de cada dia da semana
segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

# Solicitar que o usuário informe a quantidade de votos para cada dia da semana
print("Por favor, informe a quantidade de votos para cada dia da semana:\n")

# Usar o laço while para pedir o voto de cada dia e somar à variável
while True:
    # verificar se já foram contabilizados votos para todos os dias
    if segunda and terca and quarta and quinta and sexta:
        break

    # pedir o voto para cada dia da semana
    voto = input("Segunda-feira: ")
    if voto.isdigit():
        segunda += int(voto)

    voto = input("Terça-feira: ")
    if voto.isdigit():
        terca += int(voto)

    voto = input("Quarta-feira: ")
    if voto.isdigit():
        quarta += int(voto)

    voto = input("Quinta-feira: ")
    if voto.isdigit():
        quinta += int(voto)

    voto = input("Sexta-feira: ")
    if voto.isdigit():
        sexta += int(voto)

# verificar qual dia da semana teve mais votos e exibir o resultado
mais_votado = max(segunda, terca, quarta, quinta, sexta)

if mais_votado == segunda:
    print("A segunda-feira foi o dia mais votado!")
elif mais_votado == terca:
    print("A terça-feira foi o dia mais votado!")
elif mais_votado == quarta:
    print("A quarta-feira foi o dia mais votado!")
elif mais_votado == quinta:
    print("A quinta-feira foi o dia mais votado!")
else:
    print("A sexta-feira foi o dia mais votado!")

