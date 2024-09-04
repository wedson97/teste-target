SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

total = SP+RJ+MG+ES+Outros

def calcular_percentual(estado, total):
    percentual = (estado*100)/total
    return percentual

print(f'RJ : {calcular_percentual(RJ, total):.2f}%')
print(f'SP : {calcular_percentual(SP, total):.2f}%')
print(f'MG : {calcular_percentual(MG, total):.2f}%')
print(f'ES : {calcular_percentual(ES, total):.2f}%')
print(f'Outros : {calcular_percentual(Outros, total):.2f}%')