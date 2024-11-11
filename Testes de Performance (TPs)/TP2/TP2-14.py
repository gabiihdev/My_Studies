def dividir(num1, num2):
    """
    Essa função realiza a divisão inteira entre dois números e calcula também o resto da divisão.
    Os parâmetros da função são num1 (dividendo) e num2 (divisor), e esses números podem ser int ou float.
    A função retorna uma tupla com o resultado da divisão inteira e o resto da divisão.
    
    """
    
    divisao = num1 // num2
    resto_da_divisao = num1 % num2
    
    return divisao, resto_da_divisao

print(dividir(4, 2))