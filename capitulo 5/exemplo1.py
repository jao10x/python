def validaLogin(nome, senha):
   if (nome == "Joao" and senha == "senha123"):
       return print("Seja bem vindo", nome, senha)
   else:
       return print("senha ou nome invalido")


print("===Digite seu nome===")
nome = input()
print("===Digite sua senha===")
senha = input()

validaLogin(nome, senha)