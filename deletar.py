from operacoesbd import *

def deletarManifestacao(conexao):
    codigo = 'entrada'
    while codigo != 0:
        try:
            print()
            codigo = int(input('Digite o codigo da manifestação ou 0 para voltar: '))
            consultaListagem = 'select * from manifestacao where codigo = ' + str(codigo)
            listarPorCodigo = listarBancoDados(conexao, consultaListagem)
            if codigo == 0:
                print()
                print('Voltando...')
            elif len(listarPorCodigo) == 0:
                print()
                print('Não há manifestações neste codigo!')
            else:
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
                    print('1)Sim 2)Não')

                    opcao = 'entrada'
                    while opcao != 2:
                        opcao = int(input(': '))
                        if opcao == 1:
                            deletarSql = 'delete from manifestacao where codigo = %s'
                            valores = [codigo]
                            excluirBancoDados(conexao, deletarSql, valores)
                            print()
                            print('Manifestação removida com sucesso!')
                            opcao = 2
                        elif opcao == 2:
                            print()
                            print('Voltando...')

        except ValueError:
            print()
            print('Código ou opção inválido(a)!')