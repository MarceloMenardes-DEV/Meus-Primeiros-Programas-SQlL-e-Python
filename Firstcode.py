#advinhe o numero marcelo e advinhe a palavra duas fases v1
import random


print('Primeiro jogo advinhe o numero')

def passar_de_fase1():
 
  num_al=random.randint(1,10)
  tentativas=6
 
  print('Você tem', tentativas, 'tentativas')
 
  while True:
    num_user=int(input('digite um numero de 1 até 10:  '))
   
    if num_user==num_al:
     print('Você acertou o numero é' , num_al)
     return True
   
    elif num_user> num_al:
      print('Você errou o numero é menor tente de novo\n')
      tentativas-=1
      print('\nVocê ainda tem',tentativas,'tentativas')

    else:
     tentativas-=1
     print('Você errou o numero é maior tente de novo\n')
     print('\nVocê ainda tem',tentativas,'tentativas')
    if tentativas==0:
      print('\n Suas tentativas acabaram \nVocê perdeu o jogo Volte ao inicio')
      return False


def passar_de_fase2():
  tentativas=8
  print('\nProximo jogo advinhe a palavra')
  print('Você tem', tentativas, 'tentativas')
  lista=('TECNOLOGIA','INTELIGENCIA ARTIFICIAL','GTAV','VASCO DA GAMA')
  palavra_adv=random.choice(lista)
  palpite_error=[]
  palpite_certo=[]


  while True:
    
    letra_user=str(input('digite uma letra\n').upper())
    
    painel = ''
    
    for p in palavra_adv:
            if p == ' ':
                painel += '  '
            elif p in letra_user:
                painel += p + ' '
            elif p in palpite_certo:
                painel += p + ' '

            else:
                painel += '_ '

    print('\nPalavra:', painel)

    if tentativas==0:
       print('\nSuas tentativas acabaram \nVocê perde o jogo Volte ao inicio a palavra era',palavra_adv)
       return False

    elif '_' not in painel:
      print('\nParabens Você Venceu o Jogo\na palavra é', palavra_adv)
      return True

    elif letra_user in palpite_certo:
      print('Você ja usou esse letra tente de novo')
      palpite_certo.append(letra_user)
      palpite_certo.remove(letra_user)
      print('\nVocê ainda tem',tentativas,'tentativas')

    elif letra_user in  palpite_error:
      print('Você ja usou esse letra tente de novo')
      palpite_error.append(letra_user)
      palpite_error.remove(letra_user)
      print('\nVocê ainda tem',tentativas,'tentativas')

    elif letra_user not in palavra_adv:
      print('Você errou a Letra Tente denovo\n')
      tentativas-=1
      palpite_error.append(letra_user)
      print('\nVocê ainda tem',tentativas,'tentativas')

    elif letra_user in palavra_adv:
      print('Você acertou uma letra continue  assim')
      tentativas=tentativas
      palpite_certo.append(letra_user)
      print('\nVocê ainda tem',tentativas,'tentativas')


    print('letras usadas:',palpite_certo+palpite_error)
    print('letras usadas Erradas:' ,palpite_error)
    print('letras usadas Certas:' ,palpite_certo)

venceu_fase1 = passar_de_fase1()
if venceu_fase1:
    passar_de_fase2()