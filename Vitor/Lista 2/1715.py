# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

tipoCliente = int(input())
valorCompra = float(input())

if tipoCliente == 1:
  valorVenda = valorCompra
  print("Valor total a ser pago: R$%.2f" % (valorVenda))
elif tipoCliente == 2:
  valorVenda = valorCompra - valorCompra * 0.13
  print("Valor total a ser pago: R$%.2f" % (valorVenda))
elif tipoCliente == 3:
  valorVenda = valorCompra - valorCompra * 0.07
  print("Valor total a ser pago: R$%.2f" % (valorVenda))
else:
  print("OPÇÃO INVÁLIDA!")