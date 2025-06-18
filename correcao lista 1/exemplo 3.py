def calculaDiametro(raio):
    return 2 * raio

def calculaCircunferencia(pi, raio):
    return pi * raio * 2

def calculaAreaCircunferencia(pi, raio):
    return pi * (raio**2)

raio = float(input("Digite o valor do raio:"))
pi = 3.14159


diametro =calculaDiametro(raio)
circunferencia = calculaCircunferencia(pi,raio)
area = calculaAreaCircunferencia(pi, raio)

print("O diametro é de: ", diametro)
print("A medida da circunferencia é de: ", circunferencia)
print("A area da circunferencia é de: ", area)