
#Exercício 4 — Estacionamento
#Um estacionamento cobra:

#até 1 hora: 8,00;
#acima de 1 hora e até 3 horas: 8,00 + 5,00 por hora adicional;
#acima de 3 horas: 18,00 + 3,00 por hora adicional.
#Peça a quantidade de horas inteiras que o veículo permaneceu estacionado.

#Além disso:

#aos fins de semana, há desconto de 20%;
#clientes conveniados recebem mais 10% de desconto sobre o valor já calculado.
#Peça também:

#dia da semana;
#se o cliente é conveniado (sim ou não).
#Mostre o valor final. Se a quantidade de horas for menor ou igual a zero, informe Tempo inválido.

tempo=int(input('Digite o tempo que ficou estacionado: '))
convenio= input('È conveniado ? (sim ou não) ').lower().strip()
dia_semana= input('Qual dia é Hoje: ').lower().strip()

lista_ut=['segunda','terça','quarta','quinta','sexta']

lista_fds=['sabado','sábado','domingo',]

valor_est=0

if convenio == 'sim'and dia_semana in lista_ut :
   if tempo<=1:
       valor_est=8-(8 *0.1)
       print(f'Valor a pagar: {valor_est}')
   elif tempo ==2:
     valor_est=(8+5)-(8 + 5)*0.1
     print(f'Valor a pagar: {valor_est}')
   elif tempo ==3:
        valor_est=-(8+10)-(8 + 10)*0.1
        print(f'Valor a pagar: {valor_est}')
   elif tempo >3:
       valor_est=(3*(tempo-3))+18-((3*(tempo-3))+18)*0.1
       print(f'Valor a pagar: {valor_est}')

elif convenio == 'sim'and dia_semana in lista_fds:
   if tempo<1:
         valor_est=8-(8 *0.3)
         print(f'Valor a pagar: {valor_est}')
   elif tempo ==2:
       valor_est=(8+5)-(8 + 5)*0.3
       print(f'Valor a pagar: {valor_est}')
   elif tempo ==3:
        valor_est=(8+10)-(8 + 10)*0.3
        print(f'Valor a pagar: {valor_est}')
   elif tempo >3:
        valor_est=(3*(tempo-3))+18-((3*(tempo-3))+18)*0.3
        print(f'Valor a pagar: {valor_est}')

elif  convenio == 'não'and dia_semana in lista_ut:
   if tempo<=1:
       valor_est=8
       print(f'Valor a pagar: {valor_est}')
   elif tempo ==2:
        valor_est=8 + 5
        print(f'Valor a pagar: {valor_est}')
   elif tempo ==3:
        valor_est=8 + 10
        print(f'Valor a pagar: {valor_est}')
   elif tempo >3:
        valor_est=(3*(tempo-3))+18
        print(f'Valor a pagar: {valor_est}')

elif convenio == 'não'and dia_semana in lista_fds:
   if tempo <=1:
      valor_est=8-(8 *0.2)
      print(f'Valor a pagar: {valor_est}')
   elif tempo ==2:
     valor_est=(8+5)-(8 + 5)*0.2
     print(f'Valor a pagar: {valor_est}')
   elif tempo ==3:
        valor_est=(8+10)-(8 + 10)*0.2
        print(f'Valor a pagar: {valor_est}')
   elif tempo >3:
      valor_est=((3*(tempo-3))+18)-((3*(tempo-3))+18)*0.2
      print(f'Valor a pagar: {valor_est}')
elif tempo <=0:
    print('Tempo Invalido Deve Ser Maior que 0')
else:
    print('Resposta Invalida')
       