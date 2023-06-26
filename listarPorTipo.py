from operacoesbd import *

def listarManifestacaoPorTipo(conexao):  # Metodo para Listar manifestacao por Tipo
    opcao = int(input('Digite o número da sua opcão: '))

    if opcao < 0 or opcao > 3:  # Teste de Opcao Invalida
        print('Opcao Invalida!')
        print() 
    else:
        if opcao == 1:   # TIPO ELOGIO
            tip = "'Elogio'"
            tipoPlural = 'Elogios'

        elif opcao == 2:   # TIPO SUGESTAO
            tip = "'Sugestao'"
            tipoPlural = 'Sugestões'

        elif opcao == 3:    # TIPO RECLAMACAO
            tip = "'Reclamacao'"
            tipoPlural = 'reclamações'

        if opcao == 0:     # VOLTAR AO MENU PRINCIPAL
            print('Voltando...')

        else:   # CONFIRMACAO DE LEITURA DE OPCAO
            consultaListagem = 'select * from manifestacao where tipo = ' + tip
            resultado = listarBancoDados(conexao, consultaListagem)

            if len(resultado) == 0:    # teste se ha manifestacao no tipo escolhido
                print('Não há', tipoPlural,'a serem listados!')
                print()
            else:        # Execucao da Listagem por Codigo
                manifestacao = listarBancoDados(conexao, consultaListagem)
                for i in manifestacao:
                    print('codigo', i[0], '-', i[1], '-', i[4])