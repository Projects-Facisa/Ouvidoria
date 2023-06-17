from operacoesbd import *

def listarTodasAsManifestacoes(conexao):
    print()
    comandoSql = "select count(*) from manifestacao"
    manifestacoes = listarBancoDados(conexao, comandoSql)
    manifestacoes = manifestacoes[0][0]

    if manifestacoes == 0:
        print('Não há manifestações a serem listadas!')

    else:
        comandoSql = "select * from manifestacao"
        manifestacoes = listarBancoDados(conexao, comandoSql)

        for i in manifestacoes:
            print('Código', i[0], '-', i[1], '-', i[4], '-', i[3])