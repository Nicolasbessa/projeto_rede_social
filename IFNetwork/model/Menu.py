from model.Usuario import Usuario

#apenas criando e deletando usuarios

opcao = int(input("seja bem vindo!\n"
      "\n opções:\n"
      "1 - criar novo usuário\n"
      "2 - deletar usuário\n")

try:
    if (opcao == 1):
        nome = input("informe seu nome: ")
        email = input("informe seu email: ")
        senha = input("informe a senha: ")
        genero = input("informe o seu gênero: ")
        idade = int(input("informe sua idade: "))
        profissao = input("informe sua profissão: ")
        cidade = input("informe sua cidade: ")
        u = Usuario(nome, email, senha, genero, idade, profissao, cidade)
        u.inserirUser()

    elif(opcao == 2):
        email = input("informe o email da conta a ser deletada: ")
        u.deletar()
except:
    print("opção inválida.")

