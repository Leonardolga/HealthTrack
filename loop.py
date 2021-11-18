'''
Enunciado:Um grande cliente seu sofreu um ataque hacker: o servidor foi sequestrado por um software malicioso, que criptografou todos os discos e pede a digitação de uma senha para a liberação da máquina. E é claro que os criminosos exigem um pagamento para informar a senha.

Ao analisar o código do programa deles, porém, você descobre que a senha é composta da palavra “LIBERDADE” seguida do fatorial dos minutos que a máquina estiver marcando no momento da digitação da senha (se a máquina estiver marcando 5 minutos, a senha será LIBERDADE120). Crie um programa que receba do usuário os minutos atuais e exiba na tela a senha necessária para desbloqueio. ATENÇÃO: seu programa não pode utilizar funções prontas para o cálculo do fatorial. Ele deve obrigatoriamente utilizar loop.
Obs: o código feito e feito para uso academico, e apenas utiliza funções aprendidas durante o curso da faculdade.

'''
i = int(input("Digite os minutos que a máquina está marcando nesse exato momento: "))
z = i
y = 1
for x in range(0,z,1):
    y = int(y * i)
    i = i -1
print(f"A senha a ser usada pelo usuário é: LIBERDADE{y}")