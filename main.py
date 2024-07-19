import jogo as j
import fileHandler as fH

def mostrar_menu():
    print('='* 30)
    print(' '* 7 + 'JOGO DA FORCA')
    print('=' * 30)
    print('\n1 - JOGAR')
    print('2 - SCORE')
    print('3 - SAIR\n')
    print('=' * 30)

arquivo = 'score.txt'
if fH.existeArquivo(arquivo):
    print('Arquivo localizado!')
else:
    print('Arquivo NÃO EXISTE.')
    fH.criaArquivo(arquivo)

while True:
    mostrar_menu()
    opcao = int(input('Escolha a opção (1/2/3): '))

    if opcao == 1:
        print('Iniciar Jogo!')
        j.jogar()

    elif opcao == 2:
        print('SCORE:')
        dados = fH.listarArquivo('score.txt')
        if not dados:
            print('Score vázio.')
        else:
            i = 1
            for jogador in dados:
                jogador = jogador.split(';')
                print(f'{i} -> {jogador[0]}, Pontuação: {jogador[1][:-1]}')
                i += 1

    elif opcao == 3:
        print('Saindo do jogo. Até mais!')
        break
    else:
        print('Opção inválida. Tente outra.')