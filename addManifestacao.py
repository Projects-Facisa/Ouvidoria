from operacoesbd import *

def criarManifestacao(conexao, opcao):
    while opcao != 0:
        opcao = int(input('Digite o número da sua opcão: '))
        tipo = ''
        if opcao == 1:
            tipo = 'Elogio'

        elif opcao == 2:
            tipo = 'Sugestao'

        elif opcao == 3:
            tipo = 'Reclamacao'

        elif opcao != 0:
            print('Opção inválida!')

        titulo = input('Digite o Título do elogio: ')
        descricao = input('Digite a Descrição do elogio: ')
        autor = input('Digite seu nome: ')

        comandoSql = "insert into manifestacao (titulo, descricao, tipo, autor) values (%s, %s, %s, %s)"
        dados = [titulo, descricao, tipo, autor]

        insertNoBancoDados(conexao, comandoSql, dados)
        print('Manifestação cadastrado com sucesso!')