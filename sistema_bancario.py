valor=float(0)
saque_quantidade_atual=0
LIMITE_SAQUE_DIARIO_QUANTIDADE=3
LIMITE_SAQUE_DIARIO_VALOR=500
saldo=float(5000)
extrato=""""""
while True:
    menu=int(input("""
[1] Saque
[2] Deposito
[3] extrato
[0] Sair
"""))
    if menu==1:
        valor=float(input("informe o valor do saque: "))
        if valor<0:
            print("Valor incorreto")
        elif valor>LIMITE_SAQUE_DIARIO_VALOR:
            print("Valor maior que o limite diário")
        elif saque_quantidade_atual>=3:
            print("Número de saques diários excedido")
        elif valor>saldo:
            print("Saldo insuficiente")
        else:
            print("Salque efetuado")
            saque_quantidade_atual+=1
            saldo-=valor
            extrato+=f"Saque R$ {valor:.2f}\n"
    elif menu==2:
        valor=float(input("Informe o valor do deposito: "))
        if valor<0:
            print("Valor incorreto")
        else:
            print("Deposito efetuado")
            saldo+=valor
            extrato+=f"Deposito R$ {valor:.2f}\n"
    elif menu==3:
        print("          Extrato          \n")
        print(extrato)
        print(f"Saldo R$ {saldo:.2f}")
        print("###########################\n")
    elif menu==0:
        print("Sando")
        break
    else:
        print("Opção invalida")