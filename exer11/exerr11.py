def __init__(self, nome, endereco, email):
    # nomeia as tabelas
    self.nome = nome
    self.endereco = endereco
    self.email = email
class Agenda:
    #Onde vai entrar os elementos digitados
    def __init__(self):
        self.contatos = []
    def adicionar_contato(self, contato):
        self.contatos.append(contato)
    def remover_contato(self, contato):
        self.contatos.remove(contato)
    def listar_contatos(self):
        
        for contato in self.contatos:
            print('Nome:', contato.nome)
            print('Endereço:', contato.endereco)
            print('E-mail:', contato.email)
            #Onde será mostrados os elementos
agenda = Agenda()
contato1 = contato('João', 'Rua A, 123', 'joao@example.com')
contato2 = contato('Maria', 'Rua B, 456', 'maria@example.com')
agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)
agenda.listar_contatos()
agenda.remover_contato(contato1)
agenda.listar_contatos()
