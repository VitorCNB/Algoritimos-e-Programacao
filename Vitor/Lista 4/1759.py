# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

salario = 1000
ano = int(input())

if ano < 2006:
    
  print("O ano informado deverá ser > 2005!")

else:
  percentual = 0.015
  salarioFinal = salario + (salario * percentual)
  for anoAtual in range (2006, ano):
    percentual = percentual + 0.01
    salarioFinal = salarioFinal + (salarioFinal * percentual)
                         
  print("Salário atual: R$%.2f" %(salarioFinal))