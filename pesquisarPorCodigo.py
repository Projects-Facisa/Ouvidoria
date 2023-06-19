from operacoesbd import *

def pesquisarManifestacaoPorCodigo(conexao):
    comandoSql = "select count(*) from manifestacao"
    manifestacoes = listarBancoDados(conexao, comandoSql)
    manifestacoes = manifestacoes[0][0]

    if manifestacoes == 0:
        print('Não há manifestações a serem listadas!')

    else:
        codigo = input('Digite o código da manifestação que desejada listar: ')
        print()

        try:
            int(codigo)
            comandoSql = "select count(*) from manifestacao where codigo = " + codigo
            manifestacoes = listarBancoDados(conexao, comandoSql)
            manifestacoes = manifestacoes[0][0]

            if manifestacoes == 0:
                print('Não existe manifestação com este código!')
            else:
                comandoSql = "select * from manifestacao where codigo = " + codigo
                manifestacoes = listarBancoDados(conexao, comandoSql)

                for i in manifestacoes:
                    print('Código:', i[0])
                    print('Título:', i[1])
                    print('Descrição:', i[2])
                    print('Tipo:', i[3])
                    print('Autor:', i[4])

        except ValueError:
            print('Não existe manifestação com este código!')
