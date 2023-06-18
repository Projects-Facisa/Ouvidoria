from operacoesbd import *

def deletarManifestacao(conexao):
    codigo = 'entrada'
    while codigo != 0:
        try:
            print()
            codigo = int(input('digite o codigo da manifestação ou 0 para voltar: '))
            consultaListagem = 'select * from manifestacao where codigo = ' + str(codigo)
            listarPorCodigo = listarBancoDados(conexao, consultaListagem)
            if codigo == 0:
                print()
                print('voltando...')
            elif len(listarPorCodigo) == 0:
                print()
                print('não há manifestações neste codigo')
            else:
                print('deseja exlucir a manifestação abaixo?')
                for i in listarPorCodigo:
                    print('Código:', i[0])
                    print('Título:', i[1])
                    print('Descrição:', i[2])
                    print('Tipo:', i[3])
                    print('Autor:', i[4])
                    print()
                    print('1)sim 2)não')

                    opcao = 'entrada'
                    while opcao != 2:
                        opcao = int(input(': '))
                        if opcao == 1:
                            deletarSql = 'delete from manifestacao where codigo = %s'
                            valores = [codigo]
                            excluirBancoDados(conexao, deletarSql, valores)
                            print()
                            print('manifestação removida!')
                            opcao = 2
                        elif opcao == 2:
                            print()
                            print('voltando...')

        except ValueError:
            print()
            print('código ou opção inválido(a)!')