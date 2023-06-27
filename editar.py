from operacoesbd import *

'''
Linha 13 - Pq Pedir o input como int se terei que transformar-lo para str na linha 14 ?
Optei por esse tratamento pois isso impede que caso eu digite uma string no input da linha 13
o codigo dê pau e o programa se feche apresentando a seguinte mensagem de erro : Unknown column '(any str)' in 'where clause'
Finalizando entende-se que a linha 14 procura por uma coluna que não existe e por isso se fecha.
'''
def editarManifestacao(conexao):
    codigo = 'entrada' #Variavel que serve para manter o while de baixo funcionando
    while codigo != 0:
        try:
            codigo = int(input('Digite o código da manifestação ou (0).Para voltar: '))  #Input que pede o Codigo da manifestação em questão a ser editada.
            consultaListagemSql = 'select * from manifestacao where codigo =' + str(codigo) #Variavel que determina o comando a ser executado
            consultaListagem = listarBancoDados(conexao, consultaListagemSql) #Variavel que envia e executa o comando da linha 14 pro servidor do mysql

            if codigo == 0: #Opção dada na linha 13 Caso o operador da Ouvidoria Deseje voltar ao menu principal sem alterar nada do banco.
                print('Voltando...')

            elif len(consultaListagem) == 0:
                print()
                print('Não há manifestações cadastradas nesse codigo')
                print()
            else:
                print()
                print('Você deseja editar a manifestação abaixo ?')
                print()

                for i in consultaListagem: #Janela de confirmação printando todas as informações do codigo a ser editado em questão
                    print('Código:', i[0])
                    print('Título:', i[1])
                    print('Descrição:', i[2])
                    print('Tipo:', i[3])
                    print('Autor:', i[4])
                    print()
                    print('(1).Sim (2).Não')
                opcao = 'entrada' #Variavel que serve para manter o while de baixo funcionando

                while opcao != 2:
                    try:
                        opcao = int(input('= '))

                        if opcao == 1:
                            print()
                            novoTitulo = input('Digite o novo título da manifestação: ')
                            novaDescricao = input('Digite a nova descrição: ')

                            sqlAtualizar = 'update manifestacao set titulo = %s, descricao = %s where codigo = %s' #Variavel que determina o comando a ser executado
                            valores = [novoTitulo, novaDescricao, codigo] #Variavel que guarda os valores a serem alterados
                            atualizarBancoDados(conexao, sqlAtualizar, valores) #Variavel que envia e executa o comando da linha 48 e 49 pro servidor do mysql
                            print()
                            print('Edição realizada com sucesso!')
                            opcao = 2

                        elif opcao == 2:
                            print()
                            print('Voltando...')

                        elif opcao != 2:
                            raise ValueError
                            #Comando Raise serve pra englobar 2 possiveis erros na opção
                            #Da linha 41 caso a entrada seja um numero maior que 2 ou 0 e caso seja uma str
                            #Fazendo com que o try da linha 40 vá direto pro except ValueError com feedback de opção Inválida
                            #Recomendando as opções corretas de continuar com a edição (1). Ou Cancelar e Retornar pro Menu Principal (2).

                    except ValueError:
                        print('Opção inválida! Tente: (1).Sim (2).Não')
                    codigo = 0

        except ValueError:
            print()
            print('Código inválido!')
            print()
