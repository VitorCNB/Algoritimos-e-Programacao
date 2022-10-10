# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

tipo = (input())
salario = float(input())

if tipo == "A":
    novoSalario = salario + salario * 0.1
    print("Novo salário: R$%.2f" %(novoSalario))
elif tipo == "B":
    novoSalario = salario + salario * 0.15
    print("Novo salário: R$%.2f" %(novoSalario))
elif tipo == "C":
    novoSalario = salario + salario * 0.20
    print("Novo salário: R$%.2f" %(novoSalario))