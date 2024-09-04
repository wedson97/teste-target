import json

with open('faturamento.json') as file:
    dados = json.load(file)

faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

media_mensal = sum(faturamentos) / len(faturamentos)

dias_acima_da_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)
 
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
