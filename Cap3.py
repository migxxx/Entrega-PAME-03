import time
import random
import string


class consultor():
    # ID UNICO, USUARIO E SENHA PARA LOGAR
    def __init__(self, id, usuario, senha) -> None:
        
        self.id = id
        self.usuario = usuario
        self.senha = senha



class gerente():
    # ID UNICO, USUARIO E SENHA PARA LOGAR
    def __init__(self, id, usuario, senha) -> None:

        self.id = id
        self.usuario = usuario
        self.senha = senha



# classe iniciada junto com o sistema, logo tem as infos basicas e gerais, como listas e dados.

class sistema():
    
    def __init__(self) -> None:
        
        self.sysConsultores = []
        self.sysGerentes = []
        self.sysProjetos = []
        self.sysSenhas = []

class delProjeto(sistema):

    def __init__(self, nome) -> None:

        removeu = False
        nome = input("Digite o nome do projeto: ")
        for projetos in self.sysProjetos:
            if nome == projetos[0]:
                self.sysProjetos.remove(projetos)
                print(f"{projetos} removido com sucesso")
                removeu = True
                time.sleep(1.4)
        if removeu == False:
            print("Esse projeto não existe.")
        


class projeto(sistema):

    def __init__(self, nome = "", consultor = "", gerente = "") -> None:
        
        if nome == "":
            self.setNome()
        else:
            self.nome = nome

        if consultor == "":
            self.setConsultor()
        else:
            self.consultor = consultor

        if gerente == "":
            self.setGerente()
        else:
            self.gerente = gerente


    def setNome(self):
        while True:
            self.nome = input("Digite o nome do projeto: ")
            if len(self.nome) > 1:
                break
            else:
                print("Nome invalido, digite novamente: ")
                time.sleep(1.4)
            

    def setConsultor(self):

        while True:
            try:
                pergunta = input("Esse projeto possui um consultor? (s/n) ")
                if pergunta == "s":
                    self.consultor = input("Digite o nome do consultor: ")
                    if len(self.consultor) > 0 and self.consultor.capitalize in self.sysConsultores:
                        break
                    else:
                        raise ValueError
                elif pergunta == "n":
                    self.consultor = None
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Escolha fora do padrão (s/n), favor digitar corretamente.")
                time.sleep(1.4)


    def setGerente(self):

        while True:
            try:
                self.gerente = input("Digite o nome do gerente envolvido no projeto: ")
                if len(self.gerente) > 0:
                    for gerentes in self.sysGerentes:
                        if gerentes[0] == self.gerente:
                            self.sysProjetos += [self.nome, self.consultor, self.gerente],
                            print(f"Novo projeto ({self.nome}) adicionado com sucesso.")
                            time.sleep(1.4)
                            break
                else:
                    raise ValueError

            except ValueError:
                print("Nome inválido, digite novamente.")
                time.sleep(1)


class pessoas(sistema):
    def __init__(self, opcao) -> None:
        super().infos()

        if opcao == "1":
            self.usuario = input("Digite o usuario: ")
            self.__senha = input("Digite sua senha: ")
            self.id = self.ran_gen(5)
            print("Criando")
            time.sleep(1)
            self.sysConsultores.append([self.usuario.capitalize(), self.id],)
            print(self.sysConsultores)
            print("Sucesso")
        
        elif opcao == "2":
            nome = input("Digite o nome do Consultor que deseja remover: ")
            for consultor in self.sysConsultores:
                if consultor[0] == nome.capitalize():
                    removeu = True
                    self.sysConsultores.remove(consultor)

            if removeu == False:
                print("Consultor inexistente.")
                time.sleep(1)
        
        elif opcao == "3":
            self.usuario = input("Digite o usuario: ")
            self.__senha = input("Digite sua senha: ")
            self.id = self.ran_gen(6)
            self.sysGerentes.append([self.usuario.capitalize(), self.getSenha(), self.id])

        elif opcao == "4":
            nome = input("Digite o nome do Gerente que deseja remover: ")
            for gerente in self.sysGerentes:
                if gerente[0] == nome.capitalize():
                    removeu = True
                    self.sysConsultores.remove(consultor)

            if removeu == False:
                print("Gerente inexistente.")
                time.sleep(1)

        elif opcao == "5":
            escolha = input("O que deseja listar?\n>>> (1) Consultores\n>>> (2) Gerentes\n>>> (3) Projetos\n>>> ")
            if escolha == "1":
                print(self.sysConsultores)
            elif escolha == "2":
                for pessoa in self.sysGerentes:
                    print(pessoa)
            elif escolha == "3":
                for proj in self.sysProjetos:
                    print(proj)
    
    def ran_gen(self, size, chars=string.ascii_uppercase + string.digits): 
        return ''.join(random.choice(chars) for x in range(size))

    def getSenha(self):
        return self.__senha



def main():

    while True:
        print("""=================== MENU ===================
        
>>> (1) Projetos
>>> (2) Consultores e Gerentes
>>> (3) Sair
>>> (9) Login (Gerente / Consultor)""")
        
        opcao = input("Escolha uma opção:\n>>> ")
        if opcao == "1":
            while True:
                print("""=================== Projetos ===================
            
>>> (1) Criar novo projeto
>>> (2) Remover projeto
>>> (3) Voltar""")

                opcaoproj = input("O que deseja realizar?\n>>> ")
                if opcaoproj == "1":
                    novoProjeto = projeto()
                    time.sleep(1.4)

                elif opcaoproj == "2":
                    deletarProj = delProjeto()
                    time.sleep(1.4)
                
                elif opcaoproj == "3":
                    break
                else:
                    print("Opcao inexistente.")
                    time.sleep(1)
                    pass

        elif opcao == "2":
            while True:
                print("""=================== Consultores e Gerentes ===================
                
>>> (1) Criar Consultor
>>> (2) Remover Consultor
>>> (3) Criar Gerente
>>> (4) Remover Gerente
>>> (5) Listar
>>> (6) Voltar""")
                
                opcaoPessoas = input("O que deseja realizar?\n>>> ")

                if opcaoPessoas == "1":
                    pessoas("1")
                elif opcaoPessoas == "2":
                    pessoas("2")    
                elif opcaoPessoas == "3":
                    pessoas("3")
                elif opcaoPessoas == "4":
                    pessoas("4")
                elif opcaoPessoas == "5":
                    pessoas("5")
                elif opcaoPessoas == "6":
                    break
        
        elif opcao == "3":
            quit()

        elif opcao == "9":
            return





# Usuario nao logado

if __name__ == '__main__':
    main()
