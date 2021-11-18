''' 
Enunciado : O projeto HealthTrack é o máximo e tem grande possibilidade de impactar positivamente a vida das pessoas. Mesmo que a solução final não utilize uma implementação em Python, podemos aproveitar a oportunidade para desenvolver o algoritmo que resolva um problema simples: o cálculo do IMC sem distinção de sexo biológico. Por isso, você deve desenvolver um script que solicite o PESO e a ALTURA de uma pessoa. A partir disso, o script deva calcular o IMC (PESO dividido pelo quadrado da ALTURA) e informar em quais das faixas a pessoa se encontra.

Obs: o código feito e feito para uso academico, e apenas utiliza funções aprendidas durante o curso da faculdade.
'''

altura = float(input("Insira sua altura: "))
peso = float(input("Insira seu peso: "))
imc = float(peso/(altura*altura))
if imc >= 40:
    print("Obesidade Grau III")
elif imc == 39.99 or imc >= 35.00:
    print("Obesidade Grau II")
elif imc == 34.99 or imc >= 30.00:
    print("Obesidade Grau I")
elif imc == 29.99 or imc >= 25.00:
    print("Sobrepeso")
elif imc == 24.99 or imc >= 18.50:
    print("Peso ideal")
elif imc == 18.49 or imc >= 17.00:
    print("Baixo peso Grau I")
elif imc == 16.99 or imc >= 16.00:
    print("Baixo peso Grau II")
elif imc < 16.00:
    print("Baixo peso Grau III")

print("Seu IMC é de {:.2f}!".format(imc))