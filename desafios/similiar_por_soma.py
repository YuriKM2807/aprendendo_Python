'''
    Two Sum (O Clássico): Dado um array de números e um valor alvo, encontre os dois índices que somados dão esse alvo.
        Dica: Tente resolver usando apenas um "passo" na lista (Dicionários são seus melhores amigos aqui).
'''
def twoSum():
    nums = [1, 2, 3, 7, 11, 15, 16]
    i = int(input("Digite o valor alvo: "))
    n1 = 0
    for n in nums:
        if i-n in nums:
            print(n," + ", i-n," = ", i)
            return
    print("Nao eh possivel somar esse resultado!")
        
twoSum()