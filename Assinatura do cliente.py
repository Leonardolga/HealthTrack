'''
Enunciado: Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.

Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:
p - platinum (5% * faturamento)
g - gold (10% * faturamento)
s - silver (20% * faturamento)
b - basic (30% * faturamento)

Obs: o código feito e feito para uso academico, e apenas utiliza funções aprendidas durante o curso da faculdade.
'''

assinatura = input("Escolha sua assinatura: P para Platinum, G para gold, S para silver, B para basic: ")
faturamento = float(input("Digite seu faturamento: "))



if assinatura.upper() == "P":
    valor_bonus = float(faturamento * 0.05)
    print("O valor bonus a ser pago é de {:.2f}!".format(valor_bonus))
elif assinatura.upper() == "G":
    valor_bonus = float(faturamento * 0.1)
    print("O valor bonus a ser pago é de {:.2f}!".format(valor_bonus))
elif assinatura.upper() == "S":
    valor_bonus = float(faturamento * 0.2)
    print("O valor bonus a ser pago é de {:.2f}!".format(valor_bonus))
elif assinatura.upper() == "B":
    valor_bonus = float(faturamento * 0.3)
    print("O valor bonus a ser pago é de {:.2f}!".format(valor_bonus))