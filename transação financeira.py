'''
Enunciado: Olhando para o mercado de educação infantil, você e sua equipe decidem criar um aplicativo onde as crianças aprendam a controlar os seus gastos.

Como forma de validar um protótipo, foi solicitado que você crie um script simples, em que o usuário deve informar QUANTAS TRANSAÇÕES financeiras realizou ao longo de um dia e, na sequência, deve informar o VALOR DE CADA UMA das transações que realizou.

Seu programa deverá exibir, ao final, o valor total gasto pelo usuário e também a média do valor de cada transação.
Obs: o código feito e feito para uso academico, e apenas utiliza funções aprendidas durante o curso da faculdade.
'''
n = int(input("Quantas transações financeiras foram realizadas ao longo do dia? "))
i = 0
transacoes_total = 0.0

while (i != n):
    transacoes = float(input("Informe o valor da transação: "))
    transacoes_total = float(transacoes + transacoes_total)
    i = i + 1

transacoes_media = float(transacoes_total/n)
print(f"O valor total das transações e o valor médio das transações foram de respectivamente: {transacoes_total: .2f} e {transacoes_media: .2f}")