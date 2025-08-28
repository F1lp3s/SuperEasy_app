cadastro = {}
email = ""
senha = ""
def logar():
    import os
    import time
    os.system("cls")
    l_email = input("Digite seu email: ")
    l_senha = input("Digite sua senha: ")   
    for i in cadastro:
        if i == l_email and cadastro[i] == l_senha:
            from menu import menu
            os.system("cls")
            menu()
    os.system("cls")
   
def cadastrar():
    import os
    import time
    os.system("cls")
    global email, senha
    email = input("Coloque seu email: ")
    senha = input("Coloque sua senha: ")
    cadastro[email] = senha
    print(cadastro)
    time.sleep(2)
    os.system("cls")
    inicio()



def inicio():
    import os
    import time
    while True:
        print("---------------------------------------------")
        print("BEM VINDO AO SUPEREASY.")
        print("---------------------------------------------")
        inicio = input("Vc gostaria de logar ou cadastrar?: ")
        match inicio:
            case "logar":
                logar()
            case "cadastrar":
                cadastrar()
            case _:
                print("Vc digitou uma opção não existente, tente novamente.")
                time.sleep(3)
                os.system("cls")
inicio()
