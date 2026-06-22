import lagrange
import newton


def main():
    while True:
        print("deseja realizar qual metodo:")
        print("1:lagrange")
        print("2:newton")
        print("3:sair")

        escolha = int(input())

        if escolha == 1:
            lagrange.chamarLagrange()

        elif escolha==2:
            newton.chamarNewton()
        
        elif escolha == 3:
            return False
        else:
            print("opcao invalida")

main()
