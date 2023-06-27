from operacoesbd import *

def criarManifestacao(conexao):
    opcao = 1
    while opcao != 0:
        try:
            opcao = int(input('Digite o número da sua opcão: '))

            if opcao < 0 or opcao > 3:
                print()
                print('Opção inválida!')
                print()

            else:
                tipo = ''
                if opcao == 1:
                    tipo = 'Elogio'

                elif opcao == 2:
                    tipo = 'Sugestao'

                elif opcao == 3:
                    tipo = 'Reclamacao'

                if opcao == 0:
                    print()
                    print('Voltando...')

                else:
                    print()
                    titulo = input('Digite o título: ')
                    descricao = input('Digite a descrição: ')
                    autor = input('Digite seu nome: ')

                    comandoSql = "insert into manifestacao (titulo, descricao, tipo, autor) values (%s, %s, %s, %s)"
                    dados = [titulo, descricao, tipo, autor]

                    insertNoBancoDados(conexao, comandoSql, dados)
                    print()
                    print('Manifestação cadastrada com sucesso!')
                    opcao = 0

        except ValueError:
            print()
            print("Opção inválida!")
            print()