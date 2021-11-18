'''
Enunciado: Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.
Obs: o código feito e feito para uso academico, e apenas utiliza funções aprendidas durante o curso da faculdade.
 '''

segunda_feira = int(input("Informe a quantidade de votos que segunda-feira recebeu: "))
terca_feira = int(input("Informe a quantidade de votos que terça-feira recebeu: "))
quarta_feira = int(input("Informe a quantidade de votos que quarta-feira recebeu: "))
quinta_feira = int(input("Informe a quantidade de votos que quinta-feira recebeu: "))
sexta_feira = int(input("Informe a quantidade de votos que sexta-feira recebeu: "))

if segunda_feira > terca_feira and segunda_feira > quarta_feira and segunda_feira > quinta_feira and segunda_feira > sexta_feira:
    print("Segunda_feira foi escolhida com a maior quantidade de votos")
elif  terca_feira > quarta_feira and terca_feira > quinta_feira and terca_feira > sexta_feira:
    print("Terça_feira foi escolhida com a maior quantidade de votos")
elif quarta_feira > quinta_feira and quarta_feira > sexta_feira:
    print("Quarta_feira foi escolhida com a maior quantidade de votos")
elif quinta_feira > sexta_feira:
    print("Quinta_feira foi escolhida com a maior quantidade de votos")
else:
    print("Sexta_feira foi escolhida com a maior quantidade de votos")