# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = (input())
numHora_extra = float(input())

print("Nome: %s" %(nome))

salarioMin = 1192.40
valorHora = 10.00
salarioHora_extra = numHora_extra * valorHora
salarioBruto = 3 * salarioMin + salarioHora_extra

if salarioBruto > 2000.00:
    descontoINSS = salarioBruto * 0.12
    print("Salário bruto: R$%.2f" %(salarioBruto))
else:
    salarioBruto = salarioBruto * 0.05

if salarioBruto > 2500.00:
    descontoIR = salarioBruto * 0.20
    salarioLiquido = salarioBruto - descontoINSS - descontoIR
    print("Salário líquido: R$%.2f" %(salarioLiquido))
else:
    descontoINSS = 0