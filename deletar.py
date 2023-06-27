from operacoesbd import *

'''
linha 14 pede int para as entradas no if ficaram como int, e para rodar no sql sem problema caso
a pessoa bote uma letra para o sql pesquisar na column codigo,
depois transforma em string na linha 15 para integrar no codigo do sql.
'''

def deletarManifestacao(conexao):
    codigo = 'entrada'  # variavel para rodar o while abaixo
    while codigo != 0:
        try:
            codigo = int(input('Digite o código da manifestação ou (0).Para voltar: '))
            consultaListagem = 'select * from manifestacao where codigo = ' + str(codigo)  # código sql para pegar a row
            listarPorCodigo = listarBancoDados(conexao, consultaListagem)  # criada a variavel que pega o valor da row

            if codigo == 0:  # feedaback para retorno
                print()
                print('Voltando...')

            elif len(listarPorCodigo) == 0:  # verifica o tamanho da row para dar feedaback caso esteja vazia
                print()
                print('Não há manifestação cadastrada neste codigo!')
                print()

            else:  # print da manifestação do código para confirmação
                print()
                print('Deseja exlucir a manifestação abaixo?')

                for i in listarPorCodigo:
                    print()
                    print('Código:', i[0])
                    print('Título:', i[1])
                    print('Descrição:', i[2])
                    print('Tipo:', i[3])
                    print('Autor:', i[4])
                    print()
                    print('(1).Sim (2).Não')

                opcao = 'entrada'  # variavel para rodar o while abaixo
                while opcao != 2:  # while para continuar pedindo o input caso digite código inválido ou string
                    try:
                        opcao = int(input(': '))

                        if opcao == 1:
                            deletarSql = 'delete from manifestacao where codigo = %s'  # código sql para pegar a row específica do código inserido
                            valores = [codigo]
                            excluirBancoDados(conexao, deletarSql, valores)  # executa a linha 41 no servidor sql
                            print()
                            print('Manifestação excluida com sucesso!')
                            opcao = 2

                        elif opcao == 2:
                            print()
                            print('Voltando...')

                        elif opcao != 2:
                            raise ValueError  # caso a opcao não for 1 ou 2 vai pro mesmo except como se fosse o input fosse string

                    except ValueError:
                        print('Opção invalida! Tente: (1).Sim (2).Não')
                    codigo = 0

        except ValueError:
            print()
            print('Código inválido!')
            print()