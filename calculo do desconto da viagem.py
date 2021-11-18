'''
Enunciado: Viajar é bom demais! Uma agência de viagens está propondo uma estratégia para alavancar as vendas após os impactos da pandemia do coronavírus.
A empresa ofertará descontos progressivos na compra de pacotes, dependendo do número de viajantes que estão no mesmo grupo e moram na mesma residência.
Para ajudar a tornar esse projeto real, você deve criar um algoritmo que receba o VALOR BRUTO do pacote, a CATEGORIA DOS ASSENTOS no vôo e a QUANTIDADE DE VIAJANTES que moram em uma mesma casa e calcule os descontos de acordo com a tabela abaixo:
O programa deverá exibir o valor BRUTO DA VIAGEM (o mesmo que foi digitado), o VALOR DO DESCONTO, o VALOR LÍQUIDO DA VIAGEM (valor bruto menos os descontos) e o VALOR MÉDIO POR VIAJANTE.
Categoria	DESCONTOS

Econômica   2 viajantes             3%
            3 viajantes             4%
            4 viajantes ou mais     5%

Executiva   2 viajantes             5%
            3 viajantes             7%
            4 viajantes ou mais     8%

Primeira classe 2 viajantes         10%
                3 viajantes         15%
                4 viajantes ou mais 20%

Obs: o código feito e feito para uso academico, e apenas utiliza funções aprendidas durante o curso da faculdade.
 '''

valor_bruto = float(input("Qual o valor bruto do pacote? "))
categoria= input("Escolha a categoria do assento? E para Econômica, EX para Executiva, PC para Primeira classe ")
viajantes = int(input("Informe a quantidade de viajantes que moram em uma mesma casa: "))

if categoria.upper() == "E" and viajantes == 2:
    valor_desconto = float(valor_bruto * 0.03)
    valor_liquido = float(valor_bruto - valor_desconto)
    valor_medio = float(valor_liquido/viajantes)
    print(
f"O valor bruto da viagem é de {valor_bruto:.2f} ,o valor do desconto é de {valor_desconto:.2f}, o valor líquido da viagem é de {valor_liquido:.2f}  e o valor médio por viajantes é de {valor_medio:.2f}")
elif categoria.upper() == "E" and viajantes == 3:
    valor_desconto = float(valor_bruto * 0.04)
    valor_liquido = float(valor_bruto - valor_desconto)
    valor_medio = float(valor_liquido / viajantes)
    print(
        f"O valor bruto da viagem é de {valor_bruto:.2f} ,o valor do desconto é de {valor_desconto:.2f}, o valor líquido da viagem é de {valor_liquido:.2f}  e o valor médio por viajantes é de {valor_medio:.2f}")
elif categoria.upper() == "E" and viajantes >=4:
    valor_desconto = float(valor_bruto * 0.05)
    valor_liquido = float(valor_bruto - valor_desconto)
    valor_medio = float(valor_liquido / viajantes)
    print(
        f"O valor bruto da viagem é de {valor_bruto:.2f} ,o valor do desconto é de {valor_desconto:.2f}, o valor líquido da viagem é de {valor_liquido:.2f}  e o valor médio por viajantes é de {valor_medio:.2f}")
elif categoria.upper() == "EX" and viajantes == 2:
    valor_desconto = float(valor_bruto * 0.05)
    valor_liquido = float(valor_bruto - valor_desconto)
    valor_medio = float(valor_liquido / viajantes)
    print(
        f"O valor bruto da viagem é de {valor_bruto:.2f} ,o valor do desconto é de {valor_desconto:.2f}, o valor líquido da viagem é de {valor_liquido:.2f}  e o valor médio por viajantes é de {valor_medio:.2f}")
elif categoria.upper() == "EX" and viajantes == 3:
    valor_desconto = float(valor_bruto * 0.07)
    valor_liquido = float(valor_bruto - valor_desconto)
    valor_medio = float(valor_liquido / viajantes)
    print(
        f"O valor bruto da viagem é de {valor_bruto:.2f} ,o valor do desconto é de {valor_desconto:.2f}, o valor líquido da viagem é de {valor_liquido:.2f}  e o valor médio por viajantes é de {valor_medio:.2f}")
elif categoria.upper() == "EX" and viajantes >=4:
    valor_desconto = float(valor_bruto * 0.08)
    valor_liquido = float(valor_bruto - valor_desconto)
    valor_medio = float(valor_liquido / viajantes)
    print(
        f"O valor bruto da viagem é de {valor_bruto:.2f} ,o valor do desconto é de {valor_desconto:.2f}, o valor líquido da viagem é de {valor_liquido:.2f}  e o valor médio por viajantes é de {valor_medio:.2f}")
elif categoria.upper() == "PC" and viajantes == 2:
    valor_desconto = float(valor_bruto * 0.1)
    valor_liquido = float(valor_bruto - valor_desconto)
    valor_medio = float(valor_liquido / viajantes)
    print(
        f"O valor bruto da viagem é de {valor_bruto:.2f} ,o valor do desconto é de {valor_desconto:.2f}, o valor líquido da viagem é de {valor_liquido:.2f}  e o valor médio por viajantes é de {valor_medio:.2f}")
elif categoria.upper() == "PC" and viajantes == 3:
    valor_desconto = float(valor_bruto * 0.15)
    valor_liquido = float(valor_bruto - valor_desconto)
    valor_medio = float(valor_liquido / viajantes)
    print(
        f"O valor bruto da viagem é de {valor_bruto:.2f} ,o valor do desconto é de {valor_desconto:.2f}, o valor líquido da viagem é de {valor_liquido:.2f}  e o valor médio por viajantes é de {valor_medio:.2f}")
elif categoria.upper() == "PC" and viajantes >= 4:
    valor_desconto = float(valor_bruto * 0.2)
    valor_liquido = float(valor_bruto - valor_desconto)
    valor_medio = float(valor_liquido / viajantes)
    print(
        f"O valor bruto da viagem é de {valor_bruto:.2f} ,o valor do desconto é de {valor_desconto:.2f}, o valor líquido da viagem é de {valor_liquido:.2f}  e o valor médio por viajantes é de {valor_medio:.2f}")