from operacoesbd import *

def pesquisarManifestacaoPorCodigo(conexao):
    codigo = 'entrada'
    while codigo != 0:
        try:
            codigo = int(input('Digite o codigo da manifestação ou 0 para voltar: '))
            comandoSql = "select * from manifestacao where codigo = " + str(codigo)
            manifestacoes = listarBancoDados(conexao, comandoSql)

            if codigo == 0:
                print()
                print('Voltando...')
            elif len(manifestacoes) == 0:
                print('Não existe manifestação com este código!')
            else:
                for i in manifestacoes:
                    print('Código:', i[0])
                    print('Título:', i[1])
                    print('Descrição:', i[2])
                    print('Tipo:', i[3])
                    print('Autor:', i[4])
                codigo = 0
        except ValueError:
            print('Código inválido!')
