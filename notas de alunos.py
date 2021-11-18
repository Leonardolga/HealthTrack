'''
Enunciado: Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que tem número ímpar na chamada (1, 3, 5, ..., 47, 49) e depois as notas dos 25 alunos que tem número par (2, 4, 6,..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.

Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte padrão:
VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.
Obs: o código feito e feito para uso academico, e apenas utiliza funções aprendidas durante o curso da faculdade.
'''


nota_impartotal = 0.0
nota_partotal = 0.0
for i in range(1,50,2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
    nota_impar = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
    nota_impartotal = float(nota_impar + nota_impartotal)

for x in range(2,50,2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    nota_par = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {x}: "))
    nota_partotal = float(nota_par + nota_partotal)

nota_mediaimpar= float(nota_impartotal/25)
nota_mediapar= float(nota_partotal/25)

if nota_mediaimpar > nota_mediapar:
    print("A média da nota dos alunos impares foi maior!")
else:
    print("A média da nota dos alunos pares foi maior!")