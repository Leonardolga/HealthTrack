 '''Cadastro de usuário'''

usuario = []
nome = input("Cadastrar nome do usuário: ")
usuario.append(nome)
while True:
  tipo = input("Usuário é PF ou PJ?")
  usuario.append(tipo)
  if tipo.upper() == 'PF' or tipo.upper() == 'PJ':
    break

while True:
  x = input("Deseja alterar os dados do usuário? Digite sim ou nao  ")
  if x.upper() == 'SIM':
    usuario[0] = input("Novo nome usuário: ")
    while True:
      usuario[1] =input("Usuário é PF ou PJ? ")
      if usuario[1].upper() == 'PF' or usuario[1].upper() == 'PJ':
        break
  if x.upper() == 'SIM' or x.upper() == 'NAO':
     break
x = input("Deseja excluir os dados do usuário? Digite sim ou nao ")
if x.upper() == 'SIM':
    print('Usuário deletado')
    usuario = 0
else:
    if usuario[1].upper() == 'PF':
        print('O usuário é uma pessoa física')
    else:
        print('O usuário é uma pessoa jurídica')

    x = input("Você aceita os termos da lei de proteção de dados? Digite sim ou nao ")
    if x.upper() == 'SIM':
        print('Termos aceitos!')
    else:
        print('Desculpas, não iremos prosseguir pois  os termos da lei de proteção de dados? não foram aceitos')