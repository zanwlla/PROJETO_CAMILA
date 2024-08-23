import os

class Plano:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return f"{self.nome} - R${self.valor:.2f}"

class Cliente:
    def __init__(self, nome, telefone, plano, ativo=True):
        self.nome = nome
        self.telefone = telefone
        self.plano = plano
        self.ativo = ativo
        self.avaliacoes = []

    def __str__(self):
        status = "Ativo" if self.ativo else "Desativado"
        return f"{self.nome.ljust(20)} |  {self.telefone.ljust(15)} | {status.ljust(15)} | {self.plano.nome.ljust(20)} "

    def ativar_desativar(self):
        self.ativo = not self.ativo
        return f"O status do cliente {self.nome} foi alterado para {'Ativo' if self.ativo else 'Desativado'}."

    def adicionar_avaliacao(self, nota):
        self.avaliacoes.append(nota)

    def calcular_media_avaliacoes(self):
        if self.avaliacoes:
            media = sum(self.avaliacoes) / len(self.avaliacoes)
            return f"Cliente {self.nome} - Média de Avaliações: {media:.2f}"
        else:
            return f"Cliente {self.nome} ainda não possui avaliações."

class ProgramaAcademia:
    def __init__(self):
        self.planos = [
            Plano('Mensal', 100.00),
            Plano('Bimestral', 195.00),
            Plano('Trimestral', 270.00),
            Plano('Semestral', 540.00),
            Plano('Anual', 1000.00),
            Plano('Aula experimental', 25.00),
            Plano('Avaliação Física', 25.00)
        ]
        
        self.clientes = [
            Cliente('Mariana', '41965237584', self.planos[0], True),
            Cliente('Luciano', '11974586584', self.planos[1], False),
            Cliente('Cecília', '21985476554', self.planos[2], True),
        ]

    def finalizar_app(self):
        os.system("cls")
        print("Finalizando o app\n")

    def voltar_menu_principal(self):
        input("Digite uma tecla para voltar ao menu principal: ")

    def mostrar_subtitulo(self, texto):
        os.system("cls")
        linha = '*'*(len(texto))
        print(texto)
        print()

    def escolher_opcoes(self):
        self.mostrar_subtitulo('''
            𝓐𝓬𝓪𝓭𝓮𝓶𝓲𝓪 𝓑𝓸𝓭𝔂 𝓗𝓪𝓻𝓭''')

        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Ativar/Desativar Cliente")
        print("4 - Avaliar Espaço da Academia")
        print("5 - Ver Média de Avaliações")
        print("6 - Sair\n")

    def opcao_invalida(self):
        self.mostrar_subtitulo("Opção inválida\n".ljust(20))
        self.voltar_menu_principal()

    def listar_clientes(self):
        self.mostrar_subtitulo('Listando os Clientes'.ljust(20))
        print("Nome:".ljust(20), "Telefone:".ljust(15),  "  Status:".ljust(22), "   Plano:".ljust(20), )
        for cliente in self.clientes:
            print(cliente)

    def alternar_estado_cliente(self):
        self.mostrar_subtitulo("Alterando o estado do cliente".ljust(20))
        self.listar_clientes()
        nome_cliente = input("Digite o nome do cliente que deseja alterar: ")
        cliente_encontrado = False

        for cliente in self.clientes:
            if nome_cliente == cliente.nome:
                cliente_encontrado = True
                mensagem = cliente.ativar_desativar()
                print(mensagem)
                break

        if not cliente_encontrado:
            print("O cliente não foi encontrado.")

        self.voltar_menu_principal()

    def avaliacao(self):
        self.mostrar_subtitulo("Avaliar Espaço da Academia\n".ljust(20))
        self.listar_clientes()

        nome_cliente = input("Digite seu nome para avaliar nosso ambiente: ")
        cliente_encontrado = False

        for cliente in self.clientes:
            if nome_cliente == cliente.nome:
                cliente_encontrado = True
                while True:
                    nota = int(input("Digite uma nota de 1 a 5 para avaliar o espaço da academia: "))
                    if 1 <= nota <= 5:
                        cliente.adicionar_avaliacao(nota)
                        print(f"Você avaliou o espaço da academia com a nota {nota}.")
                        break
                    else:
                        print("Por favor, digite uma nota válida (entre 1 e 5).")

        if not cliente_encontrado:
            print("Cliente não encontrado.")

        self.voltar_menu_principal()

    def ver_media_avaliacoes(self):
        self.mostrar_subtitulo("Média de Avaliações dos Clientes\n".ljust(20))
        for cliente in self.clientes:
            print(cliente.calcular_media_avaliacoes())

        self.voltar_menu_principal()

    def cadastrar_novo_cliente(self):
        nome_cliente = input("Digite o nome do novo cliente: ")
        telefone = input(f'Digite o telefone de {nome_cliente}: ')
        
        print("\nEscolha o plano para o cliente:")
        for i, plano in enumerate(self.planos):
            print(f"{i+1} - {plano}")

        plano_escolhido = None
        while True:
            opcao_plano = int(input("Digite o número do plano desejado: "))
            if 1 <= opcao_plano <= len(self.planos):
                plano_escolhido = self.planos[opcao_plano-1]
                break
            else:
                print("Opção inválida, por favor, escolha um plano válido.")
        
        cliente_novo = Cliente(nome_cliente, telefone, plano_escolhido)
        self.clientes.append(cliente_novo)
        print(f"Você cadastrou o cliente: {nome_cliente} no plano {plano_escolhido.nome}")

    def main(self):
        while True:
            try:
                self.escolher_opcoes()
                opcao_digitada = int(input("Digite a opção desejada: "))
                if opcao_digitada == 1:
                    print("Você escolheu cadastrar cliente\n")
                    self.cadastrar_novo_cliente()
                elif opcao_digitada == 2:
                    self.listar_clientes()
                    self.voltar_menu_principal()
                elif opcao_digitada == 3:
                    self.alternar_estado_cliente()
                elif opcao_digitada == 4:
                    self.avaliacao()
                elif opcao_digitada == 5:
                    self.ver_media_avaliacoes()
                elif opcao_digitada == 6:
                    print("Você escolheu sair do aplicativo\n")
                    self.finalizar_app()
                    break
                else:
                    self.opcao_invalida()
            except ValueError:
                print("Por favor, digite um número válido.")

if __name__ == "__main__":
    programa = ProgramaAcademia()
    programa.main()
