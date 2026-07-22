while True:
    print("\n" * 30)
    print()
    print()
    print("\n-------------------------------")
    print('Olá, esse é um progama desenvolvido para realizar calculos matemáticos')
    print ('Qual cálculo gostaria de realizar ?')
    print ('Selecione uma das opções a seguir: ')
    print("-------------------------")
    print ("1 - Mutiplicação")
    print("2 - Adição")
    print("3 - Divisao")
    print("4 - Subtração")
    print ("5 - Porcentagem")
    print ("6 - Raiz Quadrada")

    calculo = int(input("Escolha uma opção: "))

    if calculo == 1:
        numero1 = float(input('Digite o primeiro numero: '))
        numero2 = float(input('Digite o segundo número: '))
        resultado_mult = (numero1 * numero2)
        print("O resultado da mutiplicação é:  ", resultado_mult)

    if calculo == 2:
        numero1 = float(input('Digite o primeiro numero: '))
        numero2 = float(input('Digite o segundo número: '))
        resultado_ad = (numero1 + numero2)
        print("O resultado da adicao é: ", resultado_ad)

    if calculo == 3:
        numero1 = float(input('Digite o primeiro numero: '))
        numero2 = float(input('Digite o segundo número: '))
        resultado_div = (numero1 / numero2)
        print("O resultado da divisão é: ", resultado_div)

    if calculo == 4:
        numero1 = float(input('Digite o primeiro numero: '))
        numero2 = float(input('Digite o segundo número: '))
        resultado_sub = (numero1 - numero2)
        print("O resultado da subtração é: ", resultado_sub)

    if calculo == 5:
        numero1 = float(input('Digite o número: '))
        numero2 = float(input('Digite a porcentagem desejada: '))
        resultado_por = (numero1/100*numero2)
        print("O resultado da porcentagem é:", resultado_por)

    if calculo == 6:
     numero1 = float(input('Digite o número da raiz: '))
     resultado_raiz = (numero1**0.5)
     print (" O resultado da raiz é: " , resultado_raiz)
     

    

    progama_retorno = input("Deseja fazer outro calculo? (s/n): ")

    if progama_retorno == "n":
        print("Programa encerrado.")
        break