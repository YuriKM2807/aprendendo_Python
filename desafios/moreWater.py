alturas = [1, 8, 6, 2, 5, 4, 8, 3, 7]
i = 0
j = len(alturas) - 1
mAlt = 0
while i != j:
    height = min(alturas[i], alturas[j])
    base = j-i
    if (base * height) > mAlt:
        mAlt = (base * height)
        posX = i
        posY = j
    if height == alturas[i]:
        i += 1
    else:
        j -= 1
    
    
print(mAlt," Na Posicao X: ", posX," Y: ",posY)