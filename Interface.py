#Menu
from Banco import banco
from usuario import Usuario

while True:

    print("///BEM VINDO AO CADASTRO DE USUARIO///")
    print('''
\033[31m[1]Cadastrar Usuario\033[0m
\033[32m[2]Apagar Usuario\033[0m
\033[33m[3]Ver Usuarios Cadastrados\033[0m
\033[34m[4]Sair\033[0m
          ''')
    menu = int(input("por favor selecione uma opção: "))

    #CADASTRAR USUARIO
    if menu == 1:
        nome = input("Nome Completo: ").strip().capitalize()
        senha = input("Senha: ").strip()
        user = Usuario(idusuario=0, nome=nome, senha=senha)
        mensage = user.inserirUsuario()
        print(mensage)

        op = input("Deseja adicionar mais algum usuario?: ").upper()
        while op != "N":
            nome = input("Nome Completo: ").strip().capitalize()
            senha = input("Senha: ").strip()
            user = Usuario(nome=nome, senha=senha)
            op = input("Deseja adicionar mais algum usuario?: ").upper()
            mensage = user.inserirUsuario()
            print(mensage)

    #APAGAR USUARIO
    elif menu == 2:
        pessoas = banco().SelectTable()
        if not pessoas:  # Verifica se a lista está vazia
            print("Nenhum usuário cadastrado.")
            continue

        for k, p in enumerate(pessoas):
            print(f"Pessoa[{k}]: Nome: {p[1]} Senha{p[2]}")

        op = int(input("Digite qual o usuario você quer DELETAR: "))

        if op >= len(pessoas):
            print("TENTE NOVAMENTE!")
        else:
            op2 = input(f"Deseja mesmo DELETAR a pessoa número {op}?: ").upper()
            if op2 == "S":
                banco().deleteUser(pessoas[op][0]) 
            else:
                print("Cancelado!")

    #MOSTRAR PESSOAS
    elif menu == 3:
        pessoas = banco().SelectTable()
        for k, p in enumerate(pessoas):
            print(f"Pessoa[{k}]: Nome: {p[1]} Senha: {p[2]}")

    #SAIR (sinceramente, se você precisa disso pra saber oq a função BREAK faz, se mata pfvr)
    elif menu == 4:
        break

    else:
        print("Erro!")