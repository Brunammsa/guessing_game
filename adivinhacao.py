import random

print('~~~ Bem vindo ao jogo da adivinhação! ~~~\n')

num_secreto = random.randrange(1, 101)

tentativa = 1
total_tentativas = 0
pontos = 1000

print('Escolha o nível de dificuldade: ')
print('1 - Fácil\n2 - Médio\n3 - Difícil\n')

lvl: int = int(input('Defina o nível: '))

if lvl == 1:
    total_tentativas = 20
elif lvl == 2:
    total_tentativas = 10

elif lvl == 3:
    total_tentativas = 5

for rodada in range(1, total_tentativas + 1):

    print(f'\nTentativa {tentativa} de {total_tentativas}\n')

    chute: int = int(input('Digite um número entre 1 e 100: '))
    print('Seu número foi o', chute)

    if chute < 1:
        print('Digite apenas números entre 1 e 100')
        continue
    elif chute > 100:
        print('Digite apenas números entre 1 e 100')
        continue

    acertou = num_secreto == chute
    maior = chute > num_secreto

    if acertou:
        print(f'Parabéns, você acertou o número e fez {pontos} pontos!')
        break
    else:
        if maior:
            print('Seu chute foi maior do que o número secreto\n')
        else:
            print('Seu chute foi menor do que o número secreto\n')
        tentativa += 1
        pontos_perdidos = abs(num_secreto - chute)
        pontos -= pontos_perdidos

print('Fim do jogo!')
