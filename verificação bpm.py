'''
Enunciado:O projeto HealthTrack é o máximo e tem grande possibilidade de impactar positivamente a vida das pessoas. Mesmo que a solução final não utilize uma implementação em Python, podemos aproveitar a oportunidade para desenvolver o algoritmo que resolva um problema simples: verificar se os batimentos cardíacos por minuto se encontram na faixa adequada. Para isso, você deve solicitar que o usuário informe o seu número de BATIMENTOS POR MINUTO (BPM) e a IDADE. A partir disso o script deva verificar e exibir uma mensagem informando se os batimentos do usuário encontram-se DENTRO da faixa adequada, ACIMA da faixa adequada ou ABAIXO da faixa adequada):
IDADE                             BPM

Até 2 anos                      120 a 140
De 8 anos até 17 anos           80 a 100
Adulto sedentário (18 a 65)     70 a 80
Idosos (maior 65 anos)          50 a 60
Obs: o código feito e feito para uso academico, e apenas utiliza funções aprendidas durante o curso da faculdade.
 '''

BPM = int(input("Informe a quantidade de batimentos por minutos (BPM): "))
idade = int(input("Informe a sua idade: "))

if idade <= 2 and 140 >= BPM >= 120:
    print("Os batimentos do usuário encontram-se DENTRO da faixa adequada")
elif idade <= 2 and BPM > 140:
    print("Os batimentos do usuário encontram-se ACIMA da faixa adequada")
elif idade <= 2 and BPM < 120:
    print("Os batimentos do usuário encontram-se ABAIXO da faixa adequada")
elif 8 <= idade <= 17 and 100 >= BPM >= 80:
    print("Os batimentos do usuário encontram-se DENTRO da faixa adequada")
elif 8 <= idade <= 17 and BPM > 100:
    print("Os batimentos do usuário encontram-se ACIMA da faixa adequada")
elif 8 <= idade <= 17 and BPM < 80:
    print("Os batimentos do usuário encontram-se ABAIXO da faixa adequada")
elif 18 <= idade <= 65 and 70 <= BPM <= 80:
    print("Os batimentos do usuário encontram-se DENTRO da faixa adequada")
elif 18 <= idade <= 65 and BPM > 80:
    print("Os batimentos do usuário encontram-se ACIMA da faixa adequada")
elif 18 <= idade <= 65 and BPM < 70:
    print("Os batimentos do usuário encontram-se ABAIXO da faixa adequada")
elif 65 < idade and 50 <= BPM <= 60:
    print("Os batimentos do usuário encontram-se DENTRO da faixa adequada")
elif 65 < idade and BPM > 60:
    print("Os batimentos do usuário encontram-se ACIMA da faixa adequada")
elif 65 < idade and BPM < 50:
    print("Os batimentos do usuário encontram-se ABAIXO da faixa adequada")
