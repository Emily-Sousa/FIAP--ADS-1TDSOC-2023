tipo_assinatura = input("Digite o sua de assinatura (1 - Basic, 2 - Silver, 2 - Gold ou 3 - Platinum): ")
faturamento_anual = float(input("Digite seu faturamento anual: "))

if tipo_assinatura == "1":
    bonus = 0.3 * faturamento_anual
elif tipo_assinatura == "2":
    bonus = 0.2 * faturamento_anual
elif tipo_assinatura == "3":
    bonus = 0.1 * faturamento_anual
elif tipo_assinatura == "4":
    bonus = 0.05 * faturamento_anual
else:
    print("Assinatura inválida! Por favor, tente novamente.")
    bonus = 0

while bonus < 0:
    print("O valor do bônus não pode ser negativo! Insira um valor válido.")
    tipo_assinatura = input("Digite sua assinatura (1 - Basic, 2- Silver, 3 - Gold ou 4 - Platinum): ")
    faturamento_anual = float(input("Digite seu faturamento anual: "))

    if tipo_assinatura == "1":
        bonus = 0.3 * faturamento_anual
    elif tipo_assinatura == "2":
        bonus = 0.2 * faturamento_anual
    elif tipo_assinatura == "3":
        bonus = 0.1 * faturamento_anual
    elif tipo_assinatura == "4":
        bonus = 0.05 * faturamento_anual
    else:
        print("Assinatura inválida")
        bonus = 0

print("O valor do bônus é de R$", bonus)