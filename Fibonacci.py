i1, i2 = 0, 1
variavel = 55

while i2 <= variavel:
    if i2 == variavel:
        print('Tem em Fibonacci:', variavel)
        break
    i1, i2 = i2, i1 + i2
else:
    print('Não tem em Fibonacci')