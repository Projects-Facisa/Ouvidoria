from operacoesbd import *

def editarManifestacao(conexao):

    codigo = input('Digite o codigo da manifestação : ')

    try:
        consultaListagemSql = 'select * from manifestacao where codigo =' + codigo
        consultaListagem = listarBancoDados(conexao, consultaListagemSql)
        if len(consultaListagem) == 0:
            print('Não há manifestações Cadastradas nesse Codigo')
        else:
            print('Você deseja editar a manifestação abaixo ?')
            print()

            for i in consultaListagem:
                print('Código:', i[0])
                print('Título:', i[1])
                print('Descrição:', i[2])
                print('Tipo:', i[3])
                print('Autor:', i[4])
                print()
                print('(1).Sim (2).Não')
            opcao=0
            while opcao != 2:
                opcao = int(input('= '))

                if opcao == 1:
                    novoTitulo = input('Digite o novo titulo da manifestação : ')
                    novaDescricao = input('Digite a nova Descrição : ')

                    sqlAtualizar = 'update manifestacao set titulo = %s, descricao = %s where codigo = %s'
                    valores = [novoTitulo, novaDescricao, codigo]
                    print('Edição Realizada com Sucesso !')
                    atualizarBancoDados(conexao, sqlAtualizar, valores)
                    opcao = 2
                elif opcao == 2:
                    print('Retornando...')

                elif opcao !=2:
                    print('Opção Invalida')
                    print()
                    print('Tente : (1).Sim (2).Não ')

    except ValueError:
        print('Código ou Opção inválido(a) !')


