''' Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os 
parênteses abertos e fechados na ordem correta.'''

#resolução do curso

expr = str(input('Digite uma expressão matemática: '))
pilha = []

for simb in expr:
    if simb == '(':
     pilha.append('(')
    elif simb == ')':
      if len(pilha) > 0:
        pilha.pop()#retira o ultimo item
      else:
        pilha.append(')')
        break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
  print('Sua espressão está errada!')

#conceito de pilha
#https://www.cos.ufrj.br/~rfarias/cos121/pilhas.html