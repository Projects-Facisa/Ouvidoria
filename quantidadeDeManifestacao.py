from operacoesbd import *

def listarQuantidadeDeManifestacao(conexao):
    comandoSql = "select count(*) from manifestacao"  # Quantidade de Manifestações
    manifestacoes = listarBancoDados(conexao, comandoSql)
    manifestacoes = manifestacoes[0][0]

    print('Quantidade de manifestações:', manifestacoes)
    print()

    comandoSql = "select count(*) from manifestacao where tipo = 'Reclamacao'"  # Quantidade de Reclamações
    manifestacoes = listarBancoDados(conexao, comandoSql)
    countReclamacao = manifestacoes[0][0]

    print('Quantidade de reclamações:', countReclamacao)
    print()

    comandoSql = "select count(*) from manifestacao where tipo = 'Sugestao'"  # Quantidade de Sugestões
    manifestacoes = listarBancoDados(conexao, comandoSql)
    countSugestao = manifestacoes[0][0]

    print('Quantidade de sugestões:', countSugestao)
    print()

    comandoSql = "select count(*) from manifestacao where tipo = 'Elogio'"  # Quantidade de Elogios
    manifestacoes = listarBancoDados(conexao, comandoSql)
    countElogio = manifestacoes[0][0]

    print('Quantidade de elogios:', countElogio)