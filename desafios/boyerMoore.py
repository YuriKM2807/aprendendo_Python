def boyermoore(nums: list):
    cont = 0
    contagem_real = 0
        
    for n in nums:
        if cont == 0:
            var = n
            cont = 1
        elif n == var:
            cont += 1
        else:
            cont -= 1

    for n in nums:
        if n == var:
            contagem_real += 1

    if contagem_real > len(nums) // 2:
        return var
    
    return None
        
numeros = [1,2,4,2,2,2,5,2,7,2,0,2,6,2]
result = boyermoore(numeros)
if result is not None:
    print("O resultado eh ", result)
else:
    print("Nao ha numero n/2 na lista!")