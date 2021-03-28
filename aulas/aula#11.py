print('\033[31mOla, mundo!') #vermelho
print('\033[1;31;43mOla, mundo!')#negrito:vermelho:fundo amarelo
print('\033[1;31;43mOla, mundo!\033[m')#negrito:vermelho:fundo amarelo\sem faixa ate o final
print('\033[4;30;45mOla, mundo!\033[m')#sublinhado:cor branca:fundo roxo\sem faixa ate o final
print('\033[7;30mOla, mundo!\033[m')#invertendo fundo preto por letra branca/ OBS: 7 que faz a inversão
a = 5
b = 3
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')
print(f'Os valores são \033[32;41m{a}\033[m e \033[31;42m{b}\033[m!!!')
nome = 'Márcio'
print('Ola! muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome,'\033[m'))

print('-'*10,'SISTEMA DE CORES','-'*10)
print(' '*9,'STYLE   TEXT  BACK')
print(' '*9,'  \033[0m0\033[m      \033[30m30\033[m    \033[40m40\033[m')
print(' '*9,'  \033[1m1\033[m      \033[31m31\033[m    \033[41m41\033[m')
print(' '*9,'  \033[4m4\033[m      \033[32m32\033[m    \033[42m42\033[m')
print(' '*9,'  \033[7m7\033[m      \033[33m33\033[m    \033[43m43\033[m')
print(' '*9,'         \033[34m34\033[m    \033[44m44\033[m')
print(' '*9,'         \033[35m35\033[m    \033[45m45\033[m')
print(' '*9,'         \033[36m36\033[m    \033[46m46\033[m')
print(' '*9,'         \033[37m37\033[m    \033[47m47\033[m')
print('-'*17,'fim','-'*17)