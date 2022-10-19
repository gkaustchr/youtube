salario = 1200

taxa = 1 + 2/100

c1 = 200
c2 = 120

c1Taxa = c1 * taxa
c2Taxa = c2 * taxa

contas = c1 * taxa + c2 * taxa # (200 + 120) * (1,02)
salarioFinal = salario - contas
print(f'Conta 1 {c1Taxa} - Conta 2 {c2Taxa} - Soma {c1Taxa + c2Taxa} ')
print(f'Total R$ {contas}')
print(f'Salario Final R$ {salarioFinal}')
