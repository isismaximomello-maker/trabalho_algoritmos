import lagrange
import newton
import compara



def main():
    while True:
        print("deseja realizar qual metodo:")
        print("1:lagrange")
        print("2:newton")
        print("3:comparar metodos")
        print("4:sair")

        escolha = int(input())

        if escolha == 1:
            lagrange.chamarLagrange()

        elif escolha==2:
            newton.chamarNewton()
        
        elif escolha == 4:
            return False
        
        elif escolha == 3:
            compara.comparar_metodos()
        else:
            print("opcao invalida")

main()
