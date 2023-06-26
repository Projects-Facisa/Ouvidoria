from operacoesbd import *

def pesquisarManifestacaoPorCodigo(conexao):

        codigo = int(input('Digite o código da manifestação que desejada listar: '))
        print()

        try:
            comandoSql = "select * from manifestacao where codigo = " + str(codigo)
            manifestacoes = listarBancoDados(conexao, comandoSql)

            if len(manifestacoes) == 0:
                print('Não existe manifestação com este código!')
            else:
                for i in manifestacoes:
                    print('Código:', i[0])
                    print('Título:', i[1])
                    print('Descrição:', i[2])
                    print('Tipo:', i[3])
                    print('Autor:', i[4])

        except ValueError:
            print('Não existe manifestação com este código!')
