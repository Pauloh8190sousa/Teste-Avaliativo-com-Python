from Formula1_Teste import formula1
print("_________________________________________________")
print("Programa Operações")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if(idade >= 8):
    print("Parábens, Você tem idade suficiente Para Participar do Jogo")
    res = "n";
    while(res == "n"):
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))
        print("Escolha uma operação: ")
        print("Multiplicação (m)")
        print("Adição (a)")
        print("Divisão (d)")
        print("Subtração (s)")
        op = input("Digite a operação (m,a,d,s): ")
        resul = 0
        if( op == "m"):
            resul = num1*num2
            print("Resultado:",resul)
        elif(op == "a"):
            resul = num1+num2
            print("Resultado:",resul)
        elif(op == "d"):
            resul = num1/num2
            print("Resultado:",resul)
        elif(op == "s"):
            resul = num1-num2
            print("Resultado:",resul)
        else:
            print("Entrada inválida")
        res = input("Deseja encerrar o programa? (s/n): ")
    print("_________________________________________________")
    print("Programa Formula 1")
    formula1()
    exit()
