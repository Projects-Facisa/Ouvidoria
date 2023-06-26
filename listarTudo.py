from operacoesbd import *

def listarTodasAsManifestacoes(conexao):  # Metodo para listar todas as manifestacoes
    print()
    comandoSql = "select * from manifestacao"
    manifestacoes = listarBancoDados(conexao, comandoSql)   # Comando para consultar no Banco de Dados

    if len(manifestacoes) == 0:      # Teste se ha manifestacao no banco
        print('Não há manifestações a serem listadas!')

    else:
        for i in manifestacoes:        # Execucao da Listagem
            print('Código', i[0], '-', i[1], '-', i[4], '-', i[3])