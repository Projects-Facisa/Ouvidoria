'''
GRUPO : 
Marcleidson José Fernandes De Oliveira
Yuri Diego Almeida Silva dos Santos
Silas Miguel Sarmento Araújo
Alex Junior Ferreira dos Santos
João Vitor Pereira da Silva
Severino Ferreira da Silva Neto
'''

# Sistema de ouvidoria com integração do banco de dados

from listarTudo import *
from listarPorTipo import *
from addManifestacao import *
from quantidadeDeManifestacao import *
from pesquisarPorCodigo import *
from editar import *
from deletar import *

conexao = abrirBancoDados('localhost', 'root', '1243', 'ouvidoria')

opcao = 0
while opcao != 8:   # Menu Principal
    print()
    print()
    print('                                 ===\   MENU DE MANIFESTAÇÕES   /===')
    print('(1).ListarTodos (2).ListarTipo (3).Criar (4).Quantidade (5).Pesquisar (6).Editar (7).Excluir (8).Sair')
    print()
    print()

    try:
        opcao = int(input('Digite o número da opção: '))

        if opcao == 1:   # Listar todos
            listarTodasAsManifestacoes(conexao)

        elif opcao == 2:   # Listar por tipo
            print()
            print()
            print('                                   ===\   LISTAGEM POR TIPO   /===')
            print('                       Tipo: (1).Elogio (2).Sugestão (3).Reclamação (0).Voltar')
            print()
            print()
            listarManifestacaoPorTipo(conexao)

        elif opcao == 3:   # Criar Manifestação
            print()
            print()
            print('                                  ===\   CRIAR MANIFESTAÇÃO   /===')
            print('                       Tipo: (1).Elogio (2).Sugestão (3).Reclamação (0).Voltar')
            print()
            print()
            criarManifestacao(conexao)

        elif opcao == 4:   # Quantidade de Manifestações
            print()
            print()
            print('                              ===\   QUANTIDADE DE MANIFESTAÇÕES   /===')
            print()
            print()
            listarQuantidadeDeManifestacao(conexao)

        elif opcao == 5:   # Pesquisar por Código
            print()
            print()
            print('                                 ===\   PESQUISAR POR CÓDIGO   /===')
            print()
            print()
            pesquisarManifestacaoPorCodigo(conexao)

        elif opcao == 6:   # Editar Manifestação
            print()
            print()
            print('                                  ===\   EDITAR MANIFESTAÇÃO   /===')
            print()
            print()
            editarManifestacao(conexao)

        elif opcao == 7:   # Excluir Manifestação
            print()
            print()
            print('                                 ===\   EXCLUIR MANIFESTAÇÃO   /===')
            print()
            print()
            deletarManifestacao(conexao)

        elif opcao != 8:   # Opção inválida para números
            print()
            print('Opção inválida!')

    except ValueError:   # Opção inválida para letras
        print()
        print('Opção inválida!')

print()
print('Saindo...')

encerrarBancoDados(conexao)
