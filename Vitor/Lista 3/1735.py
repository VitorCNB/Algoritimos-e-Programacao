# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1735

valorInicial = int(input())
valorFinal = int(input())

while valorInicial >= valorFinal:
    print(valorInicial)
    valorInicial = valorInicial - 1
print("Fogo!")