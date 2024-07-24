# O matemático Malbataam precisa de um programa para calcular o valor de uma função do primeiro grau ou uma função do segundo grau de acordo com o que o usuário solicitar.  

#   Se o usuário escolher calcular uma função do primeiro grau, ele deve passar os parâmetro A, B e o valor de X e o programa deve calcular f(x) = ax + b.
#   Por exemplo, se o usuário escolher A=2 , B=3 e X=1 então o programa deve calcular o valor de f(x) = 2*1 + 3 ou seja deve retornar 5
  
#   Se o usuário escolher calcular uma função do segundo grau, ele deverá passar os valores dos parâmetros A, B, C e X e o programa deve calcular f(x) = Ax**2+ Bx + C.
#   Por exemplo se o usuário escolher A=1, B=3, C=2 e X=1 então o programa deve calcular o valor de f(x)=1*[(1)**2]+3*1+2 ou seja deve retornar 6

# obs.: Deverá ser criado funções no programa


def funcaoprimeirograu(a,b,x):
    resultado = a*x+b 
    return resultado



def funcaosegundograu(a,b,c,x):
    resultado = a*(x**2)+b*x+c
    return resultado 




#a = int(input('qual função voce deseja calcular? digite 1 para função de p'))


# def qualcalculo():
        
#     print('#--------------| matematica Malbataam |--------------#')
#     print('qual tipo de função deseja calcular')
#     print('1 - função de primeiro grau')
#     print('2 - função de segundo  grau')
#     pp = int(input('qual função voce deseja calcular?'))
#     return pp

resposta = 's'
while resposta=='s':
    print('#--------------| matematica Malbataam |--------------#')
    print('qual tipo de função deseja calcular')
    print('1 - função de primeiro grau')
    print('2 - função de segundo  grau')
    pp = int(input('qual função voce deseja calcular?'))

    a = int(input('digite o coefieciente A:'))

    print("#--------------------------------#")

    b = int(input('digite o coefieciente b:'))


    print("#--------------------------------#")

    x = int(input('digite o coefieciente x:'))

    print("#--------------------------------#")

    if(pp==2):
        c = int(input('digite coefieciente c:'))

    if (pp == 1):

        print (f'O valor do seu calculo é {funcaoprimeirograu(a,b,x)} ')
    else:
        print (f'O valor do seu calculo é {funcaosegundograu(a,b,c,x)} ')

    resposta = input('deseja continuar mestre(S/N)')

    if(resposta !='s'):
        print('obrigado, até uma proxima!')

    