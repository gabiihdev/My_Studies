def intercalar_listas(lista1, lista2):
    string = []
    max_length = max(len(lista1), len(lista2))
    
    for i in range(max_length):
        if i < len(lista1):
            string.append(lista1[i])
        if i < len(lista2):
            string.append(lista2[i])
            
    return ' '.join(string)

lista1 = ['eu', 'estou', 'estudando']
lista2 = ['python', 'há', 'três', 'meses']
print(intercalar_listas(lista1, lista2))