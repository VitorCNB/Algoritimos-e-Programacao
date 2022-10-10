# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

n = int(input())
contador = 2
resultado = 1
while contador <= n:
    resultado = contador * resultado
    contador = contador + 1
print("%i! = %i" %(n, resultado))