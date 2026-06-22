
#lagrange 

def validar_pontos(x, y):
    """
    verifica se atende os criterios de lagrange
    """
    n = len(x)
    
    if n < 2:
        return False, "erro: sao necessarios pelo menos 2 pontos"
    
    if len(x) != len(y):
        return False, "erro: para cada x deve ter um y"
    
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j]:
                return False, "erro: x repetidos"
    
    return True, "valido"


def construir_lagrange(x, y):
    """
    controi o polinomio
    coeficientes = [a0, a1, a2, ..., an]
    P(x) = a0 + a1*x + a2*x^2 + ... + an*x^n
    """
    n = len(x)
    coeficientes = [0.0] * n
    
    for i in range(n):
        # Inicia L[i](x) = 1
        termo = [0.0] * n
        termo[0] = 1.0
        denominador = 1.0
        
        for j in range(n):
            if i != j:
                # Multiplica termo por (x - x[j])
                novo = [0.0] * n
                
                # Multiplica por x: sobe um grau
                for k in range(n - 1, 0, -1):
                    novo[k] = termo[k - 1]
                
                # Multiplica por -x[j]: mesmo grau
                for k in range(n):
                    novo[k] = novo[k] - x[j] * termo[k]
                
                for k in range(n):
                    termo[k] = novo[k]
                
                denominador = denominador * (x[i] - x[j])
        
        # Adiciona y[i] * L[i](x) / denominador
        for k in range(n):
            coeficientes[k] = coeficientes[k] + y[i] * termo[k] / denominador
    
    # Arredonda para 4 casas decimais
    for k in range(n):
        coeficientes[k] = round(coeficientes[k], 4)
    
    return coeficientes


def avaliar_polinomio(coeficientes, valor_x):
    """
    testa o polinomio no ponto 
    coeficientes = [a0, a1, a2, ..., an]
    P(x) = a0 + a1*x + a2*x^2 + ... + an*x^n
    """
    n = len(coeficientes)
    resultado = 0.0
    
    for i in range(n):
        resultado = resultado + coeficientes[i] * (valor_x ** i)
    
    return round(resultado, 4)


def estimar_erro(x, y, valor_x):
    """
    estima o erro em lagrange
    """
    n = len(x)
    
    produto = 1.0
    for i in range(n):
        produto = produto * (valor_x - x[i])
    
    max_variacao = 0.0
    for i in range(n - 1):
        variacao = abs(y[i + 1] - y[i]) / abs(x[i + 1] - x[i])
        if variacao > max_variacao:
            max_variacao = variacao
    
    erro = abs(max_variacao * produto)
    
    return round(erro, 4)


def mostrar_polinomio(coeficientes):
    """
    exibe o polinomio
    coeficientes = [a0, a1, a2, ..., an]
    """
    n = len(coeficientes)
    
    print("\nPolinomio Interpolador:")
    print("P(x) = ", end="")
    
    primeiro = True
    
    # Mostra do maior grau para o menor
    for i in range(n - 1, -1, -1):
        coef = coeficientes[i]
        potencia = i
        
        if coef == 0.0:
            continue
        
        if not primeiro:
            if coef > 0:
                print(" + ", end="")
            else:
                print(" - ", end="")
                coef = abs(coef)
        elif coef < 0:
            print("-", end="")
            coef = abs(coef)
        
        if abs(coef - 1.0) > 0.0001 or potencia == 0:
            print(f"{coef:.4f}", end="")
        
        if potencia > 0:
            print("x", end="")
        
        if potencia > 1:
            print(f"^{potencia}", end="")
        
        primeiro = False
    
    if primeiro:
        print("0", end="")
    
    print()


def ler_pontos():
    """
    le os pontos fornecidos pelo usuario
    """
    print("\nEntrada de pontos:")
    
    while True:
        n = int(input("Quantos pontos? "))
        if n >= 2:
            break
        print("Minimo 2 pontos!")
    
    x = []
    y = []
    
    print("Digite x y (separados por espaco):")
    for i in range(n):
        entrada = input(f"Ponto {i+1}: ").split()
        x.append(float(entrada[0]))
        y.append(float(entrada[1]))
    
    return x, y


def chamarLagrange():
    # Leitura e validacao
    x, y = ler_pontos()
    
    valido, mensagem = validar_pontos(x, y)
    if not valido:
        print(mensagem)
        return
  
    # Constroi e mostra polinomio
    coeficientes = construir_lagrange(x, y)
    mostrar_polinomio(coeficientes)
    
    # Menu de avaliacao
    while True:
        print("\n" + "="*50)
        print("1 - Testar ponto em P(X)")
        print("2 - Estimar erro")
        print("3 - Sair")
        print("="*50)
        
        opcao = input("Escolha: ")
        
        if opcao == "1":
            valor = float(input("Valor de x: "))
            resultado = avaliar_polinomio(coeficientes, valor)
            print("-"*50)
            print(f"P({valor:.4f}) = {resultado:.4f}")
        
        elif opcao == "2":
            valor = float(input("Valor de x: "))
            erro = estimar_erro(x, y, valor)
            print("-"*50)
            print(f"Erro estimado em x={valor:.4f}: {erro:.4f}")
        
        elif opcao == "3":
            print("Programa finalizado!")
            break
        
        else:
            print("Opcao invalida!")


