print('Lista de convidados')
print('############################')

convidados_num = input('Coloque a quantidade de convidados: ')
lista_de_convidados = []

i = 1

while i <= int(convidados_num): #ou outra forma de fazer esse prorama for i in range(int(convidados_num))
    convidado_nome = input('Coloque o nome do(s) convidado(s): #'+ str(i) +': ')
    lista_de_convidados.append(convidado_nome)
    i += 1

print('Serão', convidados_num, 'convidados')
print('LISTA DE CONVIDADOS')

for convidado in lista_de_convidados:
    print(convidado)