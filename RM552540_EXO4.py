# RecebeR o número de minutos atuais
minutos = int(input("Digite o número de minutos atuais: "))

# CalculaR o fatorial dos minutos
fatorial = 1
i = 1
while i <= minutos:
    fatorial *= i
    i += 1

# Criar a senha "LIBERDADE" seguida do fatorial dos minutos
senha = "LIBERDADE" + str(fatorial)

# Exibir a senha na tela
print("Senha para desbloqueio:", senha)
