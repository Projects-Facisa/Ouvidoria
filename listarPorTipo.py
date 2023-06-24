from operacoesbd import *

def listarManifestacaoPorTipo(conexao,opcao):
    opcao = int(input('Digite o número da sua opcão: '))

    if opcao < 0 or opcao > 3:
        print('Opcao Invalida!')
        print() 
    else:
        if opcao == 1:
            tip = "'Elogio'"
            tipoPlural = 'Elogios'

        elif opcao == 2:
            tip = "'Sugestao'"
            tipoPlural = 'Sugestoes'

        elif opcao == 3:
            tip = "'Reclamacao'"
            tipoPlural = 'Reclamacoes'

        if opcao == 0:
            print('Voltando...')

        else:
            consultaListagem = 'select * from manifestacao where tipo = ' + tip
            resultado = listarBancoDados(conexao, consultaListagem)

            if len(resultado) == 0:
                print('Nao ha', tipoPlural,'a serem listados!')
                print()
            else:
                manifestacao = listarBancoDados(conexao, consultaListagem)
                for i in manifestacao:
                    print('codigo', i[0], '-', i[1], '-', i[4])