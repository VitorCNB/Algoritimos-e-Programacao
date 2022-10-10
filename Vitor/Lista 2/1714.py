# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

produto = float(input())
vender45 = produto * 0.45    
vender30 = produto * 0.30
if produto < 20:
    print("Valor de venda: R$%.2f" %(produto + vender45))
else:
    print("Valor de venda: R$%.2f" %(produto + vender30))