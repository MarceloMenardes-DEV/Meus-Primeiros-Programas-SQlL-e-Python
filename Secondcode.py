import random

lista='pedra','papel','tesoura'
escolha_comp =random.choice(lista)

try:
     for i in range (3):
          score=0
          escolha_comp =random.choice(lista)
          escolha_user=(input("Escolha Pedra Papel ou Tesoura:")).lower()


          if escolha_user=='pedra' and escolha_comp=='tesoura'or escolha_user=='papel' and escolha_comp=='pedra' or escolha_user=='pedra' and escolha_comp=='tesoura':#usuario ganha
             score+=1
             print(f'Você Ganhou Pontos:{score}/3 \n\nescolha do computador {escolha_comp}\n\nescolha do usuario {escolha_user}')




          elif escolha_user=='papel' and escolha_comp=='tesoura'or escolha_user=='pedra' and escolha_comp=='papel' or escolha_user=='tesoura' and escolha_comp=='pedra': #usuario perde
            if score > 0:
              score-=1
            print(f'Você Perdeu Pontos:{score}/3 \n\nescolha do computador {escolha_comp}\n\nescolha do usuario {escolha_user}')



          elif escolha_user==escolha_comp: #empate
            score=score
            print(f'Empate Pontos:{score}/3 \n\nescolha do computador {escolha_comp}\n\nescolha do usuario {escolha_user}')



          else:
             print('\nescolha invalida')
except:
  print('\nerro tente novamente')

if score>=2:
    print('\nVocê Ganhou o jogo')
if score<2:
    print('\nVocê Perdeu o Jogo')
