# comparacao_simples.py
import lagrange
import newton



def comparar_metodos():
    """
    Compara Lagrange e Newton em UM ponto específico
    """
    
    n = int(input("Quantos pontos? "))
    
    x = []
    y = []
    
    for i in range(n):
        print(f"\nPonto {i+1}:")
        xi = float(input("  x = "))
        yi = float(input("  y = "))
        x.append(xi)
        y.append(yi)
    
    # Validar pontos
    valido, mensagem = lagrange.validar_pontos(x, y)
    if not valido:
        print(f"\nERRO: {mensagem}")
        return
    
    
    # Valor para testar
    x_teste = float(input("Digite o valor de x para testar: "))
    
    # lagrange
    print("\n" + "-"*60)
    print("LAGRANGE:")
    
    coeficientes = lagrange.construir_lagrange(x, y)
    
    # Mostrar polinômio
    lagrange.mostrar_polinomio(coeficientes)
    
    resultado_lag = lagrange.avaliar_polinomio(coeficientes, x_teste)
    erro_lag = lagrange.estimar_erro(x, y, x_teste)
    
    print(f"P({x_teste:.4f}) = {resultado_lag:.4f}")
    print(f"Erro estimado = {erro_lag:.4f}")
    
    # ===== NEWTON =====
    print("\n" + "-"*60)
    print("NEWTON:")
    
    pontos_newton = [(x[i], y[i]) for i in range(n)]
    
    coef_newton = newton.diferencasDivididas(pontos_newton)
    print("  Coeficientes: ", end="")
    for i, c in enumerate(coef_newton):
        print(f"{c:.4f}", end=" ")
    print()
    
    print("  Polinômio: ", end="")
    print(newton.construirPolinomio(pontos_newton))
    
    resultado_newton = newton.calcularNewton(pontos_newton, x_teste)
    
    # Estimar erro de Newton
    if n > 1:
        resultado_anterior = newton.calcularNewton(pontos_newton[:-1], x_teste)
        erro_newton = newton.estimarErro(resultado_anterior, resultado_newton)
    else:
        erro_newton = 0.0
    
    print(f"P({x_teste:.4f}) = {resultado_newton:.4f}")
    print(f"Erro estimado = {erro_newton:.4f}")
    
    # ===== COMPARAÇÃO =====
    print("\n" + "="*60)
    print("RESULTADO DA COMPARAÇÃO:")
    print("="*60)
    
    diferenca = abs(resultado_lag - resultado_newton)
    

    print(f" Lagrange: {resultado_lag:>20.6f} ")
    print(f" Newton:   {resultado_newton:>20.6f} ")
    print(f" Diferença:{diferenca:>20.10f} ")
    
    # Comparação dos erros
    print(f"\nErro Lagrange: {erro_lag:.6f}")
    print(f"Erro Newton:   {erro_newton:.6f}")
    print(f"   Diferença: {erro_lag - erro_newton:.6f}")

    print("\n" + "="*60)
