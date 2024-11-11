def verificar_elementos(tupla1, tupla2):
    if set(tupla1) == set(tupla2):
        return 'As tuplas 1 e 2 possuem os mesmos elementos.'
    else:
        return 'As tuplas 1 e 2 não possuem os mesmos elementos.'

tupla1 = (1, 3, 5)
tupla2 = (5, 1, 3)

print(verificar_elementos(tupla1, tupla2))