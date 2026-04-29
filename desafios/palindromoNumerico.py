def eh_palindromo(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    numA = x
    numB = 0
    
    while numA > numB:
        ultimo_digito = numA % 10
        numB = ultimo_digito + (numB * 10) 
        numA = numA // 10
        
    return numA == numB or numA == numB // 10

if eh_palindromo(int(input("Digite um Numero: "))):
    print("Eh um palindromo")
else:
    print("Nao eh um palindromo")
    