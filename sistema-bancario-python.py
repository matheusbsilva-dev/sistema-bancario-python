saldo = 1000  # saldo inicial

while True:
    print('1 - ver o saldo')
    print('2 - depositar dinheiro')
    print('3 - sacar dinheiro')
    print('4 - sair')

    r = int(input('Digite sua opção: '))

    if r == 1:
        print(f'Seu saldo atual é {saldo}')

    elif r == 2:
        d = int(input('Digite o valor que quer depositar: '))
        saldo += d
        print('Depósito realizado com sucesso!')

    elif r == 3:
        s = int(input('Quanto você quer sacar: '))
        if s <= saldo:
            saldo -= s
            print('Saque realizado com sucesso!')
        else:
            print('Saldo insuficiente.')

    elif r == 4:
        print('Programa finalizado com sucesso.')
        break

    else:
        print('Opção inválida!')
