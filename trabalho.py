# inicio newton
def validarPontos(pontos):

    # se não houver pelo menos 1 par x,y
    if len(pontos) < 2:
        return False

    xs = [p[0] for p in pontos]

    #se houverem 2 x iguais -> implica divisão por 0, não pode ser possível
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] == xs[j]:
                return False

    return True

def diferencasDivididas(pontos):
# Calcula os coeficientes 
    n = len(pontos)

    tabela = [[0 for _ in range(n)] for _ in range(n)]

    # Primeira coluna recebe os valores de y
    for i in range(n):
        tabela[i][0] = pontos[i][1]

    # Fórmula f(x1)-f(x0)/xi-x0
    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = (tabela[i+1][j-1] - tabela[i][j-1]) / (pontos[i+j][0] - pontos[i][0])

    # Coeficientes da primeira linha
    coeficientes = [tabela[0][i] for i in range(n)]

    return coeficientes

def construirPolinomio(pontos):
#constroi string do polinomio

    coef = diferencasDivididas(pontos)

    polinomio = f"{coef[0]:.6f}"

    for i in range(1, len(coef)):

        termo = f"{coef[i]:+.6f}"

        for j in range(i):
            termo += f"(x-{pontos[j][0]})"

        polinomio += termo

    return polinomio

def calcularNewton (pontos, x):
#calcula polinomio de grau n-1
    coef = diferencasDivididas(pontos)

    resultado = coef[0]

    for i in range(1, len(coef)):
        termo = coef[i]

        for j in range(i):
            termo *= (x - pontos[j][0])

        resultado += termo

    return resultado

def estimarErro(valor_anterior, valor_atual):
# Estima o erro pela diferença entre duas aproximações
    return abs(valor_atual - valor_anterior)

def main():

    pontos = []

    n = int(input("Digite a quantidade de pontos (x): "))

    for i in range(n):
        print(f"\nPonto {i}")

        x = float(input("x = "))
        fx = float(input("f(x) = "))

        pontos.append((x, fx))

    if not validarPontos(pontos):
        print("\nPontos inválidos!")
        return

    print("\nPontos informados:")
    for ponto in pontos:
        print(ponto)

    print("\nCoeficientes de Newton:")
    print(diferencasDivididas(pontos))

    print("\nPolinômio interpolador:")
    print(construirPolinomio(pontos))

    x_avaliar = float(input("\nDigite o valor de x para avaliar o polinômio: "))

    resultado = calcularNewton (pontos, x_avaliar)

    #estimativa de erro
    resultado = calcularNewton (pontos, x_avaliar)

    resultado_anterior = calcularNewton (pontos[:-1], x_avaliar)

    erro = estimarErro(resultado_anterior, resultado)

    grau_atual = len(pontos) - 1
    grau_anterior = len(pontos) - 2
    print(f"P{grau_atual}({x_avaliar}) = {resultado}")
    print(f"\nP{grau_anterior}({x_avaliar}) = {resultado_anterior}")
    print(f"\nE({x_avaliar}) = |P{grau_atual} - P{grau_anterior}|")
    print(f"E({x_avaliar}) = {erro}")

main()

# fim newton