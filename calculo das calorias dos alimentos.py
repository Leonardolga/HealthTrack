'''
Enunciado: O projeto HealthTrack está tomando forma e podemos pensar em algoritmos que possam ser reaproveitados quando estivermos implementando o front e o back do nosso sistema. Uma das funções mais procuradas por usuários de aplicativos de saúde é o de controle de calorias ingeridas em um dia. Por essa razão, você deve elaborar um algoritmo implementado em Python em que o usuário informe quantos alimentos consumiu naquele dia e depois possa informar o número de calorias de cada um dos alimentos.
Obs: o código feito e feito para uso academico, e apenas utiliza funções aprendidas durante o curso da faculdade.
'''
i = 0
n = int(input("Quantos alimentos foram consumidos durante o dia? "))
c_total = 0.0

while (i != n):
    c = float(input("Informe as calorias do alimento: "))
    c_total = float(c_total + c)
    i = i +1

print("A quantidade de caloridas totais foram de: {}".format(c_total))