# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

idadeTotal = 0
for pessoa in range(0,4):
  idade = int(input())
  peso = float(input())
  idadeTotal = (idadeTotal + idade)
  
  if peso > 90:
    contador = 0
    contador = contador + 1
      
print("Qtd pessoas > 90 Kg: %i"  %(contador))
print("Idade média: %.2f" %(idadeTotal/4))