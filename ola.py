# Criando um comando Ola


# def ola(nome):
 #  print(f'ola {nome}! Seja bem vindo(a)!')
#ola('Joao')
#ola('Maria')
#ola ('Pedro')

# ola(input('Digite seu nome: '))
#
def area(largura, profundidade): 
    return largura * profundidade
    
def volume(largura, profundidade, altura):
    return area(largura, profundidade) * altura

print(area(2,3))
print(volume(2,3,5))