import random;

print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o número secreto
numeroSecreto = random.randrange(1,101)
#print(numeroSecreto)
#Definindo o número de tentativas e rodada
numeroTentativas = 0
rodada = 1
pontos = 1000

print("qual nivel de dificudade?")
print("(1)-facil, (2)-medio, (3)-dificil")

nivel = int(input("defina o nivel: "))

#Vamos mudar o numero de tentativas conforme a dificudade
if(nivel == 1):
    numeroTentativas = 15
elif(nivel == 2):
    numeroTentativas = 10
else:
    numeroTentativas = 5


while(rodada <= numeroTentativas):
    print('Tentativa',rodada, 'de' , numeroTentativas)
 
#Recebendo o chute do jogador
    chuteString = input('Digite um número entre 1 e 100: ')
    chute = int(chuteString)

#Declarando as condições
    if (numeroSecreto == chute):
        print('Você acertou!')
        break
    elif(chute>numeroSecreto):
        print('Você errou!! O número secreto é um número menor')
    else:
        print('Você errou!! O número secreto é um número maior')
        pontos_perdidos = abs(numeroSecreto - chute);
        pontos = pntos - pontos_perdidos

    #numeroTentativas = numeroTentativas - 1
    rodada = rodada + 1



#Aula Elif 26.02.24

