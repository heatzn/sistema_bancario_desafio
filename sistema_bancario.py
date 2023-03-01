# Saque: 3 saques diários com limite de R$500,00. Caso não haja saldo em conta, o sistema informa que não há saldo.
# Extrato: Listar todos os depósitos e saques feitos. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem estar no formato R$XXX.X


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    menu = f"""

======= Sistema Bancário =======

Saldo: R$ {saldo:.2f}

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

> """

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Quanto você gostaria de depositar? "))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Depósito de R$ {deposito:.2f}" + " realizado com sucesso!")
        
        else:
            print("Operação inválida! O valor informado não é válido.")
            
    elif opcao == "2":
        saque = float(input("Quanto você deseja sacar? "))

        exedeu_saldo = saque > saldo

        exedeu_limite = saque > limite

        exedeu_n_saques = numero_saques >= LIMITE_SAQUES

        if exedeu_saldo:
            print("Impossível realizar esta operação. Você excedeu seu saldo.")
        
        elif exedeu_limite:
            print("Impossível realizar esta operação. Você excedeu o seu limite diário (R$500,00)")

        elif exedeu_n_saques:
            print("Impossível realizar esta operação. Você excedeu seu número de saques diários.")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print(f"Saque de {saque:.2f}" + " realizado com sucesso!")

    elif opcao == "3":
        print("Não foram feitas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "4":
        break

    else:
        print("Operação inválida")