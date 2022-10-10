# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

valor_ph = float(input())
horas_mes = float(input())
 
salario_bruto = valor_ph * horas_mes
imposto = salario_bruto * 0.11
inss = salario_bruto * 0.08 
sindicato = salario_bruto * 0.05

liquido = (salario_bruto - imposto - inss - sindicato)

print("Salário Bruto: R$%.2f" %(salario_bruto))
print("Imposto: R$%.2f" %(imposto))
print("INSS: R$%.2f" %(inss))
print("Sindicato: R$%.2f" %(sindicato))
print("Líquido: R$%.2f" %(liquido))