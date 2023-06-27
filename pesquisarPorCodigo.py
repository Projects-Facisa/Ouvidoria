from operacoesbd import *

def pesquisarManifestacaoPorCodigo(conexao):
    codigo = 'entrada'
    while codigo != 0:
        try:
            codigo = int(input('Digite o código da manifestação ou (0).Para voltar: '))   # Input do código
            print()
            comandoSql = "select * from manifestacao where codigo = " + str(codigo)   # Execução do código no banco de dados
            manifestacoes = listarBancoDados(conexao, comandoSql)

            if codigo == 0:   # Voltando
                print('Voltando...')

            elif len(manifestacoes) == 0:   # Não há manifestações com este código
                print('Não há manifestação cadastrada neste código!')
                print()

            else:
                for i in manifestacoes:   # Print da manifestação
                    print('Código:', i[0])
                    print('Título:', i[1])
                    print('Descrição:', i[2])
                    print('Tipo:', i[3])
                    print('Autor:', i[4])
                codigo = 0

        except ValueError:   # Código inválido
            print()
            print('Código inválido!')
            print()
