#cadastro
produtos = {}
quantidade_produto = 0
codigo_produto = 0
valor_produto = 0
nome_produto = 0
def cadastrar():
    from menu import menu
    import os
    while True:
        global quantidade_produto
        global nome_produto
        global codigo_produto
        global valor_produto
        nome_produto = input("Digite o nome do produto aqui: ")
        try:
            quantidade_produto = int(input(f"Digite a quantidade de {nome_produto}: "))
        except:
            print("vc digitou um valor quebrado ou um texto, por favor digite um valor correto")
            os.system("cls")
            continue
        try:
            codigo_produto = int(input(f"Digite o codigo do produto: "))
        except:
            print("vc digitou um valor quebrado ou um texto, por favor digite um valor correto")
            os.system("cls")
            continue
        try:
            valor_produto = float(input("Digite o valor do produto: "))
        except:
            print("vc digitou um valor quebrado ou um texto, por favor digite um valor correto")
            os.system("cls")
            continue
        produtos[codigo_produto] =[quantidade_produto, nome_produto, valor_produto] 
        terminar = input("Vc desaja cadastrar algum outro produto? (s/n): ")
        if terminar.lower() == "s":
            continue
        elif terminar.lower() == "n":
            import os
            os.system("cls")
            menu()
        print(f"Produtos cadastrados: {produtos}")
        


def retirar():
    from menu import menu
    import os 
    import time
    while True:
        global quantidade_produto
        global nome_produto
        global codigo_produto
        global valor_produto
        from menu import menu
        try:
            # bug para consertar, quando retiro uma unidade ele sempre retira da ultima chave, e o objetivo é fazer ele tirar uma unidade apenas do produto q foi digitado.By: Gemini
            retira = int(input("Digite o codigo do produto vendido: "))
            if retira in produtos:
                if produtos[retira][0] > 0:
                    produtos[retira][0] -= 1
                    print(produtos)
                
            time.sleep(3)
            os.system("cls")
            menu()
            break
        except KeyError:
            print(f"Erro: O produto '{retira}' não foi encontrado no dicionário.")
            continue
    
def consultar():
    from menu import menu
    import os
    import time
    while True:
        print(f"Os produtos cadastrados são: {produtos}")
        voltar = input("Vc deseja voltar para o menu? (s/n): ")
        match voltar.lower():
            case "s":
               os.system("cls")
               menu()
            case "n":
               os.system("cls")
            case _:
                print("vc digitou uma opção inexistente, tente novamente")
                time.sleep(2)
                os.system("cls")
                continue
        
