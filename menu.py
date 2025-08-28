# menu
# lembrar de ter uma opção para adicionar novas unidades


def menu():
    while True:
        from cadastro_dos_produtos import cadastrar, retirar, consultar
        import os
        print("Logado...")
        print("----------------------------------------------------------")
        print("BEM VINDO AO SUPEREASY, O MELHOR SISTEMA DE SUPERMERCADO.")
        print("1- Cadastrar produtos")
        print("2- retirar produtos")
        print("3- consultar produtos")
        print("4- sair")
        print("----------------------------------------------------------")

        opcao = input("Digite sua opção aqui: ")

        match opcao:
                
                case "1":
                    os.system("cls")
                    print("cadastrando...")
                    cadastrar()
                case "2":
                    os.system("cls")
                    print("retirando")
                    retirar()
                    
                case "3":
                    os.system("cls")
                    print("consultando")
                    consultar()
                case "4":
                    print("saindo")
                    os.system("cls")
                    exit()

                case _:
                    os.system("cls")
                    print("vc digitou errado, tente novamente")


                
                

